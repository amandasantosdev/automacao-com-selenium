from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(service=service, chrome_options=chrome_options)

navegador.get("https://ficsys-prod.vercel.app/")
navegador.find_element('xpath', '//*[@id="__next"]/div/article/div/div/form/input[1]').send_keys("LOGIN-DO-USUARIO")
navegador.find_element('xpath', '//*[@id="__next"]/div/article/div/div/form/input[2]').send_keys("SENHA-DO-USUARIO")
navegador.find_element('xpath', '//*[@id="__next"]/div/article/div/div/form/button').click()
