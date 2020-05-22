#!/usr/bin/python3

from selenium import webdriver
from time import sleep 
from os import system
from os import environ

nichtpara_instance = environ['NICHTPARA_INSTANCE']
nichtpara_usr = environ['NICHTPARA_USR']
nichtpara_pwd = environ['NICHTPARA_PWD']
jitsi_instance = environ['JITSI_INSTANCE']

def xdo(command, delay=0.1):
    sleep(delay)
    system("xdotool " + command)

browser = webdriver.Firefox()

browser.get(jitsi_instance)
sleep(1)
screensharebutton = browser.find_element_by_css_selector("div[aria-label=\"Toggle screenshare\"]")
screensharebutton.click()
sleep(0.5)

#click "window or screen to share"
xdo("mousemove 500 190 click 1")

#select "entire screen"
xdo("mousemove 500 280 click 1")

#select "allow button"
for i in range(0, 5):
    xdo("key \"Tab\"")

#press "allo"
xdo("key \"Return\"")

#open new tab
xdo("key \"Ctrl+t\"")

sleep(0.5)
browser.switch_to.window(browser.window_handles[1])
browser.get(nichtpara_instance)
#enter username
xdo("type \"" + nichtpar_usr  + "\"")
xdo("key \"Tab\"")
#enter password
xdo("type \"" + nichtpara_pwd  + "\"")
#confirm
xdo("key \"Tab\"")
xdo("key \"Tab\"")
xdo("key \"Return\"")

#enter fullscreen
xdo("key F11")
xdo("mousemove 3000 100")

# monitor firefox until failure
# then die for restarting container
try:
    while True:
        sleep(1)
        if(len(browser.window_handles) < 2):
            print("window handle was was smaller thant two: cleaning firefox")
            system("pkill -9 firefox")
            quit(0)
except:
    print("firefox broke: cleaning firefox")
    system("pkill -9 firefox")
    quit(0)
    
