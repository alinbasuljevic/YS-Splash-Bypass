from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, winsound, threading

def Browser():
    PROXY = '### ENTER PROXY HERE ####'
    product_page = 'https://www.yeezysupply.com/product/FW4968' ### Edit the link before running the script ###
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
    
    }
    capabilities = options.to_capabilities()
    driver = webdriver.Chrome(executable_path = "C:\\Users\\resel\\Downloads\\Symphony-master\\Symphony-master\\chromedriver.exe", desired_capabilities=capabilities)
    splash_page = driver.get(product_page)
    time.sleep(5)
    waiting_loop = True
    while waiting_loop:
        try:
            if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/h3'):
                print ('Still in Splash...')
                time.sleep(10)
                pass
        except:
            winsound.PlaySound("Passed_Splash.wav", winsound.SND_FILENAME)
            print ('Passed Splash! Check Browser!')
            waiting_loop = False
            pass

num_of_tasks = input('Enter Number of Profiles: ')
for i in range(int(num_of_tasks)):
    t = threading.Thread(target=Browser)
    t.start()
