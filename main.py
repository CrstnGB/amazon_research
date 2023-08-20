from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

def aceptar_cookies():
    try:
        boton_aceptar_cookies = wait.until(EC.presence_of_element_located((By.ID, 'sp-cc-accept')))
        boton_aceptar_cookies.click()
    except:
        pass

# Abrir una página web
url = 'https://www.amazon.es'
driver.get(url)

wait = WebDriverWait(driver, 5)  # Espera hasta 10 segundos

aceptar_cookies()

try:
    campo_buscador = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
except:
    campo_buscador = wait.until(EC.presence_of_element_located((By.ID, 'nav-bb-search')))

#texto_a_buscar = "B0C3DM1RW2"
texto_a_buscar = "laptop i7"
campo_buscador.send_keys(texto_a_buscar)

try:
    boton_buscar = driver.find_element(by = By.ID, value = 'nav-search-submit-button')
except:
    boton_buscar = driver.find_element(by = By.CLASS_NAME, value = 'nav-bb-button')

boton_buscar.click()

aceptar_cookies()

contenedor = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="sg-col-inner"]')))
descripcion = []
precio = []
for contenido in contenedor:
    try:
        descripcion_iterable = contenido.find_element(by = By.XPATH, value = './/*[@class="a-size-base-plus a-color-base a-text-normal"]')
        precio_iterable = contenido.find_element(by=By.XPATH, value='.//*[@class="a-price-whole"]')
    except:
        continue
    descripcion.append(descripcion_iterable)
    precio.append(precio_iterable)

desc_y_precio = list(zip(descripcion, precio))
print(len(desc_y_precio))

#Se trasnforma la lista creada en el texto que contiene para trabajar con este
desc_y_precio_texto = []
for sublista in desc_y_precio:
    lista_prov = []
    lista_prov.append(sublista[0].text)
    lista_prov.append(sublista[1].text)
    desc_y_precio_texto.append(lista_prov)

#Se eliminan duplicados, ya que por alguna razón, el primer resultado siempre se duplica (parece que tiene algo que ver
#con la opción Amazon
desc_y_precio = []
for elemento in desc_y_precio_texto:
    if elemento not in desc_y_precio:
        desc_y_precio.append(elemento)

for item in desc_y_precio:
    print("\nDescripción: {}".format(item[0]))
    print("Precio: {} €".format(item[1]))

input("presiona enter para continuar...")
# Cerrar el navegador
driver.quit()