import requests
import json
import urllib
import re
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose

data = []



with open('temp.json', 'w') as file:
    id = 643
    for grades in range(1,4):
        url = 'https://web085003.adm.ncyu.edu.tw/pub_clata4.aspx?'
        parameter = 'Language=zh-TW&WebYear1=109&WebTerm1=2&WebPDC99=通識教育課程(含90學年度以前共同必修科目)&WebDomainNo1=0159:通識教育選修選項：通識領域課程&WebCrsGrade1=' + str(grades)

        with requests.Session() as session:
            get = session.get('http://localhost/temp.html')
            get.encoding = 'utf-8'
            plainHtml = get.text
            print(plainHtml)
            soup = BeautifulSoup(plainHtml, 'html.parser')
            soup.encoding = 'utf-8'
            tr_tags = soup.find_all('tr')
            for tag in tr_tags:
                rows = tag.find_all('td')
                catch = False
                for x in rows:
                    color = x.get('bgcolor')
                    if color == 'ECE987' or color == 'E9D3D1':
                        catch = True
                        break
                if catch:
                    rows = [ x.text.strip() for x in rows ]
                    tmp = {
                        'id': id,
                        'class-name': rows[2],
                        'system': rows[5],
                        'grade': rows[9],
                        'course-type': rows[11],
                        'scores': rows[12],
                        'remark': rows[16],
                        'teacher': rows[17],
                        'week': rows[18],
                        'session': rows[19],
                        'classroom': rows[20],
                        'campus': rows[21]
                    }
                    data.append(tmp)
                    id += 1
                    print(id)
    json.dump(data, file, ensure_ascii = False)
