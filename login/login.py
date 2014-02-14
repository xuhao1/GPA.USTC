#!/usr/bin/python
import urllib,cv
import os

class session:
    def __init__(self,userCode="PB12203141",passWord="299792458",iden="000001"):
        initstr=urllib.urlencode({'userbz':'s'})
        initurl="http://mis.teach.ustc.edu.cn/userinit.do"
        self.wgetsavecookie(url=initurl,data=initstr,filepath="data/login.html")
        print "\n"
        checkCode=self.getCheckCode()
        loginpost=urllib.urlencode({"userbz":"s","hidjym":"","userCode":userCode,"passWord":passWord,"check":checkCode})
        loginpage="data/login.html"
        self.wgetloadcookie(url="http://mis.teach.ustc.edu.cn/login.do",data=loginpost,filepath=loginpage)
    def getCheckCode(self):
        #self.wgetloadcookie(url="http://mis.teach.ustc.edu.cn/randomImage.do",data="date='1491004419612'",filepath="data/test.gif")
        #cv.ShowImage("Check",cv.LoadImage('data/test.gif'))
        #checkCode=raw_input("Please Enter the CheckCode\n")
        #cv.DestroyAllWindows()
        self.wgetloadcookie(url="http://mis.teach.ustc.edu.cn/loadjym.do",filepath="data/check.txt")
        fp=open("data/check.txt","r")
        checkCode=fp.readline()
        print checkCode
        return checkCode
    def writePage(self,name,page):
        fileHandle = open (name, 'w' )
        fileHandle.writelines(page.readlines())
        fileHandle.close()
    def checkGPA(self):
        gpa="data/gpa.html"
        self.wgetloadcookie(url="http://mis.teach.ustc.edu.cn/querycjxx.do",data="xuenian=&chaxun=&px=1&zd=0",filepath="data/gpa.html")
    def wgetloadcookie(self,url,data="",cookie="data/cookie.txt",filepath=""):
        if filepath=="":
            os.system("wget '"+url+"?"+data+"' --load-cookies='"+cookie+"' --keep-session-cookies  ")
            return
        else:
            os.system("wget '"+url+"?"+data+"' --load-cookies='"+cookie+"' --keep-session-cookies  -O "+filepath)
            return
    def wgetsavecookie(self,url,data="",cookie="data/cookie.txt",filepath=""):
        if filepath=="":
            os.system("wget '"+url+"?"+data+"' --save-cookies='"+cookie+"' --keep-session-cookies  ")
            return
        else:
            os.system("wget '"+url+"?"+data+"' --save-cookies='"+cookie+"' --keep-session-cookies  -O "+filepath)
            return

test=session()
test.checkGPA()
