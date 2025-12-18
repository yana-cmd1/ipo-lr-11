# Дмитрук Яны

import requests  # импортируем библиотеку для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # импортируем для парсинга HTML-страниц
import json  # импортируем для сохранения данных в файл
from urllib.parse import urljoin  # импортируем для правильного объединения URL-адресов

def get_quotes_from_page(url):  # для сбора цитат с страницы, принимает URL
    all_quotes = []   
    quote_number = 1   

    while url:  
        headers = {  # определяем заголовки длч HTTP-запроса
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3"  # имитация браузера
        }
        response = requests.get(url, headers=headers)  # отправляем GET-запрос по текущему URL с заголовками
        if response.status_code != 200:   
            print("Ошибка загрузки страницы")  
            break   
        soup = BeautifulSoup(response.text, 'html.parser')  # создаем объект для парсинга HTML
        quote_blocks = soup.find_all("div", class_="quote")   

        for block in quote_blocks:   
            text = block.find("span", class_="text").get_text(strip=True)  
            all_quotes.append({"number": quote_number, "quote": text})  
            print (f'{quote_number}. {text}')  
            quote_number += 1  

        next_btn = soup.find('li', class_='next')  # ищем кнопку "следующая" страница
        if next_btn and next_btn.a:   
            url = urljoin(url, next_btn.a['href'])  # обновляем ссылкк на следующую страницу
        else:   
            url = None  

    return all_quotes  # возвращает список собранных цитат

if __name__ == '__main__': 
    start_url = 'https://quotes.toscrape.com/'  # начальный URL для парсинга
    quotes = get_quotes_from_page(start_url)  # функция сбора цитат
