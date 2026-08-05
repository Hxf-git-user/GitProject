import requests
from bs4 import BeautifulSoup

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5376.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" 
}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    print("请求成功!")
else:
    print("请求失败,状态码: ",response.status_code)
    exit()

soup = BeautifulSoup(response.text,"lxml")

title = soup.title.string
print("页面标题: ",title)

links = soup.find_all("a")
for link in links:
    href = link.get("href")
    text = link.string
    if text:
        print(f"链接文本:{text}, URL:{href}")

with open("badu_links.txt","w",encoding="utf-8") as f:
    for link in links:
        if link.string:
            f.write(f"{link.string}: {link.get('href')}\n")
print("数据已保存到 baidu links.txt")
print("modify files")