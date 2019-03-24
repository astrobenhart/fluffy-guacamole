from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chromedriver_path = 'chromed/chromedriver'
options = Options()
prefs = {"profile.managed_default_content_settings.images": 2, "download.default_directory" : "midi/"}
options.add_experimental_option("prefs", prefs)
chromewebd = webdriver.Chrome(executable_path=chromedriver_path, options=options)
chromewebd.set_window_size(500, 500)
sleep(2)

chromewebd.get('https://bushgrafts.com/midi/')
sleep(3)

ids = chromewebd.find_elements(By.TAG_NAME, 'a')

for ii in ids:
    if str(ii.get_attribute('href'))[-4:] == '.mid':
        # print('downloading :'+str(ii.get_attribute('href')))
        ii.click()