#!/usr/bin/python
# -*- coding: utf8 -*-
import requests
from lxml import etree
import sys
import time
import os
import zipfile
import getopt
import re

req = requests.session()
req.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}


def clean_path(path):
    path = path.strip()
    path = path.replace('.', '')
    path = path.replace('|', '')
    path = path.replace(':', '')
    path = path.replace(' ', '')
    path = re.sub('[^0-9a-zA-Z]', '', path)
    if len(path) > 255:
        path = str(time.ctime())
    return path


def zip_dir(dir_name, zipfile_name):
    file_list = []
    if os.path.isfile(dir_name):
        file_list.append(dir_name)
    else:
        for root, dirs, files in os.walk(dir_name):
            for the_name in files:
                file_list.append(os.path.join(root, the_name))
    zf = zipfile.ZipFile(zipfile_name, "w", zipfile.zlib.DEFLATED)
    for tar in file_list:
        zf.write(tar, tar[len(dir_name):])
    zf.close()


def download_image_file(img_url):
    local_filename = img_url.split('/')[-1]
    print "Download Image File=", local_filename
    r = req.get(img_url, stream=True)  # here we need to set stream = True parameter
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename


def download_pics(gallery_url, zip_file=True, callback=None):
    try:
        index = etree.HTML(req.get(gallery_url).text)
        all_sub_urls = index.xpath('//*[@id="gh"]/div/a')
        title = index.xpath('//*[@id="gn"]/text()')
        title = title[0]
        path = clean_path(title)
        if path is None:
            path = str(time.time())
        dir_path(path)
        pic_url = all_sub_urls[0].attrib['href']
        next_url = None
        while pic_url != next_url:
            if next_url is not None:
                pic_url = next_url
            txt = req.get(pic_url).text
            page1 = etree.HTML(txt)
            page2 = etree.HTML(txt)
            img = page1.xpath('//*[@id="sm"]')
            mix_urls = page2.xpath('//*[@id="ia"]/table[1]/tr/td[3]/a')
            for gallery_url in mix_urls:
                if gallery_url.text == 'Next Page >':
                    next_url = gallery_url.attrib['href']
                    pass
            time.sleep(1)
            try:
                download_image_file(img[0].attrib['src'])
            except Exception, e:
                print e
        os.chdir('..')
        if zip_file:
            zip_dir(path, path + '.zip')
        return True
    except Exception, e:
        print e
        return False


def dir_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "u:p:", ["url=", "proxy="])
    except getopt.GetoptError:
        sys.exit()
    input_gallery_url = ""

    for name, value in options:
        if name in ("-u", "--url"):
            input_gallery_url = value
        if name in ("-p", "--proxy"):
            proxy = value
            req.proxies = {
                'http': proxy,
            }
    if input_gallery_url is None:
        # get_index = req.get(url)
        # print(get_index.text)
        print('No Url')
    else:
        download_pics(input_gallery_url)
