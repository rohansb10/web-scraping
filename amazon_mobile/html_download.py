import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.makedirs("./amazon_mobile/data", exist_ok=True)

all = []
file = 0

for i in range(1,3):
    driver = webdriver.Chrome()
    url =f'https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&page=2&qid=1721370021&ref=sr_pg_{i}'
    driver.get(url)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "puisg-col-inner")))
        name_elements = driver.find_elements(By.CLASS_NAME, "puisg-col-inner")
        
        for element in name_elements:
            d = element.get_attribute("outerHTML")
            
            with open(f"./amazon_mobile/data/mobile_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
                file += 1
    except Exception as e:
        print(f"An error occurred: {e}")
        
    driver.quit()