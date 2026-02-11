import pytest
from selenium import webdriver
import json
import os

@pytest.fixture(scope="session")
def config():
    with open(os.path.join("config", "config.json")) as f:
        return json.load(f)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
