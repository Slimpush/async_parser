import asyncio
import aiohttp
import time
from datetime import datetime
from parsers.html_parser import get_trade_link
from parsers.excel_parser import parse_xls_data
from db_manager import create_tables, insert_data


async def fetch_content(link: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status == 200:
                return await response.read()
            else:
                raise Exception(f"Не удалось загрузить данные по ссылке: {link}, статус: {response.status}")


async def handle_link(link: str, date: str) -> None:
    try:
        xls_content = await fetch_content(link)
        data = await parse_xls_data(xls_content, date)
        if data:
            await insert_data(data)
        else:
            print(f"Нет данных для вставки по ссылке: {link}")
    except Exception as e:
        print(f"Ошибка при обработке ссылки {link}: {e}")


async def process_data() -> None:
    try:
        starttime = time.time()
        url = 'https://spimex.com/markets/oil_products/trades/results/?page=page-1'
        link = await get_trade_link(url)

        if link:
            await create_tables()
            date = datetime.now().strftime("%d.%m.%Y")
            await handle_link(link, date)
        else:
            print("Не удалось получить последнюю ссылку.")
        endtime = time.time()
        time_count = endtime - starttime
        minutes, seconds = divmod(time_count, 60)
        print(f"Время выполнения process_data: {int(minutes)} минут и {seconds:.2f} секунд")

    except Exception as e:
        print(f"Произошла ошибка при обработке данных: {e}")


def main() -> None:
    try:
        asyncio.run(process_data())
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
