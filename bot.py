
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, ConversationHandler, MessageHandler, filters

app = ApplicationBuilder().token('7685501588:AAG3orJSNE3kpm2z5R3_CSqa6cnjtOlbGgg').build()


async def button_handler(update, context):
        query = update.callback_query
        await query.answer()

        if query.data == "reservation":
            await query.message.reply_text(
                "Чтобы забронировать тур, пожалуйста, отправьте следующую информацию:\n"
                "- Дата желательного отправления\n"
                "- Дата возвращения\n"
                "- Количество людей, сколько отправляеться с вами. (если отправляетесь одни, напишите 1)"
            )
        elif query.data == "country":
            await query.message.reply_text(
                "Выберите страну, в которую желаете отправиться, в нужную вам дату: (не забывайте, этот список часто пополняеться)\n"
                "- 🇦🇺Australia\n"
                "- 🇦🇹Austrian\n"
                "- 🇧🇷Brazil\n"
                "- 🇨🇴Colombia\n"
                "- 🇫🇮Finland\n"
                "- 🇫🇷France\n"
                "- 🇩🇪Germany\n"
                "- 🇮🇪Ireland\n"
                "- 🇮🇱Israel\n"
                "- 🇮🇹Italy\n"
                "- 🇯🇵Japan\n"
                "- 🇵🇭Philippines\n"
                "- 🇹🇭Thailand"
            )
        elif query.data == "trip":
            await query.message.reply_text(
                "Вот туры готовые к отправлению:"
                "- Тур в Колумбию в Медельин. Отправка 30.11.2024\n"
                "- Тур в Финляндию, в Хельсинки. Отправка 3.12.2024\n"
                "- Тур в Филиппины, в Манилы. Отправка 20.12.2024\n"
                "- Тур в Израиль, в Нетания. Отправка 24.12.2024\n"
                "- Тур в Японию, в Токио. Отправка 5.12.2024\n"
                "- Тур в Таиланд, В Бангкок. Отправка 15.12.2024"

            )
        elif query.data == "contacts":
            await query.message.reply_text(
                "Наши данные:"
                "-+123456789\n"
                "-+987654321"
            )

async def start_command(update, context):
            inline_keyboard = [
                [InlineKeyboardButton("Забронировать тур", callback_data="reservation")],
                [InlineKeyboardButton("Страны", callback_data="country")],
                [InlineKeyboardButton("Туры", callback_data="trip")],
                [InlineKeyboardButton("Контакты", callback_data="contacts")]
            ]
            markup = InlineKeyboardMarkup(inline_keyboard)

            await update.message.reply_text(
                "Приветствуем в туристическом агенсте 'кавун'! Выберите действие:",
                reply_markup=markup
            )
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CallbackQueryHandler(button_handler))

if __name__ == '__main__':
    app.run_polling()
