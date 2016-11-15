#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

#潜客获取
def crawlUid(keyword):
	print keyword	

#选择uid文件（路径）
def loadUid(filename):
	print filename

#广告推送
def pushAd():
    print 'pushAd'

#结果追踪
def analyzeResult():
    print 'analyzeResult'

root = Tk()
root.title("基于网络爬虫技术对特定微博用户群发送产品信息的自动推送广告系统")
#root.geometry('300x200')

Label(root, text='基于网络爬虫技术对特定微博用户群发送产品信息的自动推送广告系统', font=('宋体', 40), bg='#f173ac', fg='#feeeed').pack(expand = YES, fill = BOTH)

wholefrm = Frame(root)

#button1 - 潜客获取
frm1 = Frame(wholefrm)
Label(frm1, text='请选择希望获取的目标客户类别', font=('宋体', 20), bg='#65c294', fg='#feeeed').pack(expand = YES, fill = BOTH)		
frm1_T1 = Frame(frm1,width=400, height=20).pack(side = TOP, expand = YES, fill = BOTH)
#left
frm1_L = Frame(frm1)
keyword = '理财'
variable = StringVar()
variable.set('理财') # default value        
om = OptionMenu(frm1_L, variable, '理财', '贷款').pack(side=TOP)
frm1_L.pack(side=LEFT)
#right
frm1_R = Frame(frm1)
Button(frm1_R,width=10, height=2, text = '潜客获取', font = ('宋体', 20),command = lambda : crawlUid(keyword)).pack()
frm1_R.pack(side=RIGHT)
frm1.pack(side=TOP)
frm1_T2 = Frame(wholefrm,width=400, height=20).pack(side = TOP, expand = YES, fill = BOTH)

#button2 - 查找uid文件
frm2 = Frame(wholefrm, bg='#feeeed')
Label(frm2, text='请选择潜客uid列表文件路径', font=('宋体', 20), bg='#65c294', fg='#feeeed').pack()		
frm2_T1 = Frame(frm2,width=400, height=20, bg='#feeeed').pack(side = TOP, expand = YES, fill = BOTH)
# TODO: 显示找到的文件路径
fUid = 'some uid path'
Button(frm2, width=10, height=2, text = 'uid文件加载', font = ('宋体', 20, 'normal'),command = lambda : loadUid(fUid)).pack(side=TOP)
frm2_T2 = Frame(frm2,width=400, height=20, bg='#feeeed').pack(side = TOP, expand = YES, fill = BOTH)
frm2.pack(side=TOP,expand = YES, fill = BOTH)

#button3 - 使用广告语料库中的文案对已选定用户发送推广信息
frm3 = Frame(wholefrm, bg='white')
Label(frm3, text='对已选定的用户推送广告文案语料库中的该类别信息', font=('宋体', 20), bg='#65c294', fg='#feeeed').pack(side = TOP)
frm3_T1 = Frame(frm3, width=400, height=20).pack(side = TOP, expand = YES, fill = BOTH)	
Button(frm3, width=10, height=2,text = '评论推送', font = ('宋体', 20, 'normal'),command = pushAd).pack(side = TOP)
frm3_T2 = Frame(frm3, width=400, height=20).pack(side = TOP, expand = YES, fill = BOTH)
frm3.pack(side=TOP,expand = YES, fill = BOTH)

#button4 - 结果分析
frm4 = Frame(wholefrm, bg='#feeeed')
Label(frm4, text='推送后的结果追踪，如成功推送人数，点击率，转化率等', font=('宋体', 20), bg='#65c294', fg='#feeeed').pack(side = TOP)		
frm4_T1 = Frame(frm4, width=400, height=20, bg='#feeeed').pack(side = TOP, expand = YES, fill = BOTH)	
Button(frm4, width=10, height=2,text = '结果追踪', font = ('宋体', 20, 'normal'),command = analyzeResult).pack(side = TOP)
frm4_T2 = Frame(frm4, width=400, height=20, bg='#feeeed').pack(side = TOP, expand = YES, fill = BOTH)	
frm4.pack(side=TOP,expand = YES, fill = BOTH)


wholefrm.pack(expand = YES, fill = BOTH)
root.mainloop()

