import requests
import json
import getpass
import time
from bs4 import BeautifulSoup
import string


def parsing(numbers: list) -> list:
    URL_TEMLATE = 'https://apkdk.flowfast.io/api/latest/cards/'
    task_name = []
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer debdb4c3-b062-4922-b097-e76d7587641d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / '
                      '98.0.4758.141 YaBrowser/22.3.2.644 Yowser/2.5 Safari/537.36 '
    }

    for num in numbers:
        url = URL_TEMLATE + num
        get_r = requests.get(url, headers=headers)
        if get_r.status_code != 200:
            task_name.append(f'!!! Карточка номер: #{num} - недоступна')
        else:
            ht = get_r.text
            obj = json.loads(ht)
            task_name.append(obj['title'] + f' (#{num})')
    return task_name
