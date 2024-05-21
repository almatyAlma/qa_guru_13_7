import os

import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.abspath("Users//technodom//PycharmProjects//qa_guru_13_7//tmp"),
    "download.prompt_for_download": False
}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver
browser.open("https://github.com/qa-guru/qa_guru_python_9_7_files/tree/master/tmp")
browser.element('[class="href="/qa-guru/qa_guru_python_9_7_files/blob/master/tmp/Python%20Testing%20with%20Pytest%20(Brian%20Okken).pdf"]').click()
time.sleep(20)
browser.quit()