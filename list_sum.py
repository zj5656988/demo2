"""\
1、求一个列表里的两个数，相加的最大值，返回那两个数的下标
"""

"""
下面通过冒泡的方法是不对的，因为只能查出相邻的两个数的加和值。不相邻的组合查不到
"""
# def fun():
#     list=[999,3,100,44,0,-1,0.1]  #定义数组
#     max_info=list[0]+list[1]     #最大的数，默认是第一个 第二个相加
#     result=0                     #定义下标的初始值
#     for i in range(len(list)-1): #冒泡排序，不断对比两个数的加和。
#         for j in range(i,len(list)-i-1):
#             temp=list[j]+list[j+1]
#             if temp>max_info:    #通过对比，求出最大的和值。
#                 max_info=temp    #赋值给max——info
#                 result = j       #max_info对应的下标j，赋值给result
#
#
#         return result,result+1,max_info  #返回三个值
"""
下面这个方法是可以的，先对列表排序，找出第一大和第二大的两个数。
在通过遍历，找出第一大的数，和第二大数的下角标
"""
def fun(list):
    list1=list[:]  #sort后，原列表会被修改，提前备份一个。或者直接修改备份的也行
    list.sort(reverse=True)
    temp1=list[0]  #第一大数
    temp2=list[1]  #第二大数
    i=0            #角标1
    j=0            #角标2

    for temp in list1:
        if temp1==temp:
            break  #找到了，直接跳出循环
        i+=1

    for temp in list1:
        if temp2==temp:
            break #找到了，直接跳出循环
        j+=1

    return i,j


"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
["flower","flow","flight"]
"""
# class FindAllstr():
#     def find(self,origin_list):
#         #1、找到长度最短的字符
#         min_str=origin_list[0]
#         min_str_len=len(origin_list)
#         for temp in origin_list:
#             if len(temp) <= min_str_len:
#                 min_str=temp
#                 min_str_len=len(min_str)
#         #2、判断是否是公共前缀
#         i=0
#         list1_result=[]
#         for i in range(min_str_len):
#             for temp in origin_list:
#                 if temp[i] != min_str[i]:
#                         break
#                 else:
#                     hh=temp[i]
#             list1_result.append(hh)
#             i+=1
#         return list1_result
def  longestCommonPrefix(list):

    """

    :type strs:  List[str]

    :rtype: str

     """

    list.sort(key  =len)# 根据列表中的字符串长度排序

    if not list:#如果列表为空，返回空

        return'1'

    result = ''#记录公共前缀，根据循环遍历实时更新result

    for i in  range(len(list[0])):#以列表中长度最小的单词strs[0]的长度为基准进行遍历

        for j in list[1:]:#遍历列表中的除基准单词外的每个字符串

            if j[i] !=  list[0][i]:#如果列表中的字符串的对应下标的值与strs[0][i]不相同

                return result

        result +=  list[0][i]#如果所有字符串下标都相同，更新最长公共前缀

    return result






if __name__ == '__main__':
    list=[]
    f=longestCommonPrefix(list)
    print(f)
