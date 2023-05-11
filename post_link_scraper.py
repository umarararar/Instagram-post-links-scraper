import instaloader
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
import openpyxl
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#options = Options()
options = uc.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-cookies")
# driver = webdriver.Chrome(options=options)
driver = uc.Chrome(options=options)
# create an instance of the ActionChains class
actions = ActionChains(driver)
driver.maximize_window()

driver.get("https://www.instagram.com/")
wait01 = WebDriverWait(driver, 50)

try:
    #/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]
    cookies = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")))
    cookies.click()
except:
    pass
username_input = wait01.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
password_input = wait01.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

username_input.send_keys("aiza.khan3627")
password_input.send_keys("aiza0099")

login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
try:
    notnow=WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
    notnow.click()
except:
    pass

with open('followers_output.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    profName = line.strip()  # remove newline character
    driver.get('https://www.instagram.com/' + profName)
    sleep(3)

sleep(5)
postCount=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span")
post_count=int(postCount.text)
sleep(3)


real_post_count=int(post_count/3)
flag=False
counterPost=0
for i in range(1,real_post_count+1):
    for j in range(1,4):
        
        if(i*j>=33):
            flag=True
            print("!!!!!!!")
            break
        else:
            post=driver.find_element(By.XPATH,f"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[{i}]/div[{j}]/a/div/div[2]")
            driver.execute_script("arguments[0].scrollIntoView();", post)
            post.click()
            postUrl=driver.current_url  # print the current URL
            counterPost+=1
          #  sleep(3)
            cross=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")
            cross.click()
    if(flag==True):
        print(counterPost)
        break

#


sleep(1000)