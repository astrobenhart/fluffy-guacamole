from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

dir_path = 'midi_solo/'
try:
    os.stat(dir_path)
except:
    os.mkdir(dir_path)

chromedriver_path = 'chromed/chromedriver'
options = Options()
prefs = {"profile.managed_default_content_settings.images": 2, "download.default_directory" : str(dir_path)}
options.add_experimental_option("prefs", prefs)
chromewebd = webdriver.Chrome(executable_path=chromedriver_path, options=options)
chromewebd.set_window_size(500, 500)
sleep(2)

chromewebd.get('http://www.piano-midi.de/midi_files.htm')
sleep(3)

# ids = chromewebd.find_elements(By.TAG_NAME, 'a')

choices = chromewebd.find_elements_by_xpath("//div[contains(@tag, 'a') and contains(@class, 'navi')]")

for cc in choices:
    cc.click()
    sleep(5)
    ids = chromewebd.find_elements(By.TAG_NAME, 'a')
    for ii in ids:
        if str(ii.get_attribute('href'))[-4:] == '.mid':
            # print('downloading :'+str(ii.get_attribute('href')))
            ii.click()
    chromewebd.execute_script("window.history.go(-1)")
    sleep(5)