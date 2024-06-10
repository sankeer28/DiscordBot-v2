

<p align="center">
  <img src="https://github.com/sankeer28/DiscordBot-v2/assets/112449287/131c6205-9301-4d15-b67a-96c3aa9e87dc" width="300" />
</p>

Discord bot made using Python with many features including AI chat, music playback, video downloader, OSINT tools, and more.

## Getting Started

### Prerequisites

- Python 3.12+ 🐍** 3.10 if you want the OSINT tool [Maigret](https://github.com/sankeer28/DiscordBot-v2/tree/main?tab=readme-ov-file#to-use-the-command-maigret-)
- [FFMPEG](https://ffmpeg.org/): installed onto system PATH
  - Linux (apt): 
  ```sudo apt install ffmpeg```
  - MacOS (via homebrew): 
      ```brew install ffmpeg```
  - Windows: [guide](https://www.hostinger.com/tutorials/how-to-install-ffmpeg#:~:text=successfully%20installed%20FFmpeg.-,how%20to%20install%20ffmpeg%20on%20windows,-Before%20the%20installation): 
- pip

## Features
### Chat Interaction 💬:
- Casual chat with the bot using its name. Not required to call its name if using the bot's DMs.
- Immediate responses using Gemini AI.
- Conversation is temporarily saved to memory for realism.
- 50/50 chance to get a GIF from Giphy based on the context of what is being said in chat using NLP.
  - [SpaCy](https://spacy.io/) NLP identifies the most relevant parts of a message by focusing on nouns, proper nouns, adjectives, and verbs, excluding personal pronouns which might not contribute much to the context.

### Media Retrieval 📺:
- Returns images from [Google](https://www.google.com).
- Searches [YouTube](https://www.youtube.com) for videos.
- Returns images from [Pexels](https://www.pexels.com).
- Downloads from various sources including [SoundCloud](https://soundcloud.com), [YouTube](https://www.youtube.com), [TikTok](https://www.tiktok.com), [Twitter](https://twitter.com), [Instagram](https://www.instagram.com), and [more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md). **Video length must be under 30 mins, as Discord limits large file sizes.**

### Image Related 🖼️:
- Finds the source of images through reverse image search supporting various formats using [SauceNao](https://saucenao.com/).
- Asks questions regarding uploaded images using [Gemini AI](https://gemini.google.com/).

### OSINT Tools 🔓:
- Integrates with [Sherlock](https://github.com/sherlock-project/sherlock)
- Integrates with modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python). Returns either links to chat or creates html file with --html argument.
- Integrates with [socialscan](https://github.com/iojw/socialscan).
- Integrates with [Maigret](https://github.com/soxoj/maigret) - **Not compatible with modern Python versions, must enable** [manually](https://github.com/sankeer28/DiscordBot-v2/tree/main?tab=readme-ov-file#to-use-the-command-maigret-)
- Logs info of members in servers, including the user's Discord IDs, server nickname, Discord username, and status/bio, into a folder called Servers as .json files.

### Voice Chat 🎙️:
- Auto joins any voice channel in the server
- Auto leaves after everyone leaves
<details>
  <summary>Utilizes text-to-speech in voice chat, allowing the bot to vocalize text input</summary>

https://github.com/sankeer28/DiscordBot-v2/assets/112449287/32db7e02-0132-462f-9786-edba88e0509b

 </details>

- Plays audio from the various [sources](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) in voice chat using the ```play``` command.
    - Ability to infinitely loop any audio source played in voice channel 🔁.

### Video Manipulation 📹:
- Generates [nightcore](https://en.wikipedia.org/wiki/Nightcore) videos or slowed-down videos using my project [Spedup-Slowed-MV](https://github.com/sankeer28/Spedup-Slowed-MV).
  
### Leveling System 📈:
- Users gain xp by sending messages.
- Users receive a notification in the current chat when they level up.
- Commands available:
  - `level`: Check your current level and experience points.
  - `leaderboard`: View the top 10 users by level.
- All user levels and experience points are saved locally to a .json file to ensure persistence even after bot restarts.
  
## Running locally


### Getting API Keys

- **Google Custom Search Engine API Key**: Obtain from the Google Cloud Console. [Guide](https://developers.google.com/custom-search/v1/overview)
- **Google API Keys**: Necessary for YouTube and Google Search. Obtain from the Google Cloud Console. [Guide](https://cloud.google.com/docs/authentication/api-keys)
- **Saucenao API Key**: Get from the SauceNAO website. [Guide](https://saucenao.com/user.php?page=search-api)
- **Pexels API Key**: Get from the Pexels website. [Guide](https://www.pexels.com/api/documentation/)
- **Google Gemini AI API KEY:** Get from Google AI Studio. [Here](https://aistudio.google.com/app/apikey)
- **Giphy API KEY:** Get from Giphy [website](https://developers.giphy.com/dashboard/)

### Running the Bot

1. Clone this repository:

```bash
git clone https://github.com/sankeer28/DiscordBot-v2.git
```

2. Navigate to the bot directory:

```bash
cd DiscordBot-v2
```

### Installing Dependencies

```bash
pip install -r requirements.txt
```
Install NLP model
```bash
python -m spacy download en_core_web_sm
```

3. Fill in the API Keys on missing lines.
     - Line 26: Gemini API key, Google API keys, Google search engine id, Saucenao API, Pexels API, Gify API
     - Last Line: Discord bot token
4. Rename the bot:
   - Line 83: change the bot's name from drake to your liking
     
5. Run the bot:

```bash
python bot.py
```
## Usage: type !help for all commands. There is **NO** prefix for all commands.
| Command                               | Description                                                                                                    |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `drake <prompt>`                      | Generate content using the Generative AI model. **Name of bot is customizable**.                                |
| `image <query>`                       | Search for images using Google Custom Search.                                                                  |
| `google <query>`                      | Perform a Google search.                                                                                       |
| `youtube <query>`                     | Search for videos on YouTube.                                                                                  |
| `sauce <image_url>`                   | Perform a reverse image search using SauceNAO.                                                                 |
| `pexels <query>`                      | Search for images on Pexels.                                                                                   |
| `play <URL or query>`, `pause`, `resume`, `stop` | Music commands. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) |
| `download <URL>`                      | Downloads and returns video to chat. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) |
| `cat`                                 | Random cat gif.                                                                                                |
| `dog`                                 | Random dog gif.                                                                                                |
| `sherlock <username>`                 | Returns all sites where the user has created an account. Uses [Sherlock-project](https://github.com/sherlock-project/sherlock) |
| `expose <username> --html`            | Returns all sites where the user has created an account. Uses modified [WhatsMyName](https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python) |
| `socialscan <username or email>`      | Accurately querying username and email usage on online platforms. Uses [socialscan](https://github.com/iojw/socialscan) |
| `/join`                               | Joins any specified voice channel, even without joining it yourself                                             |
| `/speak`                              | Says anything in voice channel you want using Microsoft's text to speech. Uses [edge-tts](https://pypi.org/project/edge-tts/) |
| `/nightcore`                          | Creates nightcore video or slowed down video given URL. Uses my personal [project](https://github.com/sankeer28/Spedup-Slowed-MV) |
| `level`                          | View your level |
| `leaderboard`                         | View top 10 users by xp |

## To use the command maigret <username>
- You are required to use Python 3.10 and must manually install maigret by ``` pip install maigret ```
- Has not been added to !help as it is limited to a specific version of python
- This feature uses [maigret](https://github.com/soxoj/maigret) takes in a username and returns a pdf report

