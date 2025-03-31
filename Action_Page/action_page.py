from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from repository_locators import RepositoryLocators


class RepositoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def create_new_repository(self, name, description="", private=False):
        self.wait.until(EC.element_to_be_clickable(
            RepositoryLocators.NEW_REPO_BUTTON)).click()

        self.wait.until(EC.visibility_of_element_located(
            RepositoryLocators.REPO_NAME_FIELD)).send_keys(name)

        if description:
            self.driver.find_element(*RepositoryLocators.REPO_DESC_FIELD).send_keys(description)

        if private:
            self.driver.find_element(*RepositoryLocators.REPO_VISIBILITY_PRIVATE).click()

        self.wait.until(EC.element_to_be_clickable(
            RepositoryLocators.CREATE_BUTTON)).click()

        return self.wait.until(EC.visibility_of_element_located(
            RepositoryLocators.SUCCESS_BANNER)).is_displayed()