import requests
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
import logging
from markup import markaMenu
TOKEN = 'TOKEN'
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   await message.reply("Dollor kursini aniqlash botiga Xush kelibsiz!", reply_markup=markaMenu)
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
   if message.chat.type=="private":
       await bot.send_message(message.from_user.id, reply_markup=markaMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Kursni aniqlash':
        await message.reply(f"Bugungi 1 AQSH dollor {kurs} so`mga teng!\n"
                            f"{javob}")
    else:
        await message.reply("Valyuta kusini bilish uchun Kursni aniqlash tugmasini bosing")
url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/UZS"
# Making our request
response = requests.get(url)
data = response.json()
kurs = response.json()[0]['Rate']
javob = f"Botdan foydalanganingiz uchun tashakkur! Botdagi valyuta kursi O`zbekiston Respublikasi Markaziy Banki valyuta kursiga asosan."

bugun =  datetime.now().strftime('%d-%m-%Y  %H:%m')


if __name__ == '__main__':
   
    executor.start_polling(dp, skip_updates=True)
