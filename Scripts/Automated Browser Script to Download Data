import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


#--------------------------------------------------NHS5
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',{
	"download.default_directory": "G:\\My Drive\\Projects\\Projects\\Data\\temp\\NHS5", #Change default directory for downloads
	"download.prompt_for_download": False, #To auto download the file
	"download.directory_upgrade": True,
	"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
	})

driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
driver.get("http://rchiips.org/nfhs/factsheet_NFHS-5.shtml")


state = driver.find_element("id", "state")



for option in state.find_elements(By.TAG_NAME,'option'):
    print(option)
    option.click()
    time.sleep(3)


#---------------------------------------------------NHS4
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',{
	"download.default_directory": "G:\\My Drive\\Projects\\Projects\\Data\\temp\\NHS4", #Change default directory for downloads
	"download.prompt_for_download": False, #To auto download the file
	"download.directory_upgrade": True,
	"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
	})

driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
driver.get("http://rchiips.org/nfhs/factsheet_NFHS-4.shtml")


state = driver.find_element("id", "state")



for option in state.find_elements(By.TAG_NAME,'option'):
    print(option)
    option.click()
    time.sleep(3)


#---------------------------------------------------NHS3
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',{
	"download.default_directory": "G:\\My Drive\\Projects\\Projects\\Data\\temp\\NHS3", #Change default directory for downloads
	"download.prompt_for_download": False, #To auto download the file
	"download.directory_upgrade": True,
	"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
	})

driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
driver.get("http://rchiips.org/nfhs/factsheet.shtml")


state = driver.find_element("name", "menu1")



for option in state.find_elements(By.TAG_NAME,'option'):
    print(option)
    option.click()
    time.sleep(3)