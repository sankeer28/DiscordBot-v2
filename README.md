# DiscordBot-v2
Discord bot made using Python with many features including AI chat, music playback, video downloader, and more.

## Getting Started

### Prerequisites

- Python 3.12
- FFMPEG installed onto system PATH

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
     - Line 25-38: Gemini API key, Google API keys, Google search engine id, Saucenao API, Pexels API
     - Last Line: Discord bot token
4. Rename the bot:
   - Line 53 & 62: change the bot's name from Drake/drake to your liking
     
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
- `play <URL>`, `pause`, `resume`, `stop`: Music commands. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `download <URL>`: Downloads and returns video to chat. Supports URLs from these [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- `cat`: random cat gif.
- `dog`: random dog gif.
## Note: Maximum character output for Gemini AI chat is 2000 characters, to prevent errors, output message will be cut short after 2000 characters


