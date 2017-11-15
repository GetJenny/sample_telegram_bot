# Telegram bot based on StarCgat

This is a quick and dirty telegram sample bot in python based on [StarChat.ai](http://starchat.ai). The program uses an in memory datastore for sessions data. If you want to contribute with a proper database, eg SQLite, you are wellcome!

# Fork this repository (optional)

* Fork the repository on your account. You could clone this rep directly, but then you won't be able to push your changes on github. Click on top left button "Fork" :)
* Clone: `git clone git@github.com:MY_ACCOUNT/starchat_telegram_bot.git`
* Set this repository as "upstream", so you can rebase your repository everytime we make a change: `git remote add upstream  git@github.com:GetJenny/starchat_telegram_bot.git`

In the future, when you want to update your repository with GetJenny's one, just type: 

```bash
git fetch upstream
git rebase upstream/master
```

# Requirements

* python3
* docker

# Setup

## Install starchat on localhost

Start the service following the instructions on [StarChat Documentation](https://getjenny.github.io/starchat-doc/#setup-with-docker-recommended) (5-10 minutes)

Create a new index. On a terminal (Unix) type:

```bash
curl -v -H "Content-Type: application/json" -X POST "http://localhost:8888/index_management/create"
```

## Make a Python3 virtual environment (optional)

Optional, but recommended!

```
virtualenv -p python3  env3_telegram
source env3_telegram/bin/activate
```

## Install telegram and urllib3 packages

```bash
pip install python-telegram-bot --upgrade
pip install urllib3
```

## Configure

Load a configuration file into StarChat and apply the changes:


```bash
curl -v --form "csv=@starchat_configuration_sample.csv" http://localhost:8888/decisiontable_upload_csv
# Apply:
curl -v -H "Content-Type: application/json" -X POST "http://localhost:8888/decisiontable_analyzer"
```

# Create a new Telegram bot

You need a telegram account of course!

* Go on [https://web.telegram.org/#/im?p=@BotFather]
* Type the command "/newbot" to create a new bot, follow the instructions
* Collect the unique token access which is something like this:

```
Use this token to access the HTTP API: XXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYYYYY
````

* Edit the file telegram_starchat.py and replace the token access into the main function


