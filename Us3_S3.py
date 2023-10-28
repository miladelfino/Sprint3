import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from bensimon_links import *
import pytest 
import HTMLTestRunner


class TestHomePageNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bensimon.com.ar/")

    def test_nav_link_1(self):
        # Caso de prueba para el primer enlace en la barra de navegación
        link_element = self.driver.find_element_by_link_text("COLECCION")  
        link_element.click()
        self.assertEqual(self.driver.current_url, "https://bensimon.com.ar/coleccion") #URL esperada

    def test_nav_link_2(self):
        # Caso de prueba para el segundo enlace en la barra de navegación
        link_element = self.driver.find_element_by_link_text("JEANS POR CALCE")
        link_element.click()
        self.assertEqual(self.driver.current_url, "https://bensimon.com.ar/jeans-por-calce") #URL esperada

    def test_nav_link_3(self):
        # Caso de prueba para el tercer enlace en la barra de navegación
        link_element = self.driver.find_element_by_link_text("ACCESORIOS")
        link_element.click()
        self.assertEqual(self.driver.current_url, "https://bensimon.com.ar/accesorios") #URL esperada

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # Configuro el informe HTML
    report_path = 'test_report.html'
    with open(report_path, 'wb') as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report_file,
            title='Pruebas de Navegación de la Home Page',
            description='Resultados de las pruebas de navegación de los enlaces en la barra de navegación de la Home Page'
        )

        # Ejecuto las pruebas y genero el informe HTML
        unittest.main(testRunner=runner)
