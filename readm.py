# -*- coding: utf-8 -*-
import poplib
import getpass

#Mailbox = poplib.POP3_SSL('pop.qq.com', '995')

M = poplib.POP3_SSL('pop.qq.com', '995')
M.user('2171947603@qq.com')
M.pass_('dcplburlheiseagc')
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)
# 退出
M.quit()