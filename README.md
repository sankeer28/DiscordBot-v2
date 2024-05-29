# DiscordBot-v2
Discord bot made using Python with many features including AI chat, music playback, video downloader, and more.

## Getting Started

### Prerequisites

- Python 3.12
- FFMPEG installed onto system PATH
- pip
## Features 
- Chat with the bot casually by calling its name.
- Returns images from Google.
- Search YouTube for videos.
- Finds the source of images by performing a reverse image search. Supports .png, .jpg, .jpeg, .gif, and .webp.
- Return images from Pexels.
- Download URLs from many different sources and return them to the chat including SoundCloud, Youtube, Tiktok, Twitter(X), Instagram and [more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).
- Ask questions regarding uploaded images.
- Chat History is temporarily saved to memory to have more realistic conversations.

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
   - Line 79: change the bot's name from drake to your liking
     
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
## Note: The bot has a message history feature, it will remember last 10 comments, you can change this number on line 74


