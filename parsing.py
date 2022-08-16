import requests
import json


def parsing(numbers: list) -> list:
    """Блок с парсингом карточек. В случае неудачи возвращает код ошибки"""
    URL_TEMLATE = 'https://apkdk.kaiten.ru/api/latest/cards/'
    task_name = []
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer cc1b7ae1-248a-4e09-9577-6fd3ad6f843f',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.4.731 Yowser/2.5 Safari/537.36'
        'x-'
    }

    for num in numbers:
        url = URL_TEMLATE + num
        get_r = requests.get(url, headers=headers)
        notification = 'Неизвестная ошибка'
        if get_r.status_code != 200:
            # task_name.append(f'!!! Карточка номер: #{num} - недоступна.')
            if get_r.status_code == 403:
                notification = 'Пространство/карточка недоступны'
            elif get_r.status_code == 401:
                notification = 'Неавторизованный доступ'
            elif get_r.status_code == 404:
                notification = 'запрашиваемой страницы не найдено'
            print(f'!!! Карточка номер: #{num} - недоступна. Код ошибки: {get_r.status_code}({notification})')
        else:
            ht = get_r.text
            obj = json.loads(ht)
            task_name.append(obj['title'] + f' (#{num})')
    return task_name
