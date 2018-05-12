
# coding: utf-8

# In[1]:


import certifi
import time
import lxml
import urllib3
import requests
import csv
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from selenium import webdriver
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import webbrowser


# In[2]:


url = 'https://www.livechatinc.com/typing-speed-test/?t=27582512#/'
url1 = 'http://www.typeonline.co.uk/typingspeed.php?'

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())


chromedriver = webdriver.Chrome()


# In[51]:


#chrome = webbrowser.get(chromeDoc).open(url)


# In[13]:


#play first website

chromedriver.get(url)

cnt = 0
sleeptime = 5
m = PyMouse()
k = PyKeyboard()
time.sleep(30)
while cnt < 507 :
    pageSource = chromedriver.page_source  # 取得網頁原始碼
    soup = BeautifulSoup(pageSource, 'html.parser')

    result = soup.select('.test-word')[cnt:]
   
    print(result[0].get_text())
    #print(len(result))
    time.sleep(sleeptime)
    for i in result:
        word = i.get_text()
        #print(word)
        k.type_string(word+' ')
        cnt += 1
        if cnt >= 507:
            chromedriver.save_screenshot('finish.png')
            break
    sleeptime = 0


# In[14]:


#play the second website
chromedriver.get(url1)
pageSource = chromedriver.page_source  # 取得網頁原始碼
soup = BeautifulSoup(pageSource, 'html.parser')

result = soup.select('#sampleText')[0].text
result = result.split(',')
print(result)
print(len(result))
sleeptime = 5
time.sleep(sleeptime)
chromedriver.find_element_by_id('startButton').click()

for word in result:
    if word == '':
        k.type_string(',')
    else:
        k.type_string(word)
#chromedriver.find_element_by_id('copyTextInputBox').click()
time.sleep(0.5)
chromedriver.find_element_by_id('stopButton').click()
k.press_key(k.control_l_key)
k.tap_key(k.numpad_keys['Home'])
k.release_key(k.control_l_key)
chromedriver.save_screenshot('finish1.png')


# In[61]:


print(cnt)
chromedriver.close()

