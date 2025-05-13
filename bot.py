
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '7758720459:AAE00kdon3Q82ompwTEHK6dBetSirCzyXvE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "✨ Вітаю, дорогі друзі! ✨\n\n"
        "Мене звати Анастасія, і я рада вітати вас на цьому захопливому інтенсиві з нумерології!\n\n"
        "Цифри – це не просто математичні символи, а ключі до розуміння себе, свого життєвого шляху та глибинних можливостей. "
        "Протягом цього курсу я допоможу вам:\n"
        "✅ Дізнатися, як числа впливають на характер і долю\n"
        "✅ Навчитися розраховувати свої основні нумерологічні коди\n"
        "✅ Використовувати знання чисел для прийняття правильних рішень\n\n"
        "Цей інтенсив — це ваш перший крок до розкриття внутрішнього потенціалу через мову чисел. "
        "Готові розпочати подорож? Тоді давайте заглибимося у світ нумерології разом!\n\n"
        "✨ Давайте творити магію чисел разом! ✨"
    )

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("💳 Купити курс", url="https://your-payment-link.com"))

    await message.answer(text, reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
