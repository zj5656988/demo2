"""
以前一个旧题：
统计篇文章的各个字符出现个数
"""
def funCount():
    dict_temp={}
    dict_key_list=[]
    result_list=[]


    with open("C:\\Users\Administrator\Desktop\\test.txt","r",encoding='utf-8') as f:
        for line in f.readlines():
            temp_list1=line.strip().split(" ")
            for temp in temp_list1:
                if temp.isalpha():  #判断是否是纯字母
                    if temp not in dict_key_list: #p判断是否是一个新的值
                        dict_temp[temp]=temp_list1.count(temp) #统计这个列表的数量
                        dict_key_list.append(temp)             #放入字典值的列表，不重复统计。
                    else:
                        dict_temp[temp]+=dict_key_list.count(temp) #以前统计过得，统计数量相加。
                else:
                    pass
        result_list.append(dict_temp)  #返回包含字典的值。

    return result_list

if __name__ == '__main__':
    f=funCount()
    print(f)








if __name__ == '__main__':
    f=funCount()

