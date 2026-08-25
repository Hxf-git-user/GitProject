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