from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
@pytest.fixture
def dirver():
    # inicio o streamlit em backgraund
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    #fechar o streamlit apos os testes
    driver.quit()
    process.kill()

def test_app_opens(dirver):
    dirver.get("http://localhost:8501/")
    sleep(2)