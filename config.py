import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet161616:HNGaeiIDpbJatyEt@cluster0.fnyma4q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
