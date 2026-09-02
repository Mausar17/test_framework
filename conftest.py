import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
from clients.user_client import UserClient
from selenium.webdriver.chrome.options import Options

load_dotenv()

@pytest.fixture
def driver():
    options = Options()
    if os.environ.get("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_key():
    key = os.environ.get("API_KEY")
    if not key:
        pytest.fail("Environment variable API_KEY not set")
    return key

@pytest.fixture(scope="session")
def headers(api_key):
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

@pytest.fixture(scope="session")
def user_client(headers):
    return UserClient(base_url="https://reqres.in/api", headers=headers)