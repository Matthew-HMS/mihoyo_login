import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
from selenium.common.exceptions import NoSuchElementException
import sys

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
driver.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&lang=zh-tw&bbs_theme=dark&bbs_theme_device=1")
time.sleep(3)
cookies = pickle.load(open("mihoyo.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@class='components-home-assets-__sign-guide_---guide-close---2VvmzE']").click()
driver.find_element(By.XPATH, "//*[@class='components-home-assets-__sign-content-test_---more-icon---202NrS']").click()
time.sleep(10)
try:
    reward = driver.find_element(By.XPATH, "//*[@class='components-home-assets-__sign-content-test_---actived-day---34r3rb']")
    reward.click()
except NoSuchElementException:
    print("Already claimed")
    pass
# time.sleep(30)
# pickle.dump(driver.get_cookies(), open("mihoyo.pkl", "wb"))
# print("cookie saved")


# quit
time.sleep(3)
sys.exit()
driver.quit()