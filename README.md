# getGithubTrendingToday
getGithubTrendingToday-to-email

使用gitHub Actions，每天获取github-Trending信息，发送到邮箱！

### 1.准备两个邮箱

（QQ邮箱示例）<br>
1.准备两个邮箱号，一发一收。<br>
2.获取QQ邮箱授权码（发送的那个）<br>
3.微信接收（QQ邮箱提醒功能）<br>

![1680939572-594195](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/9865a416-98be-4dd3-bbe6-d3980804eb7f)

### 2.创建一个私有仓库
1.下载几个文件or复制内容<br>
2.修改getGithubTrending.py中的：<br>

	# 邮件配置
	smtp_server = 'smtp.qq.com'#邮箱服务端
	smtp_port = 465#邮箱端口
	sender_email = 'xxxx'#发送邮箱
	sender_password = 'xxxx'#发送邮箱的授权码
	receiver_email = 'xxxx'#接收邮箱

 3.上传getGithubTrending.py，requirements.txt两个文件到仓库中<br>

 4.创建gitHub Actions

![appp](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/f6f3bbe9-2308-4546-9fb8-d21aab279f1b)

5.复制getGithubTrending.yml中的内容

### 3.效果

![IMG_20230913_173400](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/6a31750a-9f85-4c45-a683-f8d30619f1c8)

# ----------------end

thanks!

![IMG_20230913_190002](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/37294956-9bbe-423d-8275-f3e11264533b)
