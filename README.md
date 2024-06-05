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

- Python 3.12 🐍** 3.10 if you want the OSINT tool [Maigret](https://github.com/sankeer28/DiscordBot-v2/tree/main?tab=readme-ov-file#to-use-the-command-maigret-)
- FFMPEG installed onto system PATH
- pip

# Features
### Chat Interaction 💬:
- Casual chat with the bot using its name.
- Immediate responses using Gemini AI.
- Chat history temporarily saved to memory for more realistic conversations.

### Media Retrieval 📺:
- Returns images from [Google](https://www.google.com).
- Searches [YouTube](https://www.youtube.com) for videos.
- Returns images from [Pexels](https://www.pexels.com).
- Downloads URLs from various sources including [SoundCloud](https://soundcloud.com), [YouTube](https://www.youtube.com), [TikTok](https://www.tiktok.com), [Twitter](https://twitter.com), [Instagram](https://www.instagram.com), and [more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).


### Image Related 🖼️:
- Finds the source of images through reverse image search supporting various formats using [SauceNao](https://saucenao.com/).
- Asks questions regarding uploaded images using [Gemini AI](https://gemini.google.com/).

### OSINT Tools 🔓:
- Integrates with [Sherlock](https://github.com/sherlock-project/sherlock)
- Integrates with modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python)
- Integrates with [socialscan](https://github.com/iojw/socialscan).
-  Integrates with [Maigret](https://github.com/soxoj/maigret) - **Not compatible with modern Python versions, must enable** [manually](https://github.com/sankeer28/DiscordBot-v2/tree/main?tab=readme-ov-file#to-use-the-command-maigret-)
- Logs servers the bot is in upon startup, including user's Discord IDs, server nickname, Discord username, and status/bio, into a folder called Servers as .json files.

### Voice Chat 🎙️:
- Joins any voice channel in the server without the need for manual intervention.
- Utilizes text-to-speech in voice chat, allowing the bot to vocalize text input.
- Plays audio from the various [sources](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) in voice chat using the ```play``` command.

### Video Manipulation 📹:
- Generates [nightcore](https://en.wikipedia.org/wiki/Nightcore) videos or slowed-down videos using the [Spedup-Slowed-MV](https://github.com/sankeer28/Spedup-Slowed-MV) project.


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
- `drake <prompt>`: Generate content using the Generative AI model. **Name of bot is customizable**.
- `image <query>`: Search for images using Google Custom Search.
- `google <query>`: Perform a Google search.
- `youtube <query>`: Search for videos on YouTube.
- `sauce <image_url>`: Perform a reverse image search using SauceNAO.
- `pexels <query>`: Search for images on Pexels.
- `play <URL or query>`, `pause`, `resume`, `stop` : Music commands. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `download <URL>`: Downloads and returns video to chat. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `cat`: random cat gif.
- `dog`: random dog gif.
- `sherlock <username>`: returns all sites where the user has created an account. Uses [Sherlock-project](https://github.com/sherlock-project/sherlock)
- `expose <username>`: returns all sites where the user has created an account. Uses modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python)
- `socialscan <username or email>`: accurately querying username and email usage on online platforms. Uses [socialscan](https://github.com/iojw/socialscan) 
- `/join`: Joins any specified voice channel, even without joining it yourself
- `/speak`: Says anything in voice channel you want using Microsoft's text to speech. Uses [edge-tts](https://pypi.org/project/edge-tts/)
- `/nightcore`: creates nightcore video or slowed down video given URL. Uses my personal [project](https://github.com/sankeer28/Spedup-Slowed-MV)
  
### Note: The bot has a message history feature, it will remember the last 10 comments per user, you can change this number on line 82
### To use the command maigret <username>
- You are required to use Python 3.10 and must manually install maigret by ``` pip install maigret ```
- Has not been added to !help as it is limited to a specific version of python
- This feature uses [maigret](https://github.com/soxoj/maigret) takes in a username and returns a pdf report

