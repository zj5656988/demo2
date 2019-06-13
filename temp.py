class FindAllstr():
    # def find(self,list1):
        # #1、找到长度最短的字符
        # min_str=origin_list[0]
        # min_str_len=len(origin_list)
        # for temp in origin_list:
        #     if len(temp) <= min_str_len:
        #         min_str=temp
        #         min_str_len=len(min_str)
        # #2、判断是否是公共前缀
        # list1_result=[]
        # for i in range(min_str_len):
        #     for temp in origin_list:
        #         print(temp)
        #         if temp[i] != min_str[i]:
        #             return list1_result
        #
        #         else:
        #             pass
        #     print(min_str[i])
        #     list1_result.append(min_str[i])


        # return list1_result
#         result=""
#         list.sort(key=len)
#         if not list:
#             return "列表为空"
#         else:
#             for i in range(len(list[0])):
#                 for j in list[1:]:
#                     if j[i] == list[0][i]:
#                         pass
#                     else:
#                         return result
#                 result+=list[0][i]
#             return result
#
#
    def find(self,strs):

        result = ""
        print(*strs)

        for ls in zip(*strs):  # zip+解包，输出的ls是一个元组
            print(ls)
            if len(set(ls)) == 1:

                # 即所有单词相同,如果所有单词不相同，去重后其长度不可能为1

                result += ls[0]

            else:

                break  # 有一个单词不同

        return result

if __name__ == '__main__':
    list=["flower","flow","flight"]
    f=FindAllstr().find(list)
    print(f)