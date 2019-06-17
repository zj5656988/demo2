"""
abcsab
让直接写一段代码字符串{abcsab}，找出重复字符串的最小的下标
"""
def fun(str_old):
    #获取key-下标的字典
    dic_temp={}
    list_temp=[]

    #遍历字符，找到重复
    for temp in set(str_old):
        dic_temp[temp]=str_origin.index(temp)
    for temp in str_origin:
        if temp not in list_temp:
            list_temp.append(temp)
        else:
            return dic_temp[temp]
"""
将123456 转化为["1","2",'3','4','5','6']
"""
def fun1(int_origin):
    temp_list=[]
    temp_list=[str(i) for i in int_origin] #通过for来改变元素的类型
    # return temp_list
    temp_list1=[]
    temp_list1=list(map(str,int_origin))  #通过python内置高阶函数，来改变
    #ps:python3的map返回类型变化了，现在是迭代的类型，需要使用list函数转化一下。
    return temp_list1



if __name__ == '__main__':
    str_origin=[1,2,3,465,6]
    f=fun1(str_origin)
    print(f)