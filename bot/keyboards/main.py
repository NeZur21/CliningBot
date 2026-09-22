from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🧹 Заказать уборку",
                    callback_data="order_cleaning"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💰 Узнать стоимость",
                    callback_data="calculate_price"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⭐ Отзывы клиентов",
                    callback_data="reviews"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋 Мои заказы",
                    callback_data="my_orders"
                )
            ],
            [
                InlineKeyboardButton(
                    text="☎️ Связаться с менеджером",
                    callback_data="manager"
                )
            ],
        ]
    )


def service_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🏠 Уборка квартиры",
                    callback_data="service_apartment"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏢 Уборка офиса",
                    callback_data="service_office"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Генеральная уборка",
                    callback_data="service_general"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🪟 Мытьё окон",
                    callback_data="service_windows"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛋 Химчистка мебели",
                    callback_data="service_furniture"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="back_main"
                )
            ],
        ]
    )

def main_reply_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🧹 Заказать уборку"),
                KeyboardButton(text="💰 Узнать стоимость"),
            ],
            [
                KeyboardButton(text="📋 Мои заказы"),
                KeyboardButton(text="☎️ Менеджер"),
            ],
            [
                KeyboardButton(
                    text="⭐ Отзывы клиентов",
                )
            ]
        ],
        resize_keyboard=True,
        is_persistent=True
    )

def reviews_keyboard(index: int, total: int):
    buttons = []

    if index < total - 1:
        buttons.append(
            InlineKeyboardButton(
                text="Ещё ➡️",
                callback_data=f"review_next:{index + 1}"
            )
        )
    else:
        buttons.append(
            InlineKeyboardButton(
                text="🔄 Сначала",
                callback_data="review_next:0"
            )
        )
    return InlineKeyboardMarkup(
        inline_keyboard=[buttons]
    )