from selenium.webdriver.common.by import By

class RepositoryLocators:
    NEW_REPO_BUTTON = (By.XPATH, "//button[contains(text(),'New repository')]")
    REPO_NAME_FIELD = (By.ID, "repository_name")
    REPO_DESC_FIELD = (By.ID, "repository_description")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Create repository')]")
    REPO_VISIBILITY_PRIVATE = (By.ID, "repository_visibility_private")
    SUCCESS_BANNER = (By.CSS_SELECTOR, ".flash-message.success")