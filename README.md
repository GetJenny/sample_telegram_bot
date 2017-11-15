# sample_telegram_bot

This is a quick and dirty telegram sample bot in python, it just an example and the code is quite dirty.
The program uses an in memory datastore for sessions data, of course would be better to use a database.

# python requirements

* python3
* docker

# Setup

## install starchat on localhost

Follow instructions on [https://getjenny.github.io/starchat-doc/](https://getjenny.github.io/starchat-doc/)

Create a new index:
```bash
curl -v -H "Content-Type: application/json" -X POST "http://localhost:8888/index_management/create"
```

## make a Python3 virtual environment (optional)

```
virtualenv -p python3  env3_telegram
source env3_telegram/bin/activate
```

## install python packages telegram and urllib3

```bash
pip install python-telegram-bot --upgrade
pip install urllib3
```

## index a decision table

curl -v --form "csv=@<FILE_PATH>" http://localhost:8888/decisiontable_upload_csv

e.g.

```bash
curl -v --form "csv=@starchat_configuration_sample.csv" http://localhost:8888/decisiontable_upload_csv
```

Apply the modifications:

```bash
curl -v -H "Content-Type: application/json" -X POST "http://localhost:${PORT}/decisiontable_analyzer"
```

# Create a new bot (need a telegram account)

* go on [https://web.telegram.org/#/im?p=@BotFather]
* type the command "/newbot" to create a new bot, follow the instructions
* collect the unique token access which is something like this:
```Use this token to access the HTTP API: XXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYYYYY`````
* edit the file telegram_starchat.py and replace the token access into the main function


