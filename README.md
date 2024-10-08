# SPIMEX Trading Results Parser

Этот проект представляет собой парсер бюллетеней торгов с сайта [SPIMEX](https://spimex.com/markets/oil_products/trades/results/),
который автоматически извлекает и сохраняет последние данные о результатах торгов.

## Описание задачи

Парсер выполняет следующие действия:

1. Загружает торговые бюллетени с сайта биржи SPIMEX.
2. Извлекает данные из таблицы с единицей измерения "Метрическая тонна".
3. Фильтрует строки, где в столбце **«Количество Договоров, шт.»** значение больше 0.
4. Извлекает и сохраняет следующие столбцы:
    - Код Инструмента (**exchange_product_id**)
    - Наименование Инструмента (**exchange_product_name**)
    - Базис поставки (**delivery_basis_name**)
    - Объем Договоров в единицах измерения (**volume**)
    - Объем Договоров в рублях (**total**)
    - Количество Договоров (**count**)
5. Сохраняет полученные данные в таблицу базы данных `spimex_trading_results` со следующей структурой:
    - `id`: уникальный идентификатор записи
    - `exchange_product_id`: код инструмента
    - `exchange_product_name`: наименование инструмента
    - `oil_id`: первые 4 символа из `exchange_product_id`
    - `delivery_basis_id`: символы с 4 по 7 из `exchange_product_id`
    - `delivery_basis_name`: базис поставки
    - `delivery_type_id`: последний символ из `exchange_product_id`
    - `volume`: объем договоров в единицах измерения
    - `total`: объем договоров в рублях
    - `count`: количество договоров
    - `date`: дата торгов
    - `created_on`: дата создания записи
    - `updated_on`: дата обновления записи



# Общее время выполнения: 0 минут и 49.60 секунд
