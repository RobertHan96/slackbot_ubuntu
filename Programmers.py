from WantedInfo import WantedInfo
from selenium import webdriver
from ProgrammersInfo import ProgrammersInfo
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(1024, 768))
display.start()
path = '/home/ubuntu/chromedriver'
driver = webdriver.Chrome(path)
url = 'https://programmers.co.kr/job?job_position%5Bmin_career%5D=&amp;job_position%5Bjob_category_ids%5D%5B%5D=3&amp;job_position%5Bjob_category_ids%5D%5B%5D=10&amp;_=1593673591520'

driver.get(url)
programmers_jobs = []
time.sleep(10)

datas = driver.find_elements_by_css_selector('li.list-position-item>div.item-body')

for com in datas:
    name = com.find_element_by_css_selector('.company-name').text
    position_name = com.find_element_by_css_selector('.position-title>a').text
    url = com.find_element_by_css_selector('.position-title>a').get_property('href')
    location = com.find_element_by_css_selector('.company-info>.location').text
    min_career = com.find_element_by_css_selector('.company-info>.experience').text
    programmers_jobs.append(ProgrammersInfo(name, position_name, url, location, min_career))

jobs_count = len(programmers_jobs)
response_text = '프로그래머스에서 찾은 {}개의 개발자 채용정보'.format(jobs_count)
for job in programmers_jobs:
    response_text = response_text + '\n{} / {} / {}\n{}\n{}'.format(
        job.name, job.position_name, job.min_career, job.location, job.url)

print(response_text)
driver.quit()


# class Programmers:
#     def getProgrammersInfo(self):
#         driver_path = '/Users/mac/0_Dev/PythonProjects/get_coin/chromedriver'
#         url = 'https://programmers.co.kr/job?job_position%5Bmin_career%5D=&amp;job_position%5Bjob_category_ids%5D%5B%5D=3&amp;job_position%5Bjob_category_ids%5D%5B%5D=10&amp;_=1593673591520'
#         driver = webdriver.Chrome(driver_path)
#         driver.get(url)
#         programmers_jobs = []
#         time.sleep(10)
#         datas = driver.find_elements_by_css_selector('li.list-position-item>div.item-body')
#
#         for com in datas :
#             name = com.find_element_by_css_selector('.company-name').text
#             position_name = com.find_element_by_css_selector('.position-title>a').text
#             url = com.find_element_by_css_selector('.position-title>a').get_property('href')
#             location = com.find_element_by_css_selector('.company-info>.location').text
#             min_career = com.find_element_by_css_selector('.company-info>.experience').text
#             programmers_jobs.append(ProgrammersInfo(name,position_name,url,location,min_career))
#
#
#         jobs_count = len(programmers_jobs)
#         response_text = '프로그래머스에서 찾은 {}개의 개발자 채용정보'.format(jobs_count)
#         for job in programmers_jobs :
#             response_text = response_text + '\n{} / {} / {}\n{}\n{}'.format(
#                 job.name, job.position_name, job.min_career, job.location, job.url)
#         driver.close()
#         return response_text
#
