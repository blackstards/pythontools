import json
import time
import os
import random
import requests
from json import dumps, loads
from bs4 import BeautifulSoup


class 编程猫API(object):
	def __init__(self, UA='Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', debug=False):
		self.debug = debug
		self.ses = requests.session()
		self.headers = {"Content-Type": "application/json", "User-Agent": UA}

	def 登录(self, identity, password):
		soup = BeautifulSoup(requests.get(
			'https://shequ.codemao.cn', headers=self.headers).text, 'html.parser')
		pid = loads(soup.find_all("script")[0].string.split("=")[1])['pid']
		a = self.ses.post('https://api.codemao.cn/tiger/v3/web/accounts/login', headers=self.headers,
		                  data=dumps({"identity": identity, "password": password, "pid": pid}))
		if a.status_code == 200:
			self.提示('登录成功', a)
		else:
			self.提示('登录失败', a)

	def 提示(self, *msg):
		if self.debug:
			print(*msg)

	def 点赞(self, workID):
		a = self.ses.post(
			f'https://api.codemao.cn/nemo/v2/works/{workID}/like', headers=self.headers, data='{}')
		if a.status_code == 200:
			print('点赞成功', a)
		else:
			print('点赞失败', a)

	def 点评(self, workID, work):
		a = self.ses.post(f'https://api.codemao.cn/creation-tools/v1/works/{workID}/comment',
		                  headers=self.headers, data=dumps({"emoji_content": "", "content": work}))
		if a.status_code == 201:
			print('点评成功', a)
		else:
			print('点评失败', a)

	def 存储(self):
		with open("ID数据库.txt", "a") as f:
			f.write("\n"+str(数据['items'][i]['work_id']))
			f.close()

	def 收藏(self, workID):
		a = self.ses.post(
			f'https://api.codemao.cn/nemo/v2/works/{workID}/collection', headers=self.headers, data='{}')
		if a.status_code == 200:
			print('收藏成功', a)
		else:
			print('收藏失败', a)

	def 关注(self, userID):
		a = self.ses.post(
			f'https://api.codemao.cn/nemo/v2/user/{userID}/follow', headers=self.headers, data='{}')
		if a.status_code == 204:
			print('关注成功', a)
		else:
			print('关注失败', a)


print('欢迎使用速刷编程猫工具')
zhanghao = input("你的编程猫账户：")
mima = input("你的编程猫密码：")
for __count in range(20000):
	账号 = zhanghao, zhanghao, zhanghao
	AI = 编程猫API(debug=True)
	AI.登录(random.choice(账号), mima)
	数据 = requests.get(
		"https://api.codemao.cn/creation-tools/v1/pc/discover/newest-work?offset=0&limit=5")
	数据 = 数据.text
	数据 = json.loads(数据)
	for i in range(5):
		print(i+1)
		with open("ID数据库.txt", 'r') as f:
			ID库 = f.read().splitlines()
		print(数据['items'][i]['work_id'])
		if (str(数据['items'][i]['work_id']) in ID库):
			print('已点评，跳过')
		else:
			with open("词库.txt", 'r') as f:
				词库 = f.read().splitlines()
			特殊词库 = ["Hi~训练师！这个作品很有潜力呢~祝你早日首页！", "你好哇~训练师！我从神秘人那里得知一个小秘密！作品的素材精美，可玩性高，运行流畅，就可以上首页了呐！", "哇！"+str(数据['items'][i]['work_name'])+"很有潜力！只要再优化优化说不定就能上首页辣！","咕咚！这里掉出了一个优秀作品呢~很喜欢呢！我在首页推荐等你~","Hi~我是源码世界的代码喵~这个作品值得点赞！希望你在源码世界的道路上越走远越远~","喵呜~在不起眼的角落里发现了一个很棒的作品呢！希望"+str(数据['items'][i]['work_name']) +"早日首页辣~",str(数据['items'][i]['nickname'])+"好棒鸭~是一个很有潜力的训练师呢！祝你编程水平越来越高~"]
			AI.点赞(数据['items'][i]['work_id'])
			AI.收藏(数据['items'][i]['work_id'])
			AI.关注(数据['items'][i]['user_id'])
			词库类型 = random.randint(1, 2)
			if (词库类型 == 1):
				AI.点评(数据['items'][i]['work_id'], random.choice(特殊词库))
				AI.存储()
				time.sleep(5)
			else:
				AI.点评(数据['items'][i]['work_id'], random.choice(词库))
				AI.存储()
				time.sleep(5)
