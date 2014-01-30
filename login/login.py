#!/usr/bin/python
import urllib,urllib2,cookielib,cv
import os

class session:
    def __init__(self,userCode="PB12203141",passWord="299792458",iden):
        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        initstr=urllib.urlencode({'userbz':'s'})
        initurl="http://mis.teach.ustc.edu.cn/userinit.do"
        initpage=urllib2.urlopen(initurl,initstr)
        checkCode=self.getCheckCode()
        loginpost=urllib.urlencode({"userbz":"s","hidjym":"","userCode":userCode,"passWord":passWord,"check":checkCode})
        print loginpost
        loginpage=urllib2.urlopen("http://mis.teach.ustc.edu.cn/login.do",loginpost)
        self.writePage("login.do",loginpage)
        #cv.DestroyAllWindows()
    def getCheckCode(self):
        checkimage=urllib2.urlopen("http://mis.teach.ustc.edu.cn/randomImage.do?date='1491004419612'")
        fileHandle = open ( 'test.gif', 'w' )
        fileHandle.writelines(checkimage.readlines())
        fileHandle.close()
        cv.ShowImage("Check",cv.LoadImage('test.gif'))
        checkCode=raw_input("Please Enter the CheckCode\n")
        cv.DestroyAllWindows()
        return checkCode
    def writePage(self,name,page):
        fileHandle = open (name, 'w' )
        fileHandle.writelines(page.readlines())
        fileHandle.close()
    def checkGPA(self):
        gpa=urllib2.urlopen("http://mis.teach.ustc.edu.cn/querycjxx.do?xuenian=&chaxun=&px=1&zd=0")
        self.writePage("data/gpa.html",gpa)
    def wgetloadcookie(url,cookie="data/cookie.txt",filepath=""):
        if filepath="":
            os.system("wget "+url+"  --load-cookies="+cookie+" --keep-session-cookies  ")
            return
        else:
            os.system("wget "+url+"  --load-cookies="+cookie+" --keep-session-cookies  -O "+filepath)
            return
    def wgetsavecookie(url,cookie="data/cookie.txt",filepath=""):
        if filepath="":
            os.system("wget "+url+"  --save-cookies="+cookie+" --keep-session-cookies  ")
            return
        else:
            os.system("wget "+url+"  --save-cookies="+cookie+" --keep-session-cookies  -O "+filepath)
            return


