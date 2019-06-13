"""
99乘法表
"""

def nine_nine_table1():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(j)+'*'+str(i)+'='+str(i*j),end=" ") #end="" 可以把输出的字符连起来
        print("") #用来换行


if __name__ == '__main__':
    f=nine_nine_table1()

