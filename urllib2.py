#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cookielib
import urllib2

url = "http://www.baidu.com"
responsel = urllib2.urlopen(url)
print "第一种方法"
print responsel.getcode()
print len(responsel.read())

print "第二种方法"
request = urllib2.Request(url)

request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)

print response2.getcode()

