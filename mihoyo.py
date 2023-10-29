import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument('--window-size=1920,1080')
options.add_argument("--user-data-dir=C:\\Users\\Skywalker\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&lang=zh-tw&bbs_theme=dark&bbs_theme_device=1")
time.sleep(3)

# close and extend window
try:
    actions = ActionChains(driver)
    driver.find_element(By.XPATH, "//*[@class='components-home-assets-__sign-guide_---guide-close---2VvmzE']").click()
    more = driver.find_element(By.XPATH, "//*[@class='components-home-assets-__sign-content-test_---more-icon---202NrS']")
    actions.move_to_element(more).click().perform()
    time.sleep(3)
except:
    pass

# claim reward
try:
    reward = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='components-home-assets-__sign-content-test_---sign-item---3gtMqV components-home-assets-__sign-content-test_---sign-wrapper---22GpLY']")))
    actions.move_to_element(reward).click().perform()
    # reward.click()
except:
    print("Already claimed")
    pass


# quit
time.sleep(5)
driver.quit()