
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from tkinter import *
from tkinter import messagebox as MessageBox

class BVL:

    def __init__(self):
        self.datos = []
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def iniciar_busqueda(self, url):
        self.driver.get(url)
        #self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0,200);")

    def error(self):
        # Cerramos el pop-up si aparece
        sleep(8)
        try:
            boton_error = self.driver.find_element(By.ID, 'modalButtonClose')
            boton_error.click()
            print('Pop-up cerrado')
        except:
            print('No hubo pop-up')

    def recolectar_datos(self):
        #self.driver.find_element(By.CLASS_NAME, "accordion-toggler").click()
        try:
            #self.driver.execute_script("window.scrollTo(0,document.body.scroolHeight)")
            self.driver.find_element(By.XPATH, "(//*[@class='accordion-toggler'])[1]").click()
        except:
            MessageBox.showerror("Error", "Ha ocurrido un error al momento de llamar a los elementos por xpath.")

        sleep(2)
        #self.driver.execute_script("window.scrollTo(0,4000);")
        resumen_mercado = self.driver.find_element(By.LINK_TEXT, "Resumen de Mercado").get_attribute('href')
        resumen_montos = self.driver.find_element(By.LINK_TEXT, "Resumen de Montos y Operaciones").get_attribute('href')
        data = self.clasificar_datos(resumen_mercado, resumen_montos)
        # print(data)
        return data

    def clasificar_datos(self, porcentajes, monto):

        self.iniciar_busqueda(porcentajes)
        igb = float(self.driver.find_elements(By.TAG_NAME, "td")[14].text.replace(",", ""))
        indice_general_bursatil_d = float(self.driver.find_elements(By.TAG_NAME, "td")[15].text)
        indice_general_bursatil_m = float(self.driver.find_elements(By.TAG_NAME, "td")[16].text)
        isb = float(self.driver.find_elements(By.TAG_NAME, "td")[32].text.replace(",", ""))
        indice_selectivo_bursatil_d = float(self.driver.find_elements(By.TAG_NAME, "td")[33].text)
        indice_selectivo_bursatil_m = float(self.driver.find_elements(By.TAG_NAME, "td")[34].text)

        self.iniciar_busqueda(monto)
        monto_negociado_acciones = float(self.driver.find_elements(By.TAG_NAME, "td")[30].text.replace(",", ""))

        self.datos.append(indice_general_bursatil_d)
        self.datos.append(indice_selectivo_bursatil_d)
        self.datos.append(monto_negociado_acciones)
        self.datos.append(indice_general_bursatil_m)
        self.datos.append(indice_selectivo_bursatil_m)
        self.datos.append(igb)
        self.datos.append(isb)
        #self.driver.quit()

        return self.datos

    def archivar_datos(self):
        df_bvl = pd.DataFrame([self.datos],
                              columns=['Indice general bursátil d', 'indice selectivo bursatil d', 'monto negociado',
                                       'indice generak bursatl m',
                                       'indice selectivo bursatil m', 'igb', 'isb'])

        df_bvl.to_excel('indices_bvl.xlsx', startcol=5,startrow=3, sheet_name='indicadores')
        return df_bvl

