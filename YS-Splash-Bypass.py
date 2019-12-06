from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time, winsound, threading

def Browser(product_page):
    options = Options()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\abasuljevic\\Downloads\\YS-Splash-Bypass-master\\YS-Splash-Bypass-master\\chromedriver.exe', options=options)
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

product_page = input('Enter Url: ')
num_of_tasks = input('Enter Number of Firefox Profiles: ')
for i in range(int(num_of_tasks)):
    t = threading.Thread(target=Browser(product_page))
    t.start()
