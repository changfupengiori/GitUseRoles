'''
author:changfp
date:20210111
remark:
1、演示github如何使用
'''
class BaseClass():
    def __init__(self):
        pass
    def show(self,a='默认值参数'):
        print("我是第一个开发人员编写的方法"+'fixA修改这个位置目的造成冲突')
        #修复补丁的时候修改了这个位置同时修改了参数
        print("第三个人在此修复bug。同传参："+a)

cc=BaseClass()
cc.show()