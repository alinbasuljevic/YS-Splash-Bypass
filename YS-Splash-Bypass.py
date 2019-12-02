from selenium import webdriver
import time, winsound, threading

def Browser(product_page):
    driver = webdriver.Chrome()
    splash_page = driver.get(product_page)
    waiting_loop = True
    while waiting_loop:
        if 'Waiting Room' in driver.page_source:
            print ('Still in Splash...')
            time.sleep(3)
            pass
        else:
            winsound.PlaySound("Passed_Splash.wav", winsound.SND_FILENAME)
            print ('Passed Splash! Check Browser!')
            waiting_loop = False
            pass

product_page = input('Enter Url: ')
num_of_tasks = input('Enter Number of Chrome Profiles: ')
for i in range(int(num_of_tasks)):
    t = threading.Thread(target=Browser(product_page))
    t.start()
