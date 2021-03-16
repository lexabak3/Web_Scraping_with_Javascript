from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
import time
# import lxml
# import cchardet
import pandas as pd
import random


PARSE = True
NEED_LINKS = True

url = 'https://urbantoronto.ca/database/projects/'


if PARSE:
    print('Parse main page...')
    script = "document.querySelector('#database_load').click();"

    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)

    for x in range(1000):
        tmp = len(driver.find_elements_by_css_selector('.database-header-container'))
        driver.execute_script(script)
        time.sleep(4)
        if tmp == len(driver.find_elements_by_css_selector('.database-header-container')):
            print(f'Final count of elements - {tmp}')
            break

    html = driver.page_source
    driver.close()
    with open('html_file.html', 'w') as f:
        f.write(html)
else:
    print('Opening saved html file...')
    with open('html_file.html') as f:
        html = f.read()

# soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "lxml")

# Find links on main page or import from txt file
list_links = []
if NEED_LINKS:
    print('Find links on main page')
    for x in soup.find_all('div', class_="database-header-info-container"):
        tmp_a = x.find('a')
        if tmp_a is not None:
            list_links.append(tmp_a['href'])

    # Save link in file links.txt
    with open ('links.txt', 'w') as f:
        f.writelines(map(lambda line: line + '\n', list_links))
else:
    with open('links.txt', 'r') as f:
        list_links = [line.rstrip() for line in f.readlines()]

list_project_info = []
tmp_count = 0
# exit()

# Loading html snippets from link
print('Loading html snippets from links...')
pbar = tqdm(total=len(list_links))
while True:
    if len(list_links) > 0:
        url = list_links.pop()
        session = HTMLSession()
        tmp_project_info = False
        try:
            r = session.get(url)
            r.html.render(sleep=1)
            random.randint(0, 3)
            tmp_project_info = (r.html.find('.project-info'))
            session.close()
        except ConnectionRefusedError as error:
            print(error)
            session.close()
            time.sleep(45)
            list_links.append(url)
        except Exception as other_error:
            print(other_error)
            session.close()
            time.sleep(45)
            list_links.append(url)
        if tmp_project_info:
            pbar.update(1)
            list_project_info.append(tmp_project_info)
    else:
        pbar.close()
        break

# Parsing html tags: picking out the data you are looking for
print('Parsing html tags: picking out the data you are looking for...')
list_attr = []
for html_text in list_project_info:
    dict_attr = {}
    for element in html_text:
        data = [x.text for x in element.find('span')]
        dict_attr = {**dict_attr, **{data[0]: data[-1]}}
    list_attr.append(dict_attr)

# Saving data to an Excel table
print('Saving data to an Excel table')
df = pd.DataFrame(list_attr)
writer = pd.ExcelWriter('result_parse.xlsx', engine='xlsxwriter')
df.to_excel(writer, header=True, index=False)
writer.save()


