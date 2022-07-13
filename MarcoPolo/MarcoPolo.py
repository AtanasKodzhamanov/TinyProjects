import threading                                                                                                                                
from time import time
from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import os 
from os.path import exists

os.environ['GH_TOKEN'] = "**"

df = pd.read_excel('D:\Programming\GitHub Connected Repo\Links.xlsx')
mylist = df['Link'].tolist()
num=df["Num"].tolist()

def Browse(loc, driver):
    for i in range(loc,len(mylist)):
        URL = mylist[i]
        file= "screenshot_"+str(num[i])+".png"

        if os.path.exists("D:\Programming\GitHub Connected Repo\Screenshots\\"+file)==True:
            continue
        if URL[-4:]==".pdf":
            continue
        
        driver.get(URL)                                                                                        
        driver.get_full_page_screenshot_as_file("D:\Programming\GitHub Connected Repo\Screenshots\\"+file)
    driver.quit()

lenght=len(mylist)
exec(f't0 = threading.Thread(target=Browse, args=(0,webdriver.Firefox(executable_path=GeckoDriverManager().install())))')
exec(f't0.start()')

for t in range(1,7):
    loc=int(lenght/7*t)
    exec(f't{t} = threading.Thread(target=Browse, args=(loc,webdriver.Firefox(executable_path=GeckoDriverManager().install())))')
    exec(f't{t}.start()')


