from selenium import webdriver
from pyvirtualdisplay import Display
from CoinInfo import CoinInfo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Coin:
    def getCoinInfo(self):
        display = Display(visible=0, size=(1024, 768))
        display.start()

        path = '/home/ubuntu/chromedriver'
        driver = webdriver.Chrome(path)

        url = "http://luka7.net/"
        driver.get(url)
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#coinList>div.BTC>div.minus")))

        search_kewords = ['BTC', 'XRP']
        coin_infos = []
        for coin in search_kewords :
            coin_row = driver.find_element_by_css_selector('.{}'.format(coin))
            coin_name = coin_row.find_element_by_css_selector('.coin').text
            coin_usd = coin_row.find_element_by_css_selector('.usd').text
            coin_krw = coin_row.find_element_by_css_selector('.krw').text
            coin_price_diff = coin_row.find_element_by_css_selector('.minus').text
            coin_info = CoinInfo(coin_name, coin_usd, coin_krw, coin_price_diff)
            coin_infos.append(coin_info)
        result_text = '''
        오늘의 코인 가격 정보
        {} :
        원화 가격 : {}
        달러 가격 : {}
        전일 대비 증/감 : {}
        
        {} :
        원화 가격 : {}
        달러 가격 : {}
        전일 대비 증/감 : {}
        '''.format(coin_infos[0].name, coin_infos[0].price_krw, coin_infos[0].price_usd, coin_infos[0].price_diff,
                   coin_infos[1].name, coin_infos[1].price_krw, coin_infos[1].price_usd, coin_infos[1].price_diff)
        return result_text
        driver.quit()
