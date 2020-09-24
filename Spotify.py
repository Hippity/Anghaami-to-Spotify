from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 
from pyautogui import write
from pyautogui import click as clic
import os.path

driver=webdriver.Chrome(executable_path=##########Enter chromedriver path)
driver.get('https://open.spotify.com/')
name=input('Enter File Name: ')
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[4]/button[2]').click()

## Email and Pass
sleep(10)
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(######Enter Mail)
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(######Enter Pass       +Keys.ENTER)


## Creating the Playlist
sleep(10)
driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div/div[1]/button').click()
sleep(1)
write(name)
driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[2]/div[2]/button').click()


#### Search

driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a').click()
play=open(name +'.txt','r')
for line in play:
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input').send_keys(line)
    sleep(3)
    clic(x=808,y=741,button='right')
    sleep(0.5)
    clic(x=890,y=560)
    sleep(0.5)
    clic(x=171,y=671)
    sleep(0.5)
    clic(x=185, y=347)
    sleep(0.5)
    clic(x=895, y=204)



