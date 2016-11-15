#:-*-coding:utf8-*-
'''
@author:ruixilin
'''
import os
from datetime import datetime
import re
'''
	分析log, 评论发送成功率
'''
class Log:
	def __init__(self):
		now = datetime.now()
		self.today =now.strftime('%Y%m%d')

	def logAnalysis(self, logFile):
		
		success = 0
		with open(logFile) as f:
			lines = f.readlines()
			total = len(lines)
			for line in lines:
				if line.strip('\n').split()[-1] == 'SUCCESS':
					success += 1 
		f.close()
		with open('log/result_'+self.today+'.txt', 'a') as f:
			f.write('total sent:\t%s\tcomments published:\t%s\n'%(total, success))
		f.close()

	def sumOfElements(self, res):
		total = []
		success = []
		with open(res) as f:
			lines = f.readlines()
		f.close()
		for line in lines:
			total += re.findall(r'total sent:\t([0-9]+)\t', line, re.I)
			success += re.findall(r'comments published:\t([0-9]+)\n', line, re.I)
		total = map(int, total)
		success = map(int, success)
		with open('log/result_'+self.today+'.txt', 'a') as f:
			f.write('==================================SUMMARY===================================\n')
			f.write('total sent:\t%d\tcomments published:\t%d\n'%(sum(total),sum(success)))
		f.close()

if __name__ == '__main__':
	log = Log()
	user_input = ''
	filename = ''
	while user_input.lower() not in ['loganalysis','sumofelements','l','s']:
		user_input = raw_input('Please choose an operation: logAnalysis(L), sumOfElements(S): ')
	while not os.path.exists(filename):
		filename = raw_input('Please enter filename here: ')	# raw_input:abc input:'abc'
	if user_input.lower() in ['sumofelements','s']:
		log.sumOfElements(filename)
	else:
		log.logAnalysis(filename)