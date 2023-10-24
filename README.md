# getGithubTrendingToday
getGithubTrendingToday-to-email

使用gitHub Actions，每天获取github-Trending信息，发送到邮箱！

2023-10-24新增项目说明支持中英文

![fcf30948-3be8-408a-9b1e-252b91de1e72](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/5c2445b7-e2de-4b06-a06d-8833658456e1)


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

![xxxxxxsda](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/b2eb468c-9d89-426a-a7aa-a7a34434d196)


### 3.效果

![IMG_20230913_173400](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/6a31750a-9f85-4c45-a683-f8d30619f1c8)

# ----------------end

thanks!

![IMG_20230913_190002](https://github.com/SEAHAISEA/getGithubTrendingToday/assets/50478918/37294956-9bbe-423d-8275-f3e11264533b)
