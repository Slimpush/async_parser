from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_current_time():
    return datetime.now()


class SPIMEXTradingResults(Base):
    """
    Модель базы данных для хранения результатов торгов на SPIMEX.
    Атрибуты:
        id (int): Уникальный идентификатор записи.
        exchange_product_id (str): Код продукта.
        exchange_product_name (str): Наименование продукта.
        delivery_basis_name (str): Название базиса поставки.
        volume (float): Объём контрактов.
        total (float): Общая сумма.
        count (int): Количество контрактов.
        oil_id (str): Идентификатор нефти.
        delivery_basis_id (str): Идентификатор базиса поставки.
        delivery_type_id (str): Идентификатор типа поставки.
        date (Date): Дата торгов.
        created_on (datetime): Время создания записи.
        updated_on (datetime): Время последнего обновления записи.
    """

    __tablename__ = "spimex_trading_results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange_product_id = Column(String, nullable=False)
    exchange_product_name = Column(String)
    delivery_basis_name = Column(String)
    volume = Column(Float)
    total = Column(Float)
    count = Column(Integer)
    oil_id = Column(String)
    delivery_basis_id = Column(String)
    delivery_type_id = Column(String)
    date = Column(Date)
    created_on = Column(DateTime, default=get_current_time)
    updated_on = Column(
        DateTime, default=get_current_time,
        onupdate=get_current_time
    )
