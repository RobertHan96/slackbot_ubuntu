from WantedInfo import WantedInfo
from selenium import webdriver
from pyvirtualdisplay import Display
import time

class Wanted :
    def getWantedInfo(self):
        display = Display(visible=0, size=(1024, 768))
        display.start()
        path = '/home/ubuntu/chromedriver'

        driver = webdriver.Chrome(path)
        url = 'https://www.wanted.co.kr/wdlist/518/678?country=kr&job_sort=job.latest_order&years=0&locations=all'
        driver.get(url)

        wanted_jobs = []
        url_list = []
        time.sleep(10)

        datas = driver.find_element_by_css_selector('ul.clearfix')
        companies = datas.find_elements_by_class_name('body')
        urls = datas.find_elements_by_tag_name('a')

        for url in urls:
            detail_link = url.get_property('href')
            url_list.append(detail_link)
        i = 0
        for company in companies:
            position_name = company.find_element_by_class_name('job-card-position').text
            name = company.find_element_by_class_name('job-card-company-name').text
            location = company.find_element_by_class_name('job-card-company-location').text
            reward = company.find_element_by_class_name('reward').text
            url = url_list[i]
            i += 1
            wanted_jobs.append(WantedInfo(name, location, position_name, reward, url))

        response_text = '원티드에서 찾은 {}개의 개발자 채용정보'.format(len(wanted_jobs))
        for job in wanted_jobs:
            response_text = response_text + '\n{} / {} / {}\n{}\n{}'.format(
                job.name, job.position_name, job.location, job.reward, job.url)
        print(response_text)
        return response_text
        driver.quit()
