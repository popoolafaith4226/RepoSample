import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from repository_page import RepositoryPage
from login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def authenticated_session(driver):
    login = LoginPage(driver)
    login.navigate_to("https://github.com/login")
    login.enter_credentials("valid_user", "secure_password")
    login.submit()
    yield driver

def test_repository_creation(authenticated_session):
    repo_page = RepositoryPage(authenticated_session)
    assert repo_page.create_new_repository(
        name="test-repo-1",
        description="Automation test repository",
        private=True
    ), "Repository creation failed"

def test_public_repository_creation(authenticated_session):
    repo_page = RepositoryPage(authenticated_session)
    assert repo_page.create_new_repository(
        name="test-repo-2",
        description="Public test repo"
    ), "Public repository creation failed"