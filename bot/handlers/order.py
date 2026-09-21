from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from bot.keyboards.main import main_menu, service_menu


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


@router.message(F.text == "🏠 Главное меню")
async def main_menu_message(message: Message):
    await message.answer(
        "🏠 Главное меню:",
        reply_markup=main_menu()
    )


@router.callback_query(F.data == "reviews")
async def reviews_callback(callback: CallbackQuery):

    await callback.message.answer(
        "⭐ Отзывы наших клиентов\n\n"
        "«Очень довольны уборкой! Всё аккуратно и быстро.»\n"
        "— Анна, Москва\n\n"
        "«Заказывали генеральную уборку после ремонта. "
        "Результат отличный!»\n"
        "— Михаил, Москва\n\n"
        "«Приехали вовремя, всё сделали качественно. "
        "Будем обращаться ещё.»\n"
        "— Екатерина, Москва",
        reply_markup=main_menu()
    )

    await callback.answer()

@router.message(F.text == "⭐ Отзывы клиентов")
async def reviews_message(message: Message):

    await message.answer(
        "⭐ Отзывы наших клиентов\n\n"
        "«Очень довольны уборкой! Всё аккуратно и быстро.»\n"
        "— Анна, Москва\n\n"
        "«Заказывали генеральную уборку после ремонта. "
        "Результат отличный!»\n"
        "— Михаил, Москва\n\n"
        "«Приехали вовремя, всё сделали качественно. "
        "Будем обращаться ещё.»\n"
        "— Екатерина, Москва",
        reply_markup=main_menu()
    )