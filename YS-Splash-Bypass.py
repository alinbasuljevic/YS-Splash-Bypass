from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, winsound, threading

def Browser():
    product_page = 'https://www.yeezysupply.com/product/FV3260'
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\resel\\Downloads\\Symphony-master\\Symphony-master\\chromedriver.exe', options=options)
    splash_page = driver.get(product_page)
    time.sleep(5)
    waiting_loop = True
    while waiting_loop:
        if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/h3'):
            print ('Still in Splash...')
            time.sleep(10)
            pass
        else:
            winsound.PlaySound("Passed_Splash.wav", winsound.SND_FILENAME)
            print ('Passed Splash! Check Browser!')
            waiting_loop = False
            pass

num_of_tasks = input('Enter Number of Profiles: ')
for i in range(int(num_of_tasks)):
    t = threading.Thread(target=Browser())
    t.start()
