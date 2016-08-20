# coidng: utf8
import requests
from lxml import etree
import sys
import re
import time
import os
import zipfile
import getopt

def downloadImageFile(imgUrl):  
    local_filename = imgUrl.split('/')[-1]  
    print "Download Image File=", local_filename  
    r = req.get(imgUrl, stream=True) # here we need to set stream = True parameter  
    with open(local_filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk: # filter out keep-alive new chunks  
                f.write(chunk)  
                f.flush()  
        f.close()  
    return local_filename

def download_pics(url):
	index = etree.HTML(req.get(url).text)
	all_subURL = index.xpath('//*[@id="gh"]/div/a')
	title = index.xpath('//*[@id="gn"]/text()')
	title = title[0]
	path = cleanPath(title)
	dir(title)
	picurl = all_subURL[0].attrib['href']
	nexturl = None
	while picurl != nexturl:
		if nexturl != None:
			picurl = nexturl
		txt = req.get(picurl).text
		page1 = etree.HTML(txt)
		page2 = etree.HTML(txt)
		img = page1.xpath('//*[@id="sm"]')
		mixurls = page2.xpath('//*[@id="ia"]/table[1]/tr/td[3]/a')
		for url in mixurls :
			if url.text == 'Next Page >':
				nexturl = url.attrib['href']
				pass
		time.sleep(5)
		downloadImageFile(img[0].attrib['src'])
	os.chdir('..')
	zip_dir(path, path+'.zip')
	pass

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()

def cleanPath(path):
	path=path.strip()
	path = path.replace('.', '')
	path = path.replace('|', '')
	path = path.replace(':', '')

def dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
	os.chdir(path)


if __name__ == '__main__':
	req = requests.session()
	req.headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	    'Accept-Encoding': 'gzip, deflate',
	    'Referer': 'http://www.baidu.com',
	    'Connection': 'keep-alive',
	    'Cache-Control': 'max-age=0',
	}

	try:
		options,args = getopt.getopt(sys.argv[1:],"u:p:",["url=","proxy="])
	except getopt.GetoptError:
		sys.exit()

	for name,value in options:
		if name in ("-u","--url"):
			url = value
		if name in ("-p","--proxy"):
			proxy = value
			req.proxies = {
				'http': proxy,
			}
	if url is None:
		# get_index = req.get(url)
		# print(get_index.text)
		print('No Url')
	else :
		download_pics(url)
