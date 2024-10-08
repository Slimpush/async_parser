import aiohttp
import logging
from bs4 import BeautifulSoup


async def fetch_page_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            logging.error(f"Ошибка при запросе {url}: {e}")
            raise


async def get_trade_link(url: str):
    html_content = await fetch_page_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    link = soup.find('a', class_='accordeon-inner__item-title link xls')
    if link:
        href = f'https://spimex.com{link.get("href")}'
        return href
    else:
        logging.error("Не удалось найти ссылку на странице")
        return None
