from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from configs import WEB_URL


class MarketDataScraper:
    def __init__(self, execution_time: datetime) -> None:
        self.execution_time = execution_time   
        self.browser = None   

    def initialize_browser(self):
        """Initializes and configures the Selenium WebDriver."""
        self.browser = webdriver.Chrome()
        self.browser.get(WEB_URL)
        self.browser.maximize_window()
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "bc-data-grid"))
        )


    def fetch_market_data_text(self)->str:
        """Extracts raw text data from the shadow DOM."""
        shadow_host = self.browser.find_element(By.CSS_SELECTOR, "bc-data-grid")
        shadow_root = self.browser.execute_script("return arguments[0].shadowRoot", shadow_host)
        root_element = shadow_root.find_element(By.CSS_SELECTOR, "#_root")
        return root_element.text


    def shutdown_browser(self)->None:
        """Closes the WebDriver if active."""
        if self.browser:
            self.browser.quit()
