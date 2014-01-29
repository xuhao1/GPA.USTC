#USTC教务系统API总结
##初始界面
	URL
		http://mis.teach.ustc.edu.cn/
	COOKIE
		JSESSIONID
##登陆界面

	URL
		http://mis.teach.ustc.edu.cn/userinit.do 
	POST
		userbz=s
	验证码图片：
		http://mis.teach.ustc.edu.cn/randomImage.do?date='1491004419612'
		src = "randomImage.do?date"+Math.random()*(100);
	Request COOKIE:
		none
	COOKIE
		JSESSIONID	
##登陆动作
	URL
		http://mis.teach.ustc.edu.cn/login.do
	POST:
	userbz=s
	hidjym:
	userCode:PB12203141
	passWord:299792458
	check:K8af
	COOKIE
		JSESSIONID
##成绩查询
###Request URL:
http://mis.teach.ustc.edu.cn/querycjxx.do
###Request Method:POST
	xuenian:
		NULL表示所有
		2012(1,2,3)
		1为秋季学期2，为次年
	bjg:on/null
	chaxun:anything is ok
	px:1
	zd:0