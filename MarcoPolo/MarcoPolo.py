import threading                                                                                                                                
from time import time
from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import os 
from os.path import exists

# get GH_Token from GitHub to avoid hitting API limits
os.environ['GH_TOKEN'] = "**"

excel_path='D:\Programming\GitHub Connected Repo\Links.xlsx'
output_path="D:\Programming\GitHub Connected Repo\Screenshots\\"

df = pd.read_excel(excel_path)

# reads the url and index from the excel input file
url_list = df['Link'].tolist()
url_num=df["Num"].tolist()

# Browse function will take a starting location and open a Firefox browser 
# Locations depend on the size of the url list and are spread apart equally
def Browse(loc, driver):
    for i in range(loc,len(url_list)):
        URL = url_list[i]
        file= "screenshot_"+str(url_num[i])+".png"

        # skip if the url has already been processed
        if os.path.exists(output_path+file)==True:
            continue
        # skip if the url links to a pdf file
        if URL[-4:]==".pdf":
            continue
        
        driver.get(URL)                                                                                        
        driver.get_full_page_screenshot_as_file(output_path+file)
    driver.quit() # once you are done looping through the list close the browser

lenght=len(url_list)
exec(f't0 = threading.Thread(target=Browse, args=(0,webdriver.Firefox(executable_path=GeckoDriverManager().install())))')
exec(f't0.start()')

for t in range(1,7):
    loc=int(lenght/7*t)
    exec(f't{t} = threading.Thread(target=Browse, args=(loc,webdriver.Firefox(executable_path=GeckoDriverManager().install())))')
    exec(f't{t}.start()')

# To do:
# close broswer once it finishes its own subset as opposed to cycling through the entire list
# put GH_Token in a seperate file


# to avoid GDPR cookie prompts use a US proxy

