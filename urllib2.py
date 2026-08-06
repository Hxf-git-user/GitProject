import requests
from bs4 import BeautifulSoup
import time

def simple_crawler(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        #发送请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # 检查请求是否成功

        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取标题
        title = soup.title.string if soup.title else "No title found"

        # 提取描述(如果有meta description标签)
        description = "No description found"
        description_tag = soup.find('meta',attrs={'name':'description'})
        if description_tag and 'content' in description_tag.attrs:
            description = description_tag['content']

        #返回结果
        return {
            'url': url,
            'title': title,
            'description': description,
            'status': 'success'
        }
    except requests.exceptions.HTTPError as err:
        return {'url': url, 'status': f"HTTP Error: {err}"}
    except requests.exceptions.ConnectionError:
        return {'url': url, 'status': "Connection Error"}
    except requests.exceptions.Timeout:
        return {'url': url, 'status': "TImeout Error"}
    except requests.exceptions.RequestException as err:
        return {'url': url, 'status': f"Error:{err}"}
    

# 测试函数
urls_to_crawl = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.wikipedia.org'
]

for url in urls_to_crawl:
    result = simple.crawler(url)
    print(f"\nCrawling: {result['url']}")

    if result['status'] == 'success':
        print(f"Title: {result['title']}")
        print(f"Description: {result['description']}")
    else:
        print(f"Failed: {result['status']}")

    time.sleep(1)

html_doc = """
<html>
<head><title>网页标题</title></head>
<body>
<p class="story">从前有三个人:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>和
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
他们住在井底.</p>
</head>
</html>
"""

soup = BeautifulSoup(html_doc,'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))

