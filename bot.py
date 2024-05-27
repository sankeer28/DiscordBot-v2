import discord
from discord.ext import commands
import requests
import random
import asyncio
import yt_dlp
import os

import google.generativeai as genai

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())
queues = {}
voice_clients = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn -filter:a "volume=0.25"'}

genai.configure(api_key="put your API key here")

model = genai.GenerativeModel('gemini-pro',
                              safety_settings=[
                                  {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
                                  {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                                  {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                                  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                                  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
                              ])

google_api_keys = [
    'put your API keys here', 'put your API keys here',
    'put your API keys here', 'put your API keys here',
    'put your API keys here', 'put your API keys here',
    'put your API keys here', 'put your API keys here'
]
current_api_key_index = 0
google_search_engine_id = 'search engine id here'
saucenao_api_key = 'saucenao API key here'
pexels_api_key = 'pexels API key here'


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}!")


@bot.command(name="drake", case_insensitive=True)
async def ask(ctx: commands.Context, *, prompt: str):
    response = model.generate_content(prompt)
    if len(response.text) > 2000:
        response_text = response.text[:1997] + "..."
    else:
        response_text = response.text
    await ctx.reply(response_text)

@bot.command(name="Drake", case_insensitive=True)
async def ask(ctx: commands.Context, *, prompt: str):
    response = model.generate_content(prompt)
    if len(response.text) > 2000:
        response_text = response.text[:1997] + "..."
    else:
        response_text = response.text
    await ctx.reply(response_text)

def get_google_api_key():
    global current_api_key_index
    api_key = google_api_keys[current_api_key_index]
    current_api_key_index = (current_api_key_index + 1) % len(google_api_keys)
    return api_key

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}!")
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
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
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
        data = response.json()
        gif_url = data[0]['url']
        return gif_url
    except Exception as e:
        print(f"An error occurred while fetching random cat GIF: {e}")
        return None

async def fetch_random_dog_gif():
    try:
        response = requests.get('https://api.thedogapi.com/v1/images/search?mime_types=gif')
        data = response.json()
        gif_url = data[0]['url']
        return gif_url
    except Exception as e:
        print(f"An error occurred while fetching random dog GIF: {e}")
        return None


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
    
    
@bot.command(name="play")
async def play(ctx: commands.Context):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as e:
        print(e)

    try:
        url = ctx.message.content.split()[1]
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

    
bot.run('Discord bot token here')
