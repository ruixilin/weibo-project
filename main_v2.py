#-*-coding:utf8-*-

from login import *
from bigV import *
from follower import *
from hotTweet import *
from mid import *
from publish import *
from autoComment import *
from datetime import datetime

# TODO: 每一个模块更加独立，每个模块可单独使用
# 所有用到的python文件加注释！！
if __name__ == '__main__':
	login = Login()
	#使用cookie登录，press c; else press l
	user_input = raw_input(u"使用cookie登录，请按c; 使用用户名密码登录，请按s： ".decode(code).encode('gbk'))
	while user_input not in ['s','S','c','C']:
		user_input = raw_input(u"使用cookie登录，请按c; 使用用户名密码登录，请按s： ".decode(code).encode('gbk'))
	print "user input ", user_input
	if user_input in ['s','S']:
		login.loginSimulation()
	elif len(os.listdir('cookies')) == 0:
		print "Empty folder!"
		login.loginSimulation()
	with open('login_users.txt') as f:
		start_page = 0
		for user in f.readlines():
			user = user.strip('\n')
			login.loginWithCookies(user)
			# 执行用户信息爬取模块+发评论模块（爬取用户博文等有用信息模块未添加）
			now = datetime.now()
			today = now.strftime('%Y%m%d')		# 大写Y：2016 小写y: 16
			fn1 = 'commenters/commenters_'+today+'.txt'		# 评论者uid列表文件
			hotTweet = HotTweet()
			with open('urls_by_keywords.txt') as fp:		# 目前为人工筛选出的分类热门博文链接
				for line in fp.readlines():
					url = line.strip('\n').split()[0]
					hotTweet.crawlCommenters(url, fn1)
			fp.close()
			fn3 = hotTweet.removeDuplicates(fn1)	# 去重后的评论者uid列表文件		
			fn2 = 'mids/mids_'+today+'.txt'		#用户最新博文mid文件
			mid = Mid()
			mid.getMids(fn3, fn2)
			commenter = AutoComment()
			flag = commenter.comment(fn2, 'ad.txt', user)		# ad.txt 广告语文件
			if flag[0]=='editfailure':
				print "该账号发送评论过于频繁，已被禁！转到下一账号".encode('gbk', 'ignore')
				start_page = flag[1]
				continue
			else:
				break	
	f.close()