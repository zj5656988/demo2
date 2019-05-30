"""
难度分类
简单
题目描述
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","low","flight"]
输出: "fl"
示例 2:
输入:["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。（需求补充，必须都有fl才算公共前缀）
"""
"""
思路： 1、 找出最长的字符 
      2、判断是否是公共的前缀（最长字符切片，遍历比较）
      3、输出
"""
class Function2():
    def two(self,list_info):
        max_temp=len(list_info[0])
        for temp in list_info:
            if len(temp)>max_temp:
                max_temp=len(temp)
                max_info=temp
        #找到最长的字符。
        result=""
        for n in range(len(max_info)):
            for temp in list_info:
                if temp[n]==max_info[n]:
                    pass
                else:
                    break

                    pass
                pass


