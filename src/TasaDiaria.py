
import time
import openpyxl
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SBSTasaDiaria:

    def __init__(self):
        self.datos = []
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def iniciar_busqueda(self, url):
        self.driver.get(url)
        # self.driver.maximize_window()

    def recolectar_datos(self):
        tam = []
        time.sleep(2)
        tamn = self.driver.find_element(By.XPATH, '//table[@class="APLI_tabla"]/tbody/tr[1]/td[2]').text
        tamex = self.driver.find_element(By.XPATH, '//table[@class="APLI_tabla"]/tbody/tr[7]/td[2]').text

        float_tamn = float(tamn.strip('%'))
        float_tamex = float(tamex.strip('%'))

        tam.append(float_tamn)
        tam.append(float_tamex)
        self.driver.quit()

        return tam

