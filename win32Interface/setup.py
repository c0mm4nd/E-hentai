# coding: utf8
from distutils.core import setup 
import py2exe
import sys
sys.path.append("..")

# 由于lxml, setup命令：python setup.py py2exe -p lxml
includes = [
	"ehentai",
]
setup(windows=["app.py"])
