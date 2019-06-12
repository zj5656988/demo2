class FindAllstr():
    def find(self,origin_list):
        #1、找到长度最短的字符
        min_str=origin_list[0]
        min_str_len=len(origin_list)
        for temp in origin_list:
            if len(temp) <= min_str_len:
                min_str=temp
                min_str_len=len(min_str)
        #2、判断是否是公共前缀
        list1_result=[]
        for i in range(min_str_len):
            for temp in origin_list:
                print(temp)
                if temp[i] != min_str[i]:
                    return list1_result

                else:
                    pass
            print(min_str[i])
            list1_result.append(min_str[i])


        return list1_result

if __name__ == '__main__':
    list=["flower","flow","flight"]
    f=FindAllstr().find(list)
    print(f)