from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.com.br")
login = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
login.click()

email_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
email_input.send_keys('teste@gmail.com')
continuar_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continuar_button.click()

time.sleep(3)

senha_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
senha_input.send_keys('senha-teste-123456')
login_button = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
login_button.click()

time.sleep(3)

produtos = ["mouse", "teclado", "mousepad"]
for produto in produtos:
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(produto)
    search_box.send_keys(Keys.RETURN)

    first_result = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[2]/span/a')
    first_result.click()

    try:
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="submit.add-to-cart"]/span')
        add_to_cart_button.click()
        print(f"Produto '{produto}' adicionado ao carrinho.")
    except:
        print(f"Não foi possível adicionar '{produto}' ao carrinho.")

    screenshot_path = f"{produto}_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot salva em: {screenshot_path}")

    time.sleep(2)

cart = driver.find_element(By.XPATH, '//*[@id="nav-cart"]')
cart.click()

time.sleep(2)

screenshot_path = f"carrinho_finalizado.png"
driver.save_screenshot(screenshot_path)
print(f"Carrinho finalizado")

driver.quit()
