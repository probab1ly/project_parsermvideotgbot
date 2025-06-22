import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
import os
import csv
import asyncio
import time
import json
from aiogram import Bot
user_models_file = 'user_models.json'
products_finally = []
tracked_model = ['Apple']

site = 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=homepage&page='
def scroll_page(driver):
    print('Начинается прокрутка страницы')
    last_height = driver.execute_script("return document.body.scrollHeight")
    step = 800
    position = 0
    while position < last_height:
        position += step
        driver.execute_script(f"window.scrollTo(0, {position});")
        time.sleep(0.5)
        # try:
        #     show_more = driver.find_elements(By.CLASS_NAME, "mv-main-button--secondary")
        #     if show_more and show_more[0].is_displayed:
        #         actions = ActionChains(driver)
        #         actions.move_to_element(show_more[0]).click()
        #         time.sleep(2)
        #     else:
        #         print('Кнопка не найдена')
        #
        # except Exception as e:
        #     print(f'Ошибка: {e}')

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('Прокрутка завершена')

def parse():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    # options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'--user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    try:
        for i in range(1, 2):
            driver.get(f'{site}{i}')
            time.sleep(5)
            scroll_page(driver)
            products = driver.find_elements(By.CLASS_NAME, "product-cards-layout__item")
            print(f'Найдено товаров: {len(products)}')

            for index, product in enumerate(products, 1):
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", product)
                    time.sleep(0.5)
                    name = product.find_element(By.CLASS_NAME, "product-title__text").text.strip()
                    price1 = product.find_element(By.CLASS_NAME, "price__main-value").text.replace('₽', '').strip()
                    try:
                        price2 = product.find_element(By.CLASS_NAME, "price__sale-value").text.replace('₽', '').strip()
                        review = product.find_element(By.CLASS_NAME, "value").text.strip()
                        countreview = product.find_element(By.CLASS_NAME, "product-rating__feedback").text[:2].strip()
                    except:
                        price2, review, countreview = 0

                    products_finally.append({
                        'name': name,
                        'pricewithsell': price1,
                        'pricewithoutsell': price2,
                        'review': review,
                        'countreview': countreview
                    })
                    print(f'Добавлен товар: {name}')

                except Exception as e:
                    print(f'Обнаружена ошибка при сборе информации о товаре: {e}')
                    continue

    except TimeoutError:
        print('Превышено время ожидания')

    except Exception as e:
        print(f'Ошибка при парсинге: {e}')
    finally:
        driver.quit()

def save_to_excel(file='parser.xlsx'):
    try:
        df = pd.DataFrame(products_finally)
        writer = pd.ExcelWriter(file, engine='openpyxl')
        df.to_excel(writer, index=False, sheet_name='Parse')
        worksheet = writer.sheets['Parse']
        worksheet.column_dimensions['A'].width = 75
        worksheet.column_dimensions['B'].width = 20
        worksheet.column_dimensions['C'].width = 20
        print('Данные сохранены в EXCEL')
        writer.close()

    except Exception as e:
        print(f'Произошла ошибка: {e}')

def save_to_json_and_csv():
    with open('parser.json', 'w', encoding='utf-8') as file1:
        json.dump(products_finally, file1, indent=4, ensure_ascii=False)

    with open('parser.csv', 'w', newline='') as file2:
        csv_writer = csv.writer(file2)
        csv_writer.writerows(products_finally)
def filterdf(tracked_model):
    df = pd.DataFrame(products_finally)
    df = df[df['name'].str.contains('|'.join(tracked_model), case=False, na=False)]
    return df

async def main_checkpricesandnotify(tracked_model, bot):
    if os.path.exists('parser.csv') and os.path.getsize('parser.csv') > 0:
        try:
            old_df = pd.read_csv('parser.csv')
        except Exception as e:
            print(f'Произошла ошибка: {e}')
    else:
        old_df = pd.DataFrame(columns=['name', 'pricewithoutsell'])
    parse()
    save_to_json_and_csv()
    save_to_excel()
    users = await get_active_users()
    for user_id in users:
        user_models = get_models_for_user(user_id)
        if not user_models:
            continue
        df = filterdf(user_models)
        user_messages = set()
        for _, row in df.iterrows():
            name = row['name']
            try:
                price = int(str(row['pricewithoutsell']).replace(' ', ''))
            except:
                price = None
            old_price_row = old_df[old_df['name'] == name]
            if not old_price_row.empty:
                try:
                    old_price = int(str(old_price_row.iloc[0]['pricewithoutsell']).replace(' ', ''))
                except:
                    old_price = None
                if old_price is not None and price != old_price:
                    msg = f'💻 {name}\nЦена изменилась: {old_price}₽ → {price}₽'
                    user_messages.add(msg)
        if user_messages:
            for msg in user_messages:
                try:
                    await bot.send_message(chat_id=int(user_id), text=msg)
                except Exception as e:
                    print(f'Ошибка отправки сообщения {user_id}: {e}')
    all_models = set()
    for user_id in users:
        all_models.update(get_models_for_user(user_id))
    df_all = filterdf(list(all_models))
    df_all = df_all.drop_duplicates(subset=['name', 'pricewithoutsell'])
    df_all[['name', 'pricewithoutsell']].to_csv('parser.csv', index=False)

async def periodcheck(bot):
    while True:
        await main_checkpricesandnotify(tracked_model, bot)
        await asyncio.sleep(30)

async def get_active_users():
    if not os.path.exists('activate_users.txt'):
        return set()
    with open('activate_users.txt', 'r') as f:
        return set(line.strip() for line in f if line.strip())
async def activateadd(chat_id):
    users = await get_active_users()
    users.add(str(chat_id))
    with open('activate_users.txt', 'w') as f:
        for user in users:
            f.write(f'{user}\n')
async def deactivateremove(chat_id):
     users = await get_active_users()
     users.discard(str(chat_id))
     with open('activate_users.txt', 'w') as f:
         for user in users:
             f.write(f'{user}\n')
def load_user_models():
    if not os.path.exists(user_models_file):
        return {}
    with open(user_models_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return {}
def save_user_models(user_models):
    with open(user_models_file, 'w', encoding='utf-8') as f:
        json.dump(user_models, f, indent=4, ensure_ascii=False)
def add_model_for_user(user_id, model_name):
    user_models = load_user_models()
    if str(user_id) not in user_models:#если у пользователя нет модели, создаём пустой список
        user_models[str(user_id)] = []
    if model_name not in user_models[str(user_id)]:#Проверяет, есть ли уже такая модель у пользователя
        user_models[str(user_id)].append(model_name)
        save_user_models(user_models)
        return True
    return False

def remove_model_for_user(user_id, model_name):
    user_models = load_user_models()
    if str(user_id) in user_models and model_name in user_models[str(user_id)]:
        user_models[str(user_id)].remove(model_name)
        save_user_models(user_models)
        return True
    return False

def get_models_for_user(user_id):
    user_models = load_user_models()
    return user_models.get(str(user_id), [])











    









