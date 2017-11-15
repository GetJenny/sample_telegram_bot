# sample_telegram_bot

This is a quick and dirty telegram sample bot in python. The program uses an in memory datastore for sessions data. If you want to contribute with a proper database, eg SQLite, you are wellcome!

# Requirements

* python3
* docker

# Setup

## Install starchat on localhost

Follow instructions on [https://getjenny.github.io/starchat-doc/](https://getjenny.github.io/starchat-doc/)

Create a new index:

```bash
curl -v -H "Content-Type: application/json" -X POST "http://localhost:8888/index_management/create"
```

## Make a Python3 virtual environment (optional)

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
curl -v -H "Content-Type: application/json" -X POST "http://localhost:${PORT}/decisiontable_analyzer"
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


