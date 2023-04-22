from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


Token = "s"
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)

executor.start_polling(dp, skip_updates=True)
