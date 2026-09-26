from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import database as db
from utils.lang import t
from keyboards.main_kb import main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = message.from_user
    
    # Foydalanuvchini bazaga saqlash
    await db.create_user(user.id, user.username or "", user.first_name or "", "uz")
    
    bot_info = await message.bot.get_me()
    
    # Matn va menyuni chaqirish
    text = t("uz", "welcome")
    markup = main_menu("uz", bot_info.username)
    
    await message.answer(text, reply_markup=markup)

@router.callback_query(F.data == "start")
async def cb_start(call: CallbackQuery, state: FSMContext):
    await state.clear()
    
    bot_info = await call.bot.get_me()
    text = t("uz", "welcome")
    markup = main_menu("uz", bot_info.username)
    
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except Exception:
        await call.message.answer(text, reply_markup=markup)
