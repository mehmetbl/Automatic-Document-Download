from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://giris.turkiye.gov.tr/Giris/gir")
driver.implicitly_wait(10)
sleep(3)

tcno = input("TC No giriniz: ")
password = input("Şifrenizi giriniz: ")

driver.find_element(By.CSS_SELECTOR, '[name="tridField"]').send_keys(tcno)
driver.find_element(By.CSS_SELECTOR, '[name="egpField"]').send_keys(password)
sleep(1)

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-send"]').click()
driver.implicitly_wait(10)
sleep(3)

driver.find_element(By.CSS_SELECTOR, '[id="searchField"]').send_keys("Yükseköğretim Mezun Belgesi Sorgulama")
driver.find_element(By.CSS_SELECTOR, '[id="searchButton"]').click()
driver.implicitly_wait(10)
sleep(3)

driver.find_element(By.XPATH, '//*[@id="s01"]/div[2]/ul/li[2]/a').click()
driver.implicitly_wait(10)
sleep(5)

secenek = driver.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]/a').click()
driver.implicitly_wait(10)
sleep(5)

driver.find_element(By.CSS_SELECTOR, '[class="download"]').click()
sleep(10)







