"""\
求一个列表里的两个数，相加的最大值，返回那两个数的下标
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


if __name__ == '__main__':
    list = [1, 23, 33, 1, 2, 12]
    fun(list)