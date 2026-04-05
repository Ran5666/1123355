import requests
import json

# 1. 設定氣象署 API 網址
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001'

# 2. 設定參數
params = {
    'Authorization': 'CWA-428BB12E-42E5-4F87-A87E-6CCA7F286FA7', # 你的完整授權碼
    'locationName': '桃園市'
}

# 3. 發送 GET 請求
response = requests.get(url, params=params, verify=False)

# 4. 檢查是否成功
if response.status_code == 200:
    data = response.json() # 把回傳的資料轉成 JSON 物件
    
    # 存成 JSON 檔案
    with open('taoyuan_weather.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("✅ 氣象資料抓取成功！已儲存為 taoyuan_weather.json")
else:
    print(f"❌ 抓取失敗，狀態碼：{response.status_code}")