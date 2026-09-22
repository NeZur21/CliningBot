from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from bot.keyboards.main import main_menu, service_menu, reviews_keyboard
import json
from pathlib import Path
from aiogram.types import FSInputFile

router = Router()


@router.callback_query(F.data == "order_cleaning")
async def order_cleaning(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите услугу:",
        reply_markup=service_menu()
    )

    await callback.answer()


@router.callback_query(F.data.startswith("service_"))
async def select_service(callback: CallbackQuery):
    services = {
        "service_apartment": "🏠 Уборка квартиры",
        "service_office": "🏢 Уборка офиса",
        "service_general": "✨ Генеральная уборка",
        "service_windows": "🪟 Мытьё окон",
        "service_furniture": "🛋 Химчистка мебели",
    }

    service = services.get(callback.data)

    await callback.message.answer(
        f"Вы выбрали:\n\n"
        f"{service}\n\n"
        "Здесь следующим шагом можно запросить "
        "площадь помещения и рассчитать стоимость."
    )

    await callback.answer()


@router.message(F.text == "🧹 Заказать уборку")
async def order_cleaning_message(message: Message):
    await message.answer(
        "Выберите услугу:",
        reply_markup=service_menu()
    )


@router.message(F.text == "💰 Узнать стоимость")
async def calculate_price_message(message: Message):
    await message.answer(
        "💰 Расчёт стоимости\n\n"
        "Выберите услугу:",
        reply_markup=service_menu()
    )


@router.message(F.text == "📋 Мои заказы")
async def my_orders_message(message: Message):
    await message.answer(
        "📋 У вас пока нет заказов.",
    )


@router.message(F.text == "☎️ Менеджер")
async def manager_message(message: Message):
    await message.answer(
        "☎️ Связаться с менеджером\n\n"
        "Напишите ваш вопрос следующим сообщением."
    )

@router.message(F.text == "⭐ Отзывы клиентов")
async def reviews_message(message: Message):
    await show_review(message, 0)

@router.callback_query(F.data == "reviews")
async def reviews_callback(callback: CallbackQuery):
    await show_review(callback.message, 0)
    await callback.answer()

@router.callback_query(F.data.startswith("review_next:"))
async def next_review(callback: CallbackQuery):
    index = int(callback.data.split(":")[1])

    await show_review(callback.message, index)

    await callback.answer()

def load_reviews():
    with open("data/reviews.json", "r", encoding="utf-8") as file:
        return json.load(file)

REVIEWS_DIR = Path("data/reviews")

async def show_review(message, index: int):
    reviews = load_reviews()

    if not reviews:
        await message.answer(
            "⭐ Пока нет отзывов."
        )
        return

    index = index % len(reviews)

    review = reviews[index]

    photo_path = REVIEWS_DIR / review["photo"]

    text = (
        f"⭐⭐⭐⭐⭐"
        f"Отзыв {index + 1} из {len(reviews)}\n\n"
        f"{review['text']}\n\n"
        f"— {review['author']}"
    )

    await message.answer_photo(
        photo=FSInputFile(photo_path),
        caption=text,
        reply_markup=reviews_keyboard(index, len(reviews)))
