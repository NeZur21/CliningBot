from aiogram.fsm.state import State, StatesGroup


class OrderState(StatesGroup):
    service = State()
    area = State()
    additional_services = State()
    address = State()
    date = State()
    time = State()
    phone = State()
    confirmation = State()