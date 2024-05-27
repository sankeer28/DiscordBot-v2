# DiscordBot-v2
Discord bot made using Python with many features including AI chat and music playback



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
     - Line 18: Gemini API key
     - Line 29 - 39: Google API keys, Google search engine id, Saucenao API, Pexels API
     - Line 326: Discord bot token
4. Rename the bot:
   - Line 47 & 56: change the bot's name from Drake/drake to your liking
     
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
- `play <URL>`, `pause`, `resume`, `stop`: Music commands.

## Demo


https://github.com/sankeer28/DiscordBot-v2/assets/112449287/272f8302-7d9a-481b-8da4-603143ba6a8f


