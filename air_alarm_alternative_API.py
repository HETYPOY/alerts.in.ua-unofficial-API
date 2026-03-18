import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

print(f"https://map.ukrainealarm.com alternative API module by @Zloi_Ramen. Use responsibly.")

class Session:
    def __init__(self,lang:str="en",timeout:int=6):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=en-en')
        options.add_argument("--headless=new")
        options.page_load_strategy = "eager"
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1080,1080)
        driver.implicitly_wait(timeout)
        if lang=="en":
            driver.get("https://alerts.in.ua/en")
        else:
            driver.get("https://alerts.in.ua")
        list_btn = driver.find_element(By.XPATH,"/html/body/main/div[1]/div[3]/div[13]")
        list_btn.click()
        self.active_list = driver.find_elements(By.CSS_SELECTOR,".alert-container")
    def get_active_alarms(self) -> dict:
        alarms = {}
        for alarm in self.active_list:
            #print(alarm.text)
            #text = alarm.find_element(By.CLASS_NAME,"text-container")
            region = alarm.find_element(By.TAG_NAME, "strong").text
            type_ = alarm.find_elements(By.CLASS_NAME, "alert-extra")[0].text
            duration = alarm.find_elements(By.CLASS_NAME, "alert-extra")[1].text.strip()
            alarms[region] = {"type":type_,"duration":duration}
        return alarms
