import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7574475855:AAHvO7iVsRXAnvWb-bP9kd1DvbOK_-NEy_o")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27808501"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9edcc32d1848771360efa9379868d352")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet161616:HNGaeiIDpbJatyEt@cluster0.fnyma4q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
