```
  ____  _                       _ ____        _     __     ______  
 |  _ \(_)___  ___ ___  _ __ __| | __ )  ___ | |_   \ \   / /___ \ 
 | | | | / __|/ __/ _ \| '__/ _` |  _ \ / _ \| __|___\ \ / /  __) |
 | |_| | \__ \ (_| (_) | | | (_| | |_) | (_) | ||_____\ V /  / __/ 
 |____/|_|___/\___\___/|_|  \__,_|____/ \___/ \__|     \_/  |_____|
                                                                   
```
Discord bot made using Python with many features including AI chat, music playback, video downloader, and more.

## Getting Started

### Prerequisites

- Python 3.12
- FFMPEG installed onto system PATH
- pip
## Features 
- Chat with the bot casually by calling its name and get immediate responses using Gemini AI.
- Returns images from Google.
- Search YouTube for videos.
- Finds the source of images by performing a reverse image search. Supports .png, .jpg, .jpeg, .gif, and .webp.
- Return images from Pexels.
- Download URLs from many different sources and return downloaded videos to the chat including SoundCloud, Youtube, Tiktok, Twitter(X), Instagram and [more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).
- Play the audio from the same URLs in voice chat or input a song title.
- Ability to store songs in a queue automatically if multiple play commands are used.
- Ask questions regarding uploaded images.
- Chat history is temporarily saved to memory to have more realistic conversations.
- Integration with [Sherlock](https://github.com/sherlock-project/sherlock) and other OSINT tools.
- Ability to join any voice channel in the server without the need to join the voice channel yourself.
- Ability to speak using text-to-speech in voice chat, allowing the bot to say whatever you want.

## Running locally
### Installing Dependencies

```bash
pip install -r requirements.txt
```

### Getting API Keys

- **Google Custom Search Engine API Key**: Obtain from the Google Cloud Console. [Guide](https://developers.google.com/custom-search/v1/overview)
- **Google API Keys**: Necessary for YouTube and Google Search. Obtain from the Google Cloud Console. [Guide](https://cloud.google.com/docs/authentication/api-keys)
- **Saucenao API Key**: Get from the SauceNAO website. [Guide](https://saucenao.com/user.php?page=search-api)
- **Pexels API Key**: Get from the Pexels website. [Guide](https://www.pexels.com/api/documentation/)
- **Google Gemini AI API KEY:** Get from Google AI Studio. [Here](https://aistudio.google.com/app/apikey)

### Running the Bot

1. Clone this repository:

```bash
git clone https://github.com/sankeer28/DiscordBot-v2.git
```

2. Navigate to the bot directory:

```bash
cd DiscordBot-v2
```

3. Fill in the API Keys on missing lines.
     - Line 26: Gemini API key, Google API keys, Google search engine id, Saucenao API, Pexels API
     - Last Line: Discord bot token
4. Rename the bot:
   - Line 83: change the bot's name from drake to your liking
     
5. Run the bot:

```bash
python bot.py
```
## Usage: type !help for all commands
- `drake <prompt>`: Generate content using the Generative AI model.
- `image <query>`: Search for images using Google Custom Search.
- `google <query>`: Perform a Google search.
- `youtube <query>`: Search for videos on YouTube.
- `sauce <image_url>`: Perform a reverse image search using SauceNAO.
- `pexels <query>`: Search for images on Pexels.
- `play <URL or query>`, `pause`, `resume`, `stop`, `next`: Music commands. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `download <URL>`: Downloads and returns video to chat. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `cat`: random cat gif.
- `dog`: random dog gif.
- `sherlock <username>`: returns all sites where the user has created an account. Uses [Sherlock-project](https://github.com/sherlock-project/sherlock)
- `expose <username>`: returns all sites where the user has created an account. Uses modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python)
- `/join`: Joins any specified voice channel, even without joining it yourself
- `/speak`: Says anything in voice channel you want using Microsoft's text to speech. Uses [edge-tts](https://pypi.org/project/edge-tts/)
### Note: The bot has a message history feature, it will remember the last 10 comments per user, you can change this number on line 74


