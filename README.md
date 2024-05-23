# InclusiBrief

<p align="center">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/logo.png" alt="Logo" width="200" height="200">
</p>

This is a discord bot developed for GDSC genai workshop. This bot is continued conversation bot made for plan trip, get information about places, etc. The bot is made using discord.py and genai API. The history and new chat can be configured by the commands provided by the bot. The bot is deployed on render and cron-jobs is used to monitor the uptime.

## Folder Structure:

```bash
.
├── assets
│   └── logo.png
│   └── permissions.png
│   └── demo (Demo Images)
│      ├── 1.png till 7.png
│── .env
│    ├── TOKEN=Your Discord Bot Token
│    ├── GEMINI_API_KEY=Your Gemini API Key
├── .gitignore
├── main.py
├── app.py
├── bot.py
├── monitor_and_restart.py
├── build.sh
├── Procfile
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation and Running:

1. Clone the repository using the following command:

```bash
git clone https://github.com/scienmanas/JourneyGenie.git
```

2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

3. Either you can run locally or deploy it in a virtual private server, or you can configure an Arduino zero to do it, since the bot is not heavy.

4. Create a `.env` file in the root directory and add the following variables:

```bash
TOKEN=YOUT_DISCORD_BOT_TOKEN
GEMINI_API_KEY=Your Gemini API Key
```

5. In Testing/debugging phase :

```bash
python monitor_and_restart.py
```

## Deployment:

1. You can deploy the bot in a virtual private server or in a cloud platform like Heroku, AWS, etc.
2. This bot is deployed on render and cron-jobs is used to monitor the uptime.
3. To deployt in render:
   - `build command`:
     - ```bash
       ./build.sh
       ```
   - `run command`:
     - ```bash
       python main.py
       ```

## Features:

- This is a genai chat bot, which can be used as a travel guide or a travel planner.

## Contributors:

1. [Manas](https://github.com/scienmanas)

## API Used:

1. [Gemini API](https://docs.gemini.com/)

## Note:

- The bot is not optimized and configures, so we advise you to create your own bot and configure it according to your needs by utilizing the code. use **`&help`** to get bot commands.

- Enable the intents so that it can read message events.

![Permissions](https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/permissions.png)

## Contributing:

The repository is open for contribution. All types of contribution are acknowledged - raising a bug issue, recommending new features as well as updating the code base. Before updating the code base raise an issue of recoomendign new feature and then can raise a pull requesting with the mentioned issue id.

## License:

This project is licensed under the MIT License

## Demo :

<div>
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/1.png" alt="Demo 1">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/2.png" alt="Demo 2">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/3.png" alt="Demo 3">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/4.png" alt="Demo 4">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/5.png" alt="Demo 5">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/6.png" alt="Demo 6">
  <img src="https://raw.githubusercontent.com/scienmanas/JourneyGenie/main/assets/demo/7.png" alt="Demo 7">
</div>
