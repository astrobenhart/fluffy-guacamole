from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException, StaleElementReferenceException

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

music_list = ['http://www.piano-midi.de/albeniz.htm',
'http://www.piano-midi.de/bach.htm',
'http://www.piano-midi.de/balak.htm',
'http://www.piano-midi.de/beeth.htm',
'http://www.piano-midi.de/borodin.htm',
'http://www.piano-midi.de/brahms.htm',
'http://www.piano-midi.de/burgm.htm',
'http://www.piano-midi.de/chopin.htm',
'http://www.piano-midi.de/clementi.htm',
'http://www.piano-midi.de/debuss.htm',
'http://www.piano-midi.de/godowsky.htm',
'http://www.piano-midi.de/grana.htm',
'http://www.piano-midi.de/grieg.htm',
'http://www.piano-midi.de/haydn.htm',
'http://www.piano-midi.de/liszt.htm',
'http://www.piano-midi.de/mendelssohn.htm',
'http://www.piano-midi.de/moszkowski.htm',
'http://www.piano-midi.de/mozart.htm',
'http://www.piano-midi.de/muss.htm',
'http://www.piano-midi.de/rach.htm',
'http://www.piano-midi.de/ravel.htm',
'http://www.piano-midi.de/schub.htm',
'http://www.piano-midi.de/schum.htm',
'http://www.piano-midi.de/sinding.htm',
'http://www.piano-midi.de/tschai.htm',
'http://www.piano-midi.de/other.htm'
]

for url in music_list:
	chromewebd.get(url)
	sleep(3)

	choices = chromewebd.find_elements(By.TAG_NAME, 'a')

	for i in choices:
		try:
			tag_html = i.get_attribute('href')
		except StaleElementReferenceException:
			pass
		if tag_html:
			if tag_html[-11:] == 'format0.mid':
				try:
					i.click()
				except (ElementNotVisibleException, ElementNotInteractableException, StaleElementReferenceException) as e:
					pass

chromewebd.quit()