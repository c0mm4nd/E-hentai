# E-Hentai

Pic Downloader  for Lofi.E-hentai based on Python 2.7

# Version 0.0.2

0.0.1: init project

0.0.2：change arguments in CLI, add autozip function, add http proxy

0.0.3: fix some bugs & fit the web interface

# 使用方法-Win32GUI(Windows下可视化界面版)

本版本**无**浏览功能，要浏览的看下面web版。

1. 打开https://github.com/maoxs2/e-hentai/releases

2. 下载最新release包（dist_\*.\*.\*-win32.zip ）

3. 解压缩后摁那个exe就会真相大白


# 使用方法-Web(网页版)

本版本仍为**beta**版，性能界面等TODO现请勿吐槽。

1. 先荡下来 `git clone https://github.com/maoxs2/E-Hentai `

2. 进入项目文件夹 `cd E-hentai `

3. 然后安装依赖（lxml、requests、webpy（web用）、tk（win32用）） 

    win下：

    如果是64位python27: `pip install -r requirements/requirement_64.txt` 
    
    如果是32位python27：`pip install -r requirements/requirement_32.txt`

    linux下:

    想必你动手能力比较强，直接自己pip或apt吧

4. `python webInterface/app.py ` 然后到http://localhost:8080下看看吧~

# 使用方法-CLI(命令行版)

example：`python ehentai.py -u http://lofi.e-hentai.org/g/750140/8afd88daa3/ -p http://127.0.0.1:1080`

1. 上lofi.e-hentai.org找自己喜欢的本子

2. 复制本子封面的链接，如……为了不暴露喜好我们用http://XXX/XXX表示

3. `python ehentai.py -u http://XXX/XXX [ -p http代理 ] `

4. 自己看目录

# 说明

做这个真伤肾……

自己翻墙

自用脚本不喜勿喷

由于e绅士不喜欢爬虫故增加了请求间隔（sleep），嫌慢就改小，被ban不负责（

咳咳我又把sleep改小了……
