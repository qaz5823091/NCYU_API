import requests
import json
import urllib
from bs4 import BeautifulSoup

departments = requests.get('https://www.cppwebs.ga/NCYU_Class/department.json')
departments = departments.json()


#url = 'https://web085003.adm.ncyu.edu.tw/pub_schta2.aspx?'
#parameter = 'WebYear1=109&WebTerm1=2&PkwCno9=34700025'

data = []


with open('classOfDepartment.json', 'w') as file:
    id = 1
    for department in departments:
        url = 'https://web085003.adm.ncyu.edu.tw/pub_depta2.aspx?'
        parameter = 'WebPid1=&Language=zh-TW&WebYear1=109&WebTerm1=2&WebDep67=' + department['id']
        with requests.Session() as session:
            get = session.get(url + parameter)
            plainHtml = get.text
            soup = BeautifulSoup(plainHtml, 'html.parser')
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
                        'select-type': rows[0],
                        'class-type': rows[1],
                        'class-name': rows[4],
                        'department': rows[6],
                        'system': rows[7],
                        'academy': rows[8],
                        'grade': rows[11],
                        'course-type': rows[13],
                        'scores': rows[14],
                        'remark': rows[18],
                        'teacher': rows[19],
                        'week': rows[20],
                        'session': rows[21],
                        'classroom': rows[22],
                        'campus': rows[23]
                    }
                    data.append(tmp)
                    id += 1
                    print(id)
    json.dump(data, file, ensure_ascii = False)
