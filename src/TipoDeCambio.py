
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from timeit import default_timer
from time import sleep
from datetime import datetime, timedelta
import time

class SBSTipoCambio:

    def __init__(self):
        self.datos = []
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def iniciar_busqueda(self, url):
        self.driver.get(url)
        #self.driver.maximize_window()

    def recolectar_datos(self):

        # Obteniendo fecha Metodo
        addDays = -1
        if datetime.today().weekday() == 4:  # 4 es día viernes
            addDays = -3

        att_fecha = (datetime.now() + timedelta(days=addDays)).strftime("%d/%m/%Y")
        #att_fecha = datetime.today().strftime('%Y-%m-%d')

        # Obteniendo datos de los precios
        precios = []
        precios_compra = self.driver.find_elements(By.XPATH, "//table[@class='rgMasterTable']/tbody/tr/td[2]")
        precios_venta = self.driver.find_elements(By.XPATH, "//table[@class='rgMasterTable']/tbody/tr/td[3]")


        print(precios_compra[0].text)
        print(precios_venta[0].text)
        print(precios_compra[6].text)
        print(precios_venta[6].text)

        #self.datos_requeridos = [att_fecha, precios[0], precios[12], precios[8], precios[20]]
        self.datos_requeridos = [att_fecha, precios_compra[0].text, precios_venta[0].text, precios_compra[6].text, precios_venta[6].text]
        self.driver.quit()

        return self.datos_requeridos

