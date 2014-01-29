#!/bin/bash
rm -r data
mkdir data
wget http://mis.teach.ustc.edu.cn/userinit.do urllib2.urlopen--save-cookies=data/cok.txt --keep-session-cookies -O data/userinit.html
wget http://mis.teach.ustc.edu.cn/randomImage.do\?date\='1491004419612' --load-cookies="data/cok.txt" -O data/check.gif 
read -p "Please Enter Check" check
echo"Check Read Successful\n"
wget http://mis.teach.ustc.edu.cn/login.do --post-data="userbz=s&userCode=PB12203141&passWord=299792458&check=$check" --load-cookies="data/cok.txt" -O data/login.do
mvim data/login.do
