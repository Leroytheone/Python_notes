'''
def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]
 
    # 重新组合字符串
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
    
'''

#var1 = "Hello world"
#var1[-5:-1]

'''list=[1,2,3,4]
for x in list:
    print (x)'''
    
'''#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
 
# 调用 printme 函数，不加参数会报错
printme('2sfd')'''

# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   #return total
 
# 调用sum函数
a = sum( 10, 20 )
#print ("函数外 : ", tota)
type(a)