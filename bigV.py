#-*-coding:utf8-*-

from login import *

class BigV():
	def __init__(self):
		pass

	def saveUids(self, results, filename):
		with open(filename, 'a') as f:
			for uid in results:
				uid = uid.split('&')[0] # remove '&type=0' in some strings
				f.write(uid+'\n')
		f.close()

	def parseHtml(self, url, filename):
		#print "in parseHtml url is: ", url
		res = session.get(url)
		content = res.text
		scripts=re.findall(r"<script>FM.view\((.*?)\)</script>", content, re.I) # get all parts tagged by script
		#scripts=re.findall(r"<script>STK && STK.pageletM && STK.pageletM.view\((.*?)\)</script>", content, re.I) # get all parts tagged by script
		js_content = scripts[-1] # extract the part containing big v info
		results = re.findall(r'usercard=\\\"id=(.*?)&refer_flag', js_content, re.I)
		#results = re.findall(r'usercard=\\\"id=(.*?)&', js_content, re.I)
		#print "results: ", results
		results = list(set(results)) # remove duplicates
		#results = [uid.split('&')[0] for uid in results]
		#self.saveUids(results, filename)
		with open(filename, 'a') as f:
			for line in results:
				uid = line.split('&')[0]
				f.write(uid+'\n')
		f.close()

	def getUids(self, url, filename):
		# read the first page and get page_num
		req = session.get(url)
		res = req.text
		numList = re.findall(r'page=(\d+)#', res, re.I)
		numList = [int(i) for i in numList]
		page_num = max(numList)
		print page_num
		#page_num = 174#100#20
		for pnum in range(1, page_num+1):
			furl = "%s?page=%s" % (url, str(pnum))
			self.parseHtml(furl, filename)