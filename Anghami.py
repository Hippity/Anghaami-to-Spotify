from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os.path

driver=webdriver.Chrome(executable_path=########Enter your chromedrive path)
driver.get('https://play.anghami.com/login')

p=int(input('Enter the number of playlists: '))


##### Path to save files
path= #########Enter your path to save the files location (Better to put it next to Spotify.py)


#### Function to extract x number of playlists and put them into separate files

def playlist(p):
    L=[]
    for x in range(0,p):
        x=x+1
        name=driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-mymusic-new/div/div/div[2]/div/anghami-new-section-builder/div[2]/anghami-list-section/div/div/div/div['+str(x)+']/div[2]').text
        driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-mymusic-new/div/div/div[2]/div/anghami-new-section-builder/div[2]/anghami-list-section/div/div/div/div['+str(x)+']/div[2]').click()

        for i in range(10):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)
            try:
                driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-view/div/div[2]/anghami-new-section-builder/div[2]/anghami-list-section/div/div[2]/button').click()
            except ElementClickInterceptedException:
                pass
            except NoSuchElementException:
                pass

        L.append(name)
        comp= os.path.join(path,str(name)+".txt")
        f=open(comp,'w+')
        song_number= driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-view/div/div[1]/anghami-collection-header-side/div/div/div[3]/span/div').text

        for i in range(2,int(song_number[0:3])+5):
            try:
                song=driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-view/div/div[2]/anghami-new-section-builder/div[2]/anghami-list-section/div/div/div/div['+str(i)+']/div[4]').text
                artist=driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-view/div/div[2]/anghami-new-section-builder/div[2]/anghami-list-section/div/div/div/div['+str(i)+']/div[6]').text
                f.write(str(song)+' '+str(artist))
                f.write('\n')
            except NoSuchElementException:
                pass
        f.close()
        driver.get('https://play.anghami.com/playlists')
    return L





driver.find_element_by_xpath('//*[@id="ang_app"]/anghami-login-page/div/anghami-main-login/div/anghami-login-landing/div/div/div/span').click()

## Mail

driver.find_element_by_xpath('//*[@id="ang_app"]/anghami-login-page/div/anghami-main-login/div/anghami-more-ways-login/div/div/form/span/input').send_keys(######Enter Mail)

driver.find_element_by_xpath('//*[@id="ang_app"]/anghami-login-page/div/anghami-main-login/div/anghami-more-ways-login/div/div/form/button').click()

## Pass
sleep(5)

driver.find_element_by_xpath('//*[@id="ang_app"]/anghami-login-page/div/anghami-main-login/div/anghami-fill-email-password/div/div/form/span[2]/input').send_keys(#####Enter Password)

driver.find_element_by_xpath('//*[@id="ang_app"]/anghami-login-page/div/anghami-main-login/div/anghami-fill-email-password/div/div/form/button').click()

## By now login should be complete
sleep(15)

driver.find_element_by_xpath('//*[@id="ang-nav"]/div/ul/li[5]').click()

sleep(5)

driver.find_element_by_xpath('//*[@id="base_content"]/div/anghami-mymusic-new/div/div/div[1]/div/div/div[4]/div[5]').click()

### Playlist Songs


Playlists=playlist(p)
print(Playlists)


