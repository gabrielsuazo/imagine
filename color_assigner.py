import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import numpy as np

QUERY_LIMIT = 10


def retrieve_avg_color(query):
    colors = []
    driver = webdriver.Chrome()
    url = f'https://www.ecosia.org/images?q={query}&source=lnms&tbm=isch'
    driver.get(url)

    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    images = soup.find_all('img', limit=QUERY_LIMIT)

    for img_tag in images:
        try:
            img_url = img_tag['src']
            # print("Image URL: " + img_url)

            if "https://" in img_url:
                img_data = requests.get(img_url).content
            elif "data:image/gif;base64" in img_url:
                # img_url_clean = img_url.replace('data:image/gif;base64,', '')
                # img_data = base64.b64decode(img_url_clean)
                continue
            else:
                # print("Unknown url type")
                continue
        except Exception as e:
            print(e)
            continue

        try:
            img = Image.open(BytesIO(img_data))

            img_array = np.array(img)

            avg_color = img_array.mean(axis=(0, 1))

            # print(f'Average color of the image: {avg_color}')
            colors.append(avg_color)
        except Exception as e:
            print("ERROR:")
            print(img_url)
            print(e)
    driver.quit()

    if len(colors) == 0:
        print("Error: no colors retrieved")
        return 255, 255, 255
    else:
        return np.average(colors, axis=0)
