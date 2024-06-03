https://github.com/sankeer28/DiscordBot-v2/blob/main/bot.pyimport discord
from discord.ext import commands
from discord import app_commands
import requests
import random
import asyncio
import yt_dlp
import os
import re
import aiohttp
import google.generativeai as genai
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


bot = commands.Bot(command_prefix='', intents=discord.Intents.all()) #---------------------------------ADD PREFIX HERE (OPTIONAL)
queues = {}
message_history = {}
voice_clients = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn -filter:a "volume=0.25"'}


#----------------------------------------------------------------------------------------------------------
#                                         API KEYS
#----------------------------------------------------------------------------------------------------------
google_api_keys = [

]
current_api_key_index = 0
google_search_engine_id = ' '
saucenao_api_key = ' '
pexels_api_key = ' '
genai.configure(api_key=" ")


#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold":  "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold":  "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold":  "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold":  "BLOCK_NONE"}
]
text_model = genai.GenerativeModel(model_name="gemini-pro", safety_settings=safety_settings)
image_model = genai.GenerativeModel(model_name="gemini-pro-vision", safety_settings=safety_settings)

@bot.event
async def on_ready():
    try:
        s = await bot.tree.sync()
        print(f'Synced {len(s)} commands')
    except Exception as e:
        print(f'Error syncing commands: {e}')
    
    print(f'Logged in as {bot.user.name}')

def get_google_api_key():
    global current_api_key_index
    api_key = google_api_keys[current_api_key_index]
    current_api_key_index = (current_api_key_index + 1) % len(google_api_keys)
    return api_key

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

    
MAX_HISTORY_LENGTH = 10 #--------------------------------------------------------------------CHANGE MAX HISTORY (OPTIONAL)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

@bot.event
async def on_message(message):
    if message.author == bot.user or message.mention_everyone:
        return
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel) or 'drake' in message.content.lower(): #----------------------CHANGE BOT's NAME
        cleaned_text = clean_discord_message(message.content)
        async with message.channel.typing():
            if message.attachments:
                print("Graphic uploaded by:" + str(message.author.id) + ": " + cleaned_text)
                for attachment in message.attachments:
                    if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
                        await message.add_reaction('🎨')
                        async with aiohttp.ClientSession() as session:
                            async with session.get(attachment.url) as resp:
                                if resp.status != 200:
                                    await message.channel.send('Unable to download the image.')
                                    return
                                image_data = await resp.read()
                                response_text = await generate_response_with_image_and_text(image_data, cleaned_text)
                                await split_and_send_messages(message, response_text, 1700)
                                return
            else:
                print("New Message FROM:" + str(message.author.id) + ": " + cleaned_text)
                await message.add_reaction('💬')
                if MAX_HISTORY_LENGTH == 0:
                    response_text = await generate_response_with_text(cleaned_text)
                    await split_and_send_messages(message, response_text, 1700)
                    return
                update_message_history(message.author.id, cleaned_text)
                response_text = await generate_response_with_text(get_formatted_message_history(message.author.id))
                update_message_history(message.author.id, response_text)
                await split_and_send_messages(message, response_text, 1700)
    if 'cat' in message.content.lower():
        gif_url = await fetch_random_cat_gif()
        if gif_url:
            await message.channel.send(gif_url)
    if 'dog' in message.content.lower():
        gif_url = await fetch_random_dog_gif()
        if gif_url:
            await message.channel.send(gif_url)
    await bot.process_commands(message)

async def fetch_random_cat_gif():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search?mime_types=gif') as response:
            data = await response.json()
            return data[0]['url'] if data else None


async def fetch_random_dog_gif():
    try:
        response = requests.get('https://api.thedogapi.com/v1/images/search?mime_types=gif')
        data = response.json()
        gif_url = data[0]['url']
        return gif_url
    except Exception as e:
        print(f"An error occurred while fetching random dog GIF: {e}")
        return None

def clean_discord_message(input_string):
    bracket_pattern = re.compile(r'<[^>]+>')
    cleaned_content = bracket_pattern.sub('', input_string)
    return cleaned_content

def update_message_history(user_id, text):
    if user_id in message_history:
        message_history[user_id].append(text)
        if len(message_history[user_id]) > MAX_HISTORY_LENGTH:
            message_history[user_id].pop(0)
    else:
        message_history[user_id] = [text]

def get_formatted_message_history(user_id):
    if user_id in message_history:
        return '\n\n'.join(message_history[user_id])
    return "No messages found for this user."

async def generate_response_with_text(message_text):
    prompt_parts = [message_text]
    response = text_model.generate_content(prompt_parts)
    if(response._error):
        return "❌" +  str(response._error)
    return response.text

async def generate_response_with_image_and_text(image_data, text):
    image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
    prompt_parts = [image_parts[0], f"\n{text if text else 'What is this a picture of?'}"]
    response = image_model.generate_content(prompt_parts)
    if(response._error):
        return "❌" +  str(response._error)
    return response.text

async def split_and_send_messages(message_system, text, max_length):
    messages = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    for string in messages:
        await message_system.channel.send(string)
        
#----------------------------------------------------------------------------------------------------------
#                                         FUNCTIONS FOR COMMANDS
#----------------------------------------------------------------------------------------------------------

@bot.command(name="image")
async def google_image_search(ctx: commands.Context, *, query: str):
    google_api_key = get_google_api_key()
    url = f'https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={google_search_engine_id}&q={query}&searchType=image'
    response = requests.get(url)
    data = response.json()
    if 'items' not in data:
        await ctx.reply("No images found.")
        return
    embeds = [
        discord.Embed(title=item['title'], url=item['link']).set_image(url=item['link'])
        for item in data['items']
    ]
    current_page = 0
    message = await ctx.send(embed=embeds[current_page])
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['⬅️', '➡️']
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == '⬅️':
                current_page = (current_page - 1) % len(embeds)
            elif str(reaction.emoji) == '➡️':
                current_page = (current_page + 1) % len(embeds)
            await message.edit(embed=embeds[current_page])
            await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break

@bot.command(name="google")
async def google_search(ctx: commands.Context, *, query: str):
    google_api_key = get_google_api_key()
    url = f'https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={google_search_engine_id}&q={query}'
    response = requests.get(url)
    data = response.json()
    if 'items' not in data:
        await ctx.reply("No results found.")
        return
    embeds = [
        discord.Embed(title=item['title'], url=item['link'], description=item['snippet'])
        for item in data['items']
    ]
    current_page = 0
    message = await ctx.send(embed=embeds[current_page])
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['⬅️', '➡️']
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == '⬅️':
                current_page = (current_page - 1) % len(embeds)
            elif str(reaction.emoji) == '➡️':
                current_page = (current_page + 1) % len(embeds)
            await message.edit(embed=embeds[current_page])
            await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break

@bot.command(name="youtube")
async def youtube_search(ctx: commands.Context, *, query: str):
    google_api_key = get_google_api_key()
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={query}&key={google_api_key}&type=video'
    response = requests.get(url)
    data = response.json()
    if 'items' not in data:
        await ctx.reply("No videos found.")
        return
    embeds = [
        discord.Embed(
            title=item['snippet']['title'],
            url=f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            description=item['snippet']['description']
        ).set_thumbnail(url=item['snippet']['thumbnails']['high']['url'])
        for item in data['items']
    ]
    current_page = 0
    message = await ctx.send(embed=embeds[current_page])
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    await message.add_reaction('▶️')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['⬅️', '➡️', '▶️']
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == '⬅️':
                current_page = (current_page - 1) % len(embeds)
            elif str(reaction.emoji) == '➡️':
                current_page = (current_page + 1) % len(embeds)
            elif str(reaction.emoji) == '▶️':
                await ctx.send(f"Here's the video URL: {embeds[current_page].url}")
            await message.edit(embed=embeds[current_page])
            await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break

@bot.command(name="sauce")
async def saucenao_search(ctx: commands.Context, *, image_url: str):
    url = f'https://saucenao.com/search.php?output_type=2&api_key={saucenao_api_key}&url={image_url}'
    response = requests.get(url)
    data = response.json()
    if 'results' not in data:
        await ctx.reply("No results found.")
        return
    results = [result for result in data['results'] if float(result['header']['similarity']) > 50][:3]
    if not results:
        await ctx.reply("No results with over 50% similarity.")
        return
    reply = "Top results:\n"
    for result in results:
        similarity = result['header']['similarity']
        data_info = result['data']
        reply += f"{similarity}% - {data_info.get('title', 'No title')} - {data_info.get('author_name', 'Unknown author')} - URL: {data_info['ext_urls'][0] if 'ext_urls' in data_info else 'No URL'}\n"

    await ctx.reply(reply)

@bot.command(name="pexels")
async def pexels_search(ctx: commands.Context, *, query: str):
    headers = {'Authorization': pexels_api_key}
    url = f'https://api.pexels.com/v1/search?query={query}'
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'photos' not in data or not data['photos']:
        await ctx.reply("No images found.")
        return
    photo = random.choice(data['photos'])
    image_url = photo['src']['original']
    await ctx.reply(image_url)

#----------------------------------------------------------------------------------------------------------
#                                         Music Playback
#----------------------------------------------------------------------------------------------------------
@bot.command(name="play")
async def play(ctx: commands.Context):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as e:
        print(e)
    try:
        query = ctx.message.content.split(maxsplit=1)[1]
        if query.startswith('http'):
            url = query
            await ctx.send(f"Playing from provided URL: {url}")
        else:
            with ytdl:
                search_result = ytdl.extract_info(f"ytsearch1:{query}", download=False)
            url = "https://www.youtube.com/watch?v=" + search_result['entries'][0]['id']
            await ctx.send(f"Playing from search result: {url}")
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        song = data['url']
        player = discord.FFmpegOpusAudio(song, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(player)
    except Exception as e:
        print(e)

@bot.command(name="pause")
async def pause(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as e:
        print(e)

@bot.command(name="resume")
async def resume(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as e:
        print(e)

@bot.command(name="stop")
async def stop(ctx: commands.Context):
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
    except Exception as e:
        print(e)
        
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

        
@bot.tree.command(name='ping', description='Display the latency of the bot!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! ||{round(bot.latency * 1000)}ms||')
    
@bot.command()
async def download(ctx, url: str):
    video_path = await download_video(url)
    if video_path:
        await ctx.send(file=discord.File(video_path))
        os.remove(video_path)
    else:
        await ctx.send("Sorry, I couldn't download the video from that URL.")
    
async def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best',
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
            return video_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None
    
@bot.command(name="sherlock")
async def sherlock(ctx, username: str):
    async with ctx.typing():
        process = await asyncio.create_subprocess_exec(
            'sherlock', username,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        while True:
            line = await process.stdout.readline()
            if not line:
                break
            decoded_line = line.decode('utf-8').strip()
            if decoded_line: 
                await ctx.send(decoded_line)
        await process.wait()
    if process.returncode != 0:
        error = await process.stderr.read()
        decoded_error = error.decode('utf-8').strip()
        if decoded_error:
            await ctx.send(f"Error: {decoded_error}")
            
            
def check_site(site, username, headers, session):
    uri_check = site["uri_check"].format(account=username)
    try:
        res = session.get(uri_check, headers=headers, timeout=10)
        estring_pos = site["e_string"] in res.text
        estring_neg = site["m_string"] in res.text
        if res.status_code == site["e_code"] and estring_pos and not estring_neg:
            return site["name"], uri_check
    except:
        pass
    return None

@bot.command()
async def expose(ctx, username):
    headers = {
        "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "en-US;q=0.9,en,q=0,8",
        "accept-encoding": "gzip, deflate",
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    async with ctx.typing():
        with requests.Session() as session:
            response = session.get("https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json")
            data = response.json()
            sites = data["sites"]
            total_sites = len(sites)
            found_sites = 0
            try:
                with ThreadPoolExecutor() as executor:
                    futures = {executor.submit(check_site, site, username, headers, session): site for site in sites}

                    for future in as_completed(futures):
                        try:
                            result = future.result()
                            if result:
                                site_name, uri_check = result
                                await ctx.send(f"- **{site_name}**: {uri_check}")
                                found_sites += 1
                                await asyncio.sleep(1)
                        except:
                            pass
            except TimeoutError:
                await ctx.send("Some sites took too long to respond and were skipped.")
            if found_sites:
                await ctx.send(f"The user **{username}** was found on {found_sites} sites.")
            else:
                await ctx.send(f"No sites found for the user **{username}**.")

voice_clients = {}

@bot.tree.command(name="join", description="Join a specified voice channel")
@app_commands.describe(channel_name="The name of the voice channel to join")
async def join(interaction: discord.Interaction, channel_name: str):
    channel = discord.utils.get(interaction.guild.voice_channels, name=channel_name)
    if channel is None:
        await interaction.response.send_message(f"Could not find a channel named '{channel_name}'.", ephemeral=True)
        return
    try:
        voice_client = await channel.connect()
        voice_clients[interaction.guild.id] = voice_client
        await interaction.response.send_message(f"Joined channel: {channel_name}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Error connecting to channel: {e}", ephemeral=True)


@bot.tree.command(name="speak", description="Convert text to speech and play it in the voice channel")
@app_commands.describe(text="The text to convert to speech")
async def speak(interaction: discord.Interaction, text: str):
    if interaction.user.voice is None or interaction.user.voice.channel is None:
        await interaction.response.send_message("You need to be in a voice channel to use this command.", ephemeral=True)
        return
    voice_channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client
    if voice_client is None:
        try:
            voice_client = await voice_channel.connect()
        except Exception as e:
            await interaction.response.send_message(f"Error connecting to voice channel: {e}", ephemeral=True)
            return
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)
    if voice_client.is_playing():
        voice_client.stop()

    file_path = "output.mp3"
    command = f'edge-tts --text "{text}" --voice en-US-SteffanNeural --write-media {file_path}'
    subprocess.run(command, shell=True, capture_output=True)
    await asyncio.sleep(1)
    def after_playing(error):
        if error:
            print(f'Error ')
        else:
            print('Text-to-speech finished successfully.')
        asyncio.run_coroutine_threadsafe(voice_client.disconnect(), bot.loop)
    voice_client.play(discord.FFmpegPCMAudio(file_path), after=after_playing)
    while voice_client.is_playing():
        await asyncio.sleep(1)
    os.remove(file_path)
    await interaction.response.send_message("Finished playing the text-to-speech message.", ephemeral=True)

#----------------------------------------------------------------------------------------------------------
#                                              NIGHTCORE                               
#----------------------------------------------------------------------------------------------------------

def download_video(url, output_file):
    ydl_opts = {
        'outtmpl': output_file,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_audio(video_file, output_audio, pitch=1.4):
    command = f'ffmpeg -i "{video_file}" -vn -af "asetrate=44100*{pitch},aresample=44100" -acodec libmp3lame "{output_audio}"'
    os.system(command)

def download_image(image_filename, api_choice, search_query=None):
    try:
        if api_choice == "anime":
            response = requests.get("https://pic.re/image")
            response.raise_for_status()
            image_url = response.url
        elif api_choice == "cat":
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            response.raise_for_status()
            data = response.json()
            if not data or 'url' not in data[0]:
                print("Error: No image URL found in response data.")
                return
            image_url = data[0]['url']
        elif api_choice == "random":
            response = requests.get("https://random.imagecdn.app/v1/image?width=1920&height=1080&format=json")
            response.raise_for_status()
            data = response.json()
            if not data or 'url' not in data:
                print("Error: No image URL found in response data.")
                return
            image_url = data['url']
        elif api_choice == "pexels":
            headers = {
                'Authorization': pexels_api_key
            }
            params = {
                'query': search_query,
                'per_page': 1,
                'orientation': 'landscape',
            }
            response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            if not data['photos']:
                print("Error: No image found for the given search query.")
                return
            image_url = data['photos'][0]['src']['large']
        else:
            print("Invalid API choice.")
            return

        image_data = requests.get(image_url).content
        with open(image_filename, 'wb') as f:
            f.write(image_data)
    except Exception as e:
        print(f"Error fetching image: {e}")

def combine_video_audio_image(image_file, audio_file, output_video, video_title):
    try:
        resized_image_file = "resized_" + image_file
        resize_command = f'ffmpeg -i "{image_file}" -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "{resized_image_file}" -y'
        os.system(resize_command)
        text = re.sub(r'\(.*?\)', '', re.sub(r'[\\/:*?"<>|]', '', video_title.replace("_", " ").replace("nightcore", "").strip()))
        text_command = f'ffmpeg -loop 1 -i "{resized_image_file}" -vf "drawtext=text=\'{text}\':x=w-tw-10:y=h-th-10:fontsize=40:fontcolor=black:shadowcolor=white:shadowx=2:shadowy=2" -r 30 "{image_file}_with_text.jpg"'
        os.system(text_command)
        command = f'ffmpeg -loop 1 -i "{image_file}_with_text.jpg" -i "{audio_file}" -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest "{output_video}"'
        os.system(command)
        os.remove(resized_image_file)
        os.remove(f"{image_file}_with_text.jpg")
    except Exception as e:
        print(f"Error combining video and audio: {e}")

@bot.tree.command(name="nightcore", description="Convert a YouTube video to nightcore")
@app_commands.describe(
    url="The YouTube video URL",
    image_choice="The choice of background image",
    audio_speed="The choice of audio speed",
    search_query="The search query for Pexels image (only used if image_choice is 'pexels')"
)
@app_commands.choices(
    image_choice=[
        app_commands.Choice(name="Anime", value="anime"),
        app_commands.Choice(name="Cat", value="cat"),
        app_commands.Choice(name="Random", value="random"),
        app_commands.Choice(name="Pexels", value="pexels")
    ],
    audio_speed=[
        app_commands.Choice(name="Spedup", value="fast"),
        app_commands.Choice(name="Slowed", value="slow")
    ]
)
async def nightcore(interaction: discord.Interaction, url: str, image_choice: app_commands.Choice[str], audio_speed: app_commands.Choice[str], search_query: str = None):
    await interaction.response.defer()
    video_info = yt_dlp.YoutubeDL().extract_info(url, download=False)
    video_title = "nightcore_" + re.sub(r'[\\/:*?"<>|]', '', video_info['title'].replace(" ", "_"))
    video_filename = "video.mp4"
    audio_filename = "audio.mp3"
    image_filename = "background_image.jpg"
    output_video = f"{video_title}.mp4"
    download_video(url, video_filename)
    pitch = 1.4 if audio_speed.value == "fast" else 0.9
    extract_audio(video_filename, audio_filename, pitch=pitch)
    download_image(image_filename, image_choice.value, search_query)
    combine_video_audio_image(image_filename, audio_filename, output_video, video_title)
    await interaction.followup.send(file=discord.File(output_video))
    os.remove(video_filename)
    os.remove(audio_filename)
    os.remove(image_filename)
    os.remove(output_video)



#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
@bot.command(name="!help")
async def help_command(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description=("Here are the available commands:\n\n"
                     "`drake <prompt>`: Generate content using the Generative AI model.\n"
                     "`image <query>`: Search for images using Google Custom Search.\n"
                     "`google <query>`: Perform a Google search.\n"
                     "`youtube <query>`: Search for videos on YouTube.\n"
                     "`sauce <image_url>`: Perform a reverse image search using SauceNAO.\n"
                     "`pexels <query>`: Search for images on Pexels.\n"
                     "`play <URL or query>`: Play music from the provided URL or search on YT. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)\n"
                     "`pause`: Pause the currently playing music.\n"
                     "`resume`: Resume the paused music.\n"
                     "`stop`: Stop the music and disconnect from the voice channel.\n"
                     "`download <URL>`: Downloads and returns video to chat. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)\n"
                     "`cat`: random cat gif.\n"
                     "`dog`: random dog gif.\n"
                     "`sherlock <username>`: returns all sites where the user has created an account. Uses [Sherlock-project](https://github.com/sherlock-project/sherlock)\n"
                     "`expose <username>`: returns all sites where the user has created an account. Uses modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python)\n"
                     "`/join`: Joins any specified voice channel, even without joining it yourself\n"
                     "`/speak`: Says anything in voice channel you want using Microsoft's text to speech \n"
                     "`/nightcore`: creates nightcore video or slowed down video given URL. Uses my personal [project](https://github.com/sankeer28/Spedup-Slowed-MV) \n"

                     ),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

    
#----------------------------------------------------------------------------------------------------------
#                                         DISCORD TOKEN
#----------------------------------------------------------------------------------------------------------

bot.run(' ')

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
