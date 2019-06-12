# noinspection PyInterpreter
"""
测试开发面试题解（1）-整数反转

题目描述:
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例1:
输入: 123、-123负数、120有零的情况
输出: 321、-321、21
"""
import math  #math.pow(x,y) 就是计算x的y次方
class Function():
    def one(self,num):
        if abs(num)<math.pow(2,32):  #先判断数据是否超长

            if num>=0:  #根据绝对值，做出判断。正数不做处理
                return int(str(abs(num))[::-1])
            else:       #负数需要用切片之后，加一个负号
                return -int(str(abs(num))[::-1])
        else:
            return "超出长度"

if __name__ == '__main__':
    f=Function().one(-120990000)
    print(f)