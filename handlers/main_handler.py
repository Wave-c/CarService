from aiogram import Router, F, types

router = Router()

@router.message(F.text.lower() == "/start")
async def start_message_handler(message : types.Message):
    await message.answer("Hello world")