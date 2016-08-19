# coidng: utf8
import requests
import sys
from lxml import etree
import wget
import re
import time
import os

def download_pics(url, headers):
	index = etree.HTML(requests.get(url, headers=headers).text)
	all_subURL = index.xpath('//*[@id="gh"]/div/a')
	title = index.xpath('//*[@id="gn"]/text()')
	title = title[0]
	dir(title)
	# print all_subURL
	# u = all_subURL[0]
	# print u
	# picurl = re.match(r'http://lofi.e-hentai.org/s/[A-Za-z0-9]+/[A-Za-z0-9]+', u)
	picurl = all_subURL[0].attrib['href']
	# print picurl
	nexturl = None
	while picurl != nexturl:
		if nexturl != None:
			picurl = nexturl
		txt = requests.get(picurl, headers=headers).text
		# print txt.encode('utf8')
		page1 = etree.HTML(txt)
		page2 = etree.HTML(txt)
		img = page1.xpath('//*[@id="sm"]')
		mixurls = page2.xpath('//*[@id="ia"]/table[1]/tr/td[3]/a')
		for url in mixurls :
			if url.text == 'Next Page >':
				nexturl = url.attrib['href']
				pass
		# print nexturl
		time.sleep(5)
		wget.download(img[0].attrib['src'])
	pass

def dir(path):
	path=path.strip()
	path = path.replace('.', '')
	path = path.replace('|', '')
	# path=path.rstrip("\\")
	# delset = path.punctuation
	# path = line.translate(None,delset)
	if not os.path.exists(path):
		os.makedirs(path)
	os.chdir(path)
	# return path


if __name__ == '__main__':
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	    'Accept-Encoding': 'gzip, deflate',
	    'Referer': 'http://www.baidu.com',
	    'Connection': 'keep-alive',
	    'Cache-Control': 'max-age=0',
	}
	url = sys.argv[1]
	if url is None:
        # print "The Url Can NOT Be Nil"
		get_index = requests.get(url, headers=headers)
		# print get_index.text
	else :
		download_pics(url, headers)

