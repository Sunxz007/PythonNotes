'''
@Description: 
@Author: 孙晓昼
@since: 2019-10-28 17:11:47
@LastEditors: 孙晓昼
@LastEditTime: 2019-10-28 17:17:31
'''
age =int(input("请你输入狗狗的年龄"))
print('')
if age<=0:
    print("你是在逗我吧!")
elif age==1:
    print("相当于 14 岁的人。")
elif age==2:
    print("相当于 22 岁的人。")
elif age > 2:
    human=22+(age-2)*5
    print('对应人类年龄：',human)
# 退出提示
input('点击 enter 键退出')