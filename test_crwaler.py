from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

path = '/home/ubuntu/chromedriver'
driver = webdriver.Chrome(path)

url = "http://luka7.net/"
driver.get(url)

content = driver.find_element_by_css_selector("#coinList").text 
print(content)

driver.quit()
