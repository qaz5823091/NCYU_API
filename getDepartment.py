import requests
import json
from bs4 import BeautifulSoup
# 美湯 package

url = 'https://web085003.adm.ncyu.edu.tw/pub_depta1.aspx'

data = []

with requests.Session() as session:
    post = session.post(url)
    post = post.text
    print(post)
    soup = BeautifulSoup(post, 'html.parser')
    option_tags = soup.find_all('option')
    with open('department.json', 'w') as file:
        for tag in option_tags:
            if tag.parent.get('name') == 'WebDep67':
                tmp = {
                    'id': tag.get('value'),
                    'content': tag.string.split()
                }
                data.append(tmp);
        json.dump(data, file, ensure_ascii = False)
