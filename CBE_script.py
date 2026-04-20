import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# 1. تعريف الرابط والهوية (Variables)
url = "https://www.cbe.org.eg/ar/economic-research/statistics/exchange-rates"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(" جاري طلب الصفحة من البنك المركزي...")

# 2. طلب الصفحة من الإنترنت
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 3. تحليل محتوى الصفحة
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 4. البحث عن الجدول
    table = soup.find('table')
    rows = table.find_all('tr')
    
    all_data = []

    # 5. اللف على الصفوف واستخراج البيانات
    for row in rows[1:]:  # تخطي العنوان
        cols = row.find_all('td')
        if len(cols) >= 3:
            currency_info = {
              'Currency': cols[0].text.strip(),
              'Buy': float(cols[1].text.strip().replace(',', '')),
              'Sell': float(cols[2].text.strip().replace(',', '')),
              'Extraction_Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            spread = round(currency_info['Sell'] - currency_info['Buy'], 4)
            currency_info['Spread'] = spread
            all_data.append(currency_info)

    # 6. تحويل البيانات لجدول وحفظها
    df = pd.DataFrame(all_data)
   # filename = "cbe_simple_rates.csv"
    filename = f"cbe_rates_{datetime.now().strftime('%H%M%S')}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    
    
    print(f"تم بنجاح! البيانات حفظت في ملف: {filename}")
    print(df) # عرض النتيجة في الشاشة

else:
    print(f" فشل الاتصال بالموقع. كود الخطأ: {response.status_code}")