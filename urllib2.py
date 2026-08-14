import requests
from bs4 import BeautifulSoup
import time
from lxml import etree

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
print(soup.find(id="link3"))

links = soup.find_all('a')
for link in links:
    print(link.get('href'))

links = soup.select('p a.sister')
for link in links:
    print(link['href'])

print(soup.find_all('a',class_='sister'))
import re
print(soup.find_all(text=re.compile("Tillie")))

html = """
<html>
<head><title>网页标题</title></head>
<body>
<div class="content">
   <ul>
      <li class="item-0"><a href="link1.html">第一个</a></li>
      <li class="item-1"><a href="link2.html">第二个</a></li>
      <li class="item-2"><a href="link3.html">第三个</a></li>
      <li class="item-3"><a href="link4.html">第四个</a></li>
      <li class="item-4"><a href="link5.html">第五个</a></li>
   </ul>
</div>
</body>
</html>
"""
soup.title.string = "新标题"
soup.body.append(soup.new_tag('div',id='new_div'))
new_div = soup.find(id='new_div')
new_div.string = "这是新添加的div"
print(soup.prettify())

tree = etree.HTML(html)


li_elements = tree.xpath('//li')
print(f"共找到 {len(li_elements)} 个li元素")

links = tree.xpath('//a/@href')
print(links)

text = tree.xpath('//a/text()')
print(text)

items = tree.xpath('//li[@class="item-0"]')
for item in items:
    link = item.xpath('./a/text()')[0]
    href = item.xpath('./a/@href')[0]
    print(f"{link} -> {href}")

third_item = tree.xpath('//li[3]')
print(etree.tostring(third_item[0],encoding='utf-8').decode('utf-8'))

items = tree.xpath('//li[contains(@class, "item-")]')
print(f"匹配的元素数量:{len(items)}")


