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
"""
1、思路找到最短的数
2、以最短的数的前几位字符从头比较。循环，如果一直就添加，不一致直接return
"""
def  find(list1):

    """

    :type strs:  List[str]

    :rtype: str

     """

    list1.sort(key  =len)# 根据列表中的字符串长度排序

    if not list1:#如果列表为空，返回空

        return'1'

    result = ''#记录公共前缀，根据循环遍历实时更新result

    for i in  range(len(list1[0])):#以列表中长度最小的单词strs[0]的长度为基准进行遍历

        for j in list1[1:]:#遍历列表中的除基准单词外的每个字符串

            if j[i] !=  list1[0][i]:#如果列表中的字符串的对应下标的值与strs[0][i]不相同

                return result

        result +=  list1[0][i]#如果所有字符串下标都相同，更新最长公共前缀

    return result

"""
思路二:
1、先将strs使用*表达式，取出里面的每个元素
2、将取出来的元素按照索引进行压包，压包后是一个元组
3、利用集合去重后判断集合长度来判断列表中单词的同一索引位置的字母是否相同，
如果相同则更新公共前缀
"""
def find_1(origin_list):
    result=""
    if len(origin_list)==0:
        return "列表为空"
    else:
        for ls in zip(*origin_list):  #zip+解包，输出的ls是一个元组
                if len(set(ls))==1:   #即所有单词相同,如果所有单词不相同，去重后其长度不可能为1
                    result+=ls[0]
                else:
                    return result    #有一个单词不同
"""
题目描述
合并两个有序数组合并，输出到一个新的数组中，其结果仍然是一个有序数组。
例如：输入：
nums1 = [1,2,3]
nums2 = [1,2,4]
输出：[1,2，3,4]
"""
"""
思路一：
列表1的数据往列表2插
先判断列表1中的字母列表2在不在，在的话不变，不在的话，插到最后。
然后对列表排序输出即可。list用sorted函数输出。
"""
def fun2to1(list1,list2):
    for temp in list1:
        if temp in list2:
            pass
        else:
            list_2.append(temp)

    return sorted(list_2)





if __name__ == '__main__':
    list_one=['fun1','funsss','fuwwww']
    list_null=[]
    list_1=[1,2,4,9]
    list_2= [1,3,4,7,9]
    f=fun2to1(list_1,list_2)
    print(f)
