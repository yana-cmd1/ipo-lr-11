import json
#Дмитрук Яны
#Вариант 4
import requests   
from bs4 import BeautifulSoup  
import json   
from urllib.parse import urljoin  

def get_quotes_from_page(url):   
    all_quotes = []   
    quote_number = 1   

    while url:   
        headers = {  # определяем заголовки для HTTP-запроса
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3"  # имитация браузера
        }
        response = requests.get(url, headers=headers)  # отправляем GET-запрос по текущему URL с заголовками
        if response.status_code != 200:  
            print("Ошибка загрузки страницы")   
            break  
        soup = BeautifulSoup(response.text, 'html.parser')   
        quote_blocks = soup.find_all("div", class_="quote")  # находим все блоки цитат на странице

        for block in quote_blocks:  # Проходим по каждому блоку цитаты
            text = block.find("span", class_="text").get_text(strip=True)   
            all_quotes.append({"number": quote_number, "quote": text})   
            quote_number += 1  # увеличиваем счетчик цитат

        next_btn = soup.find('li', class_='next')   
        if next_btn and next_btn.a:   
            url = urljoin(url, next_btn.a['href'])   
        else:   
            url = None  

    return all_quotes  # список собранных цитат

def save_quotes(quotes, filename="data.json"):  # объявляем функцию для сохранения цитат в файл
    with open(filename, 'w', encoding='utf-8') as f:  
        json.dump(quotes, f, ensure_ascii=False, indent=2)  # ззаписываем список цитат в JSON файл с отступами

if __name__ == '__main__':  
    start_url = 'https://quotes.toscrape.com/'  # начальный URL для парсинга
    quotes = get_quotes_from_page(start_url)  # вызываем функцию сбора цитат
    save_quotes(quotes, filename='data.json')  # сохраняем в файл
