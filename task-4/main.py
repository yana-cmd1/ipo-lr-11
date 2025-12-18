#Дмитрук Яны
#Вариант 4
import requests   
from bs4 import BeautifulSoup   
import json  
from urllib.parse import urljoin  

def get_quotes_from_page(url):  # объявляем функцию для сбора цитат с  страницы, принимает URL
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

        for block in quote_blocks:  
            text = block.find("span", class_="text").get_text(strip=True)   
            all_quotes.append({"number": quote_number, "quote": text})   
            quote_number += 1  

        next_btn = soup.find('li', class_='next')   
        if next_btn and next_btn.a:   
            url = urljoin(url, next_btn.a['href'])   
        else:   
            url = None   
    return all_quotes  # возвращаем список собранных цитат

def save_quotes(quotes, filename="data.json"):  
    with open(filename, 'w', encoding='utf-8') as f:   
        json.dump(quotes, f, ensure_ascii=False, indent=2)  # записываем список цитат в JSON файл с отступами
    print("Цитаты сохранены в файл")   

def generate_html_table(quotes, output_file='quotes.html'): # Объявляем функцию для создания файла с цитатами
    html = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Цитаты с сайта quotes.toscrape.com</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #f0f4f8, #d9e2ec);
      padding: 40px;
      margin: 0;
    }
    h1 {
      text-align: center;
      color: #2c3e50;
      margin-bottom: 30px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      background-color: #fff;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    th, td {
      padding: 15px;
      border: 1px solid #ccc;
      text-align: left;
    }
    th {
      background-color: #3498db;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    .source {
      margin-top: 30px;
      text-align: center;
      font-size: 1em;
    }
    .source a {
      color: #3498db;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <h1>Собранные цитаты</h1>
  <table>
    <tr>
      <th>№</th>
      <th>Цитата</th>
    </tr>
'''

    for quote in quotes:
        html += f'''
    <tr>
      <td>{quote["number"]}</td>
      <td>{quote["quote"]}</td>
    </tr>
'''

    html += '''
  </table>
  <div class="source">
    Источник: <a href="https://quotes.toscrape.com/" target="_blank">quotes.toscrape.com</a>
  </div>
</body>
</html>'''

    with open(output_file, 'w', encoding='utf-8') as f: # Создаем файл для записи
        f.write(html)# Записываем данные 

if __name__ == '__main__':   
    start_url = 'https://quotes.toscrape.com/' 
    quotes = get_quotes_from_page(start_url)  
    save_quotes(quotes, filename='data.json')   
    generate_html_table(quotes, output_file='index.html')  # генерируем HTML-таблицу
