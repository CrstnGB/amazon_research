from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Abrir una página web
url = 'https://www.amazon.es'
driver.get(url)

wait = WebDriverWait(driver, 20)  # Espera hasta 10 segundos

try:
    boton_aceptar_cookies = wait.until(EC.presence_of_element_located((By.ID, 'sp-cc-accept')))
    boton_aceptar_cookies.click()
except:
    pass

campo_buscador = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
texto_a_buscar = "B0C3DM1RW2"
campo_buscador.send_keys(texto_a_buscar)

boton_buscar = driver.find_element(by = By.ID, value = 'nav-search-submit-button')
boton_buscar.click()

descripcion = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "a-size-small") and contains(@class, "a-color-base") and contains(@class, "a-text-normal")]')))
precio = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'a-price-whole')))

desc_precio = list(zip(descripcion.text, precio.text))
print(desc_precio)

input("presiona enter para continuar...")
# Cerrar el navegador
#driver.quit()