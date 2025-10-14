import requests
from bs4 import BeautifulSoup
import pycountry
def dato(zh):
    try:
        meet_headers = {
            'Referer': 'https://bincheck.io/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.get(f'https://bincheck.io/ar/details/{zh[:6]}', headers=meet_headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        table1 = soup.find('table', class_='w-full table-auto')
        rows1 = table1.find_all('tr')
        table2 = soup.find_all('table', class_='w-full table-auto')[1]
        rows2 = table2.find_all('tr')
        info = {}
        for row in rows1:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'العلامة التجارية للبطاقة':
                    info['brand'] = cell2_text.upper()
                elif cell1_text == 'نوع البطاقة':
                    info['card_type'] = cell2_text.upper()
                elif cell1_text == 'تصنيف البطاقة':
                    info['card_level'] = cell2_text.upper()
                elif cell1_text == 'اسم المصدر / البنك':
                    info['bank'] = cell2_text.upper()
        for row in rows2:
            cells = row.find_all('td')
            if len(cells) == 2:
                cell1_text = cells[0].text.strip()
                cell2_text = cells[1].text.strip()
                if cell1_text == 'اسم الدولة ISO':
                    info['country_name'] = cell2_text.upper()
                    country = pycountry.countries.get(name=info['country_name'])
                    info['flag'] = getattr(country, 'flag', "") if country else ""
                elif cell1_text == 'عملة البلد ISO':
                    info['currency'] = cell2_text.upper()
        brand = info.get('brand', 'UNKNOWN')
        card_type = info.get('card_type', 'UNKNOWN')
        card_level = info.get('card_level', 'UNKNOWN')
        bank = info.get('bank', 'UNKNOWN')
        country_name = info.get('country_name', 'UNKNOWN')
        country_flag = info.get('flag', '')
        mn = f'''[<a href="https://t.me/baba_coder">ϟ</a>] 𝗜𝗻𝗳𝗼 -> {brand} - {card_type} - {card_level}
        
[<a href="https://t.me/baba_coder">ϟ</a>] 𝗕𝗮𝗻𝗸 : {bank} - {country_flag}

[<a href="https://t.me/baba_coder">ϟ</a>] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 : {country_name} [ {country_flag} ]'''
        return mn
    except Exception as e:
        print(f"Error fetching BIN info: {e}")
        return 'No info'