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
		http://mis.teach.ustc.edu.cn/randomImage.do?date='..........'
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