import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

all_data = []
base_url = "https://sldict.korean.go.kr/front/sign/signList.do?current_pos_index=&origin_no=0&searchWay=count&top_category=CTE&category=&detailCategory=&searchKeyword=&pageIndex="

for page_index in range(1, 4):
    url = base_url + str(page_index)
    driver.get(url)

    for i in range(1, 11):
        # get the link and click it
        link_path = f"/html/body/div[2]/div[2]/div/div/div[4]/form/div[2]/div[2]/ul/li[{i}]/div[2]/div/ul/li/div/p/span[1]/a"
        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, link_path)))
        link.click()

        # wait for the new page to load
        time.sleep(1)

        # get the image source
        image_path = "/html/body/div[2]/div[2]/div/div/div[4]/form/div[3]/div[2]/div/div/div[1]/div/dl/dd[1]/a/img"
        image_src = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_path))).get_attribute('src')

        # get the description
        description_path = "/html/body/div[2]/div[2]/div/div/div[4]/form/div[3]/div[2]/div/div/div[1]/div/dl/dd[2]"
        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, description_path))).text

        # get the name
        name_path = "/html/body/div[2]/div[2]/div/div/div[4]/form/dl/dd"
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_path))).text

        # append the data to the list
        all_data.append({
            "name": name,
            "description": description,
            "image_src": image_src
        })

        # go back to the list page
        driver.back()
        time.sleep(1)

driver.quit()

for data in all_data:
    print(data)
    
###################

import os
import requests

# 이미지 다운로드 함수
def download_image(image_url, image_path):
    response = requests.get(image_url, verify=False)

    with open(image_path, 'wb') as f:
        f.write(response.content)

###################

from todaysignlan.models import Sign
from django.core.files.base import ContentFile

def save_to_database(name, description, image_path):
    sign = Sign(name=name, description=description)
    image_data = open(image_path, 'rb').read()
    sign.image.save(os.path.basename(image_path), ContentFile(image_data), save=True)

####################

for data in all_data:
    # 이미지 다운로드
    image_path = f"media/signoftheday/{data['name']}.jpg"
    download_image(data['image_src'], image_path)
    
    # 데이터베이스에 저장
    save_to_database(data['name'], data['description'], image_path)