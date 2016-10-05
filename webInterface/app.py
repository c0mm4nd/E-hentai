# -*- coding:utf8 -*-
import sys
import web
import os
sys.path.append("..")
import ehentai
from urllib import unquote,quote
reload(sys)
sys.setdefaultencoding( "utf-8" )

render = web.template.render('templates')
urls = (
    "/", "index",
    "/gallery/(.*)", "gallery"
)


class index:
    def GET(self):
        galleries = os.listdir("static/gallery")
        if "url" in web.input():
            # print "test1"
            current_dir = os.getcwd()
            os.chdir("static/gallery")
            path_name = ehentai.download_pics(web.input().url, zip_file=False)
            os.chdir(current_dir)
            url = web.input().url
            return render.index(url, galleries, quote, str)
        else:
            # print "test2"
            url = None
            return render.index(url, galleries, quote, str)


class gallery:
    def GET(self, path):
        path = unquote(path)
        gallery_path = "static/gallery/%s" % path
        print gallery_path
        current_dir = os.getcwd()
        # os.chdir(gallery_path)
        list = []
        os.chdir(current_dir)
        for i in os.walk("./" + gallery_path):
            list = i[2]
        return render.gallery(path, list, quote, str)


app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()
