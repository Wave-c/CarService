from aiogram import Bot, Dispatcher
import hendlers.main_handler as main_handler
import asyncio

API_TOKEN = '7757737885:AAHFrd0lywZyauPbK0_RZkOLVrlv6Txe0xs'

async def init_bot():
    bot = Bot(token = API_TOKEN)
    dp = Dispatcher(bot)
    dp.include_routers(
        main_handler.router
    )
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(init_bot())