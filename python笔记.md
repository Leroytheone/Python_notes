### Python数据类型
Number, String, List, Tuple, Set, Dictionary  
不可变：Number, String, Tuple  
可变：List, Dictionary, Set

### Number: int, float, bool, complex
type()函数可以用来查询变量所指的对象类型  
bool是int的子类  
运算符：+, -, *, /(除法，得到一个浮点数), //(除法，得到一个整数), %(取余), **(乘方)  
数学函数：  
| 函数     | 返回值 |
| ----------- | ----------- |
| abs(x)     | 返回数字的绝对值，如abs(-10) 返回 10 |
| cell(x)  | 返回数字的上入整数，如math.ceil(4.1) 返回 5       |
| exp(x)   | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045 |
| fabs(x) | 返回数字的绝对值，如math.fabs(-10) 返回10.0 |
| floor(x) | 返回数字的下舍整数，如math.floor(4.9)返回 4 |
| log(x) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0 |
| log10(x) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0 |
| max(x1, x2,...) | 返回给定参数的最大值，参数可以为序列 |
| min(x1, x2,...) | 返回给定参数的最小值，参数可以为序列 |
| modf(x) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示 |
| pow(x,y) | x**y 运算后的值 |
| round(x, n) | 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数 |
| sqrt(x) | 返回数字x的平方根 |

随机数函数：
| 函数 |	描述 |
| ----------- | ----------- |
| choice(seq) |	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。|
| randrange ([start,] stop [,step]) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1 |
| random() |	随机生成下一个实数，它在[0,1)范围内。|
| seed([x])	 | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| shuffle(lst) |	将序列的所有元素随机排序 |
| uniform(x, y) | 	随机生成下一个实数，它在[x,y]范围内。 |

数学常量：
| 常量	| 描述 |
| ----------- | ----------- |
| pi |	数学常量 pi（圆周率，一般以π来表示） |
| e |	数学常量 e，e即自然常数（自然常数） |

### String: 用单引号或者双引号括起来，用反斜杠\转义特殊字符
+是字符串的连接符，*表示复制当前的字符串  
Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
转义字符：
| 转义字符	| 描述 |
| ----------- | ----------- |
| \\(在行尾) | 续行符 | 
| \b |  退格  |
| \n | 换行 |

字符串运算符：
| 操作符	| 描述 |
| ----------- | ----------- |
| + | 字符串连接 |
| *	| 重复输出字符串 |
| [] | 通过索引获取字符串中字符 |
| [ : ]	| 截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的 |
| in |	成员运算符 - 如果字符串中包含给定的字符返回 True |
| not in |	成员运算符 - 如果字符串中不包含给定的字符返回 True |
| r/R |	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法 |	
| %	| 格式字符串 |	

字符串格式化：Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

| 符号 |	描述 |
| ----------- | ----------- |
| %c | 格式化字符及其ASCII码 |
| %s | 格式化字符串 |
| %d | 格式化整数 |
| %u | 格式化无符号整型 |
| %o | 格式化无符号八进制数 |
| %x | 格式化无符号十六进制数 |
| %X | 格式化无符号十六进制数（大写) |
| %f | 格式化浮点数字，可指定小数点后的精度 |
| %e | 用科学计数法格式化浮点数 |
| %E | 作用同%e，用科学计数法格式化浮点数 |
| %g | %f和%e的简写 |
| %G | %f 和 %E 的简写 |
| %p | 用十六进制数格式化变量的地址 |

f-string: f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。  
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去  
> name = 'Runoob'  
> f'Hello {name}'  # 替换变量  
>> 'Hello Runoob'  

> f'{1+2}'         # 使用表达式  
>> '3'  

> w = {'name': 'Runoob', 'url': 'www.runoob.com'}  
> f'{w["name"]}: {w["url"]}'  
>> 'Runoob: www.runoob.com'  

Python的字符串内建函数  
| 序号	| 方法 | 描述  |
| ----------- | ----------- | ----------- |
| 1	 |  capitalize() | 将字符串的第一个字符转换为大写 | 
| 2	 |   center(width, fillchar) | 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。 | 
| 3	 | count(str, beg= 0,end=len(string))  | 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数  | 
| 4	 |  bytes.decode(encoding="utf-8", errors="strict")  | Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。 |
| 5	| encode(encoding='UTF-8',errors='strict')  | 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'  |
| 6	| endswith(suffix, beg=0, end=len(string)) | 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.  |
| 7	| expandtabs(tabsize=8) |  把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。 |
| 8	| find(str, beg=0, end=len(string)) | 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
| 9	| index(str, beg=0, end=len(string)) | 跟find()方法一样，只不过如果str不在字符串中会报一个异常。 |
| 10	| isalnum() | 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False |
| 11	| isalpha() | 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False |
| 12	| isdigit() | 如果字符串只包含数字则返回 True 否则返回 False.. |
| 13	| islower() | 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| 14	| isnumeric() | 如果字符串中只包含数字字符，则返回 True，否则返回 False |
| 15	| isspace() | 如果字符串中只包含空白，则返回 True，否则返回 False. |
| 16	| istitle() | 如果字符串是标题化的(见 title())则返回 True，否则返回 False |
| 17	| isupper() | 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| 18	| join(seq) | 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| 19	| len(string) | 返回字符串长度 |
| 20	| ljust(width[, fillchar]) | 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。 |
| 21	| lower() | 转换字符串中所有大写字符为小写. |
| 22	| lstrip() | 截掉字符串左边的空格或指定字符。 |
| 23	| maketrans() | 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| 24	| max(str) | 返回字符串 str 中最大的字母。 |
| 25	| min(str) | 返回字符串 str 中最小的字母。 |
| 26	| replace(old, new [, max]) | 把将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。 |
| 27	| rfind(str, beg=0,end=len(string)) | 类似于 find()函数，不过是从右边开始查找. |
| 28	| rindex( str, beg=0, end=len(string)) | 类似于 index()，不过是从右边开始. |
| 29	| rjust(width,[, fillchar]) | 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串 |
| 30	| rstrip() | 删除字符串末尾的空格或指定字符。 |
| 31	| split(str="", num=string.count(str)) 以 str | 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串 |
| 32	| splitlines([keepends]) | 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| 33	|  startswith(substr, beg=0,end=len(string)) | 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
| 34	| strip([chars]) | 在字符串上执行 lstrip()和 rstrip() |
| 35	| swapcase() | 将字符串中大写转换为小写，小写转换为大写 |
| 36	|  title() | 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| 37	| translate(table, deletechars="") | 根据 table 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中 |
| 38	|  upper()  | 转换字符串中的小写字母为大写 |
| 39	| zfill (width) | 返回长度为 width 的字符串，原字符串右对齐，前面填充0  |
| 40	|  isdecimal() | 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。| 


### List: 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
列表是写在方括号 [] 之间、用逗号分隔开的元素列表  
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表  
与Python字符串不一样的是，列表中的元素是可以改变的  
List可以使用+操作符进行拼接  
Python 列表截取可以接收第三个参数，参数作用是截取的步长  
如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：  
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项  
可以使用 del 语句来删除列表的的元素  
Python列表函数和方法：  
len(list) 列表元素个数  
max(list) 返回列表元素最大值  
min(list) 返回列表元素最小值  
list(seq) 将元组转换为列表  

Python包含以下方法：
list.append(obj) 在列表末尾添加新的对象  
list.count(obj) 统计某个元素在列表中出现的次数  
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）  
list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) 移除列表中某个值的第一个匹配项
list.reverse()  反向列表中元素
list.sort( key=None, reverse=False) 对原列表进行排序
list.clear() 清空列表
list.copy() 复制列表


### Tuple: 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
元组写在小括号 () 里，元素之间用逗号隔开  
元组中的元素类型也可以不相同  
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置  
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则  
tup1 = ()    # 空元组  
tup2 = (20,) # 一个元素，需要在元素后添加逗号  
Python 的元组与列表类似，不同之处在于元组的元素不能修改。  
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。  
元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用： 
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合   
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
元组内置函数：len(tuple), max(tuple), min(tuple), tuple(iterable)

### Set:可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
集合（set）是一个无序的不重复元素序列。  
基本功能是进行成员关系测试和删除重复元素  
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}  
set可以进行集合运算  
a = set('abracadabra')  
添加元素：s.add()  
移除元素：s.remove()  
随机删除集合中的一个元素：s.pop()  
计算集合元素个数：len(s)  
清空集合：s.clear()  
判断元素是否在集合中存在：x in s  

### Dictionary: 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合  
键(key)必须使用不可变类型，值可以取任何数据类型，但键必须是不可变的，如字符串，数字   
在同一个字典中，键(key)必须是唯一的，但值不一定  
dic.keys() dic.values() 输出所有键或值  
构造函数 dict() 可以直接从键值对序列中构建字典如下：  
实例  

    dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  
    > {'Runoob': 1, 'Google': 2, 'Taobao': 3}  

    {x: x**2 for x in (2, 4, 6)}  
    > {2: 4, 4: 16, 6: 36}  

    dict(Runoob=1, Google=2, Taobao=3)  
    > {'Runoob': 1, 'Google': 2, 'Taobao': 3} 

创建空字典使用 { }  也可以使用内建函数 dict() 创建字典：  
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。  
两个重要的点需要记住：  

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，  
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行  

字典内置函数和方法：
len(dict)
str(dict): 输出字典，可以打印的字符串表示。  
type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。

dict.clear(): 删除字典内所有元素  
dict.copy(): 返回一个字典的浅复制  
dict.fromkeys(): 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值  
dict.get(key, default=None): 返回指定键的值，如果键不在字典中返回 default 设置的默认值  
key in dict: 如果键在字典dict里返回true，否则返回false  
dict.items(): 以列表返回一个视图对象  
dict.keys(): 返回一个视图对象  
dict.setdefault(key, default=None): 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default  
dict.update(dict2): 把字典dict2的键/值对更新到dict里  
dict.values(): 返回一个视图对象  
pop(key[,default]): 删除字典 key（键）所对应的值，返回被删除的值。  
popitem(): 返回并删除字典中的最后一对键和值。  

### 数据类型转换
Python 数据类型转换可以分为两种：  
隐式类型转换 - 自动完成  
显式类型转换 - 需要使用类型函数来转换  
在显式类型转换中，用户将对象的数据类型转换为所需的数据类型。 我们使用 int()、float()、str() 等预定义函数来执行显式类型转换。  

### Python推导式
#### 列表推导式
    [表达式 for 变量 in 列表] 
    [out_exp_res for out_exp in input_list]

    或者

    [表达式 for 变量 in 列表 if 条件]
    [out_exp_res for out_exp in input_list]

- out_exp_res：列表生成元素表达式，可以是有返回值的函数
- for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中
- if condition：条件语句，可以过滤列表中不符合条件的值

#### 字典推导式
    { key_expr: value_expr for value in collection }

    或

    { key_expr: value_expr for value in collection if condition }

#### 集合推导式
    { expression for item in Sequence }

    或

    { expression for item in Sequence if conditional }

#### 元组推导式
    (expression for item in Sequence )

    或

    (expression for item in Sequence if conditional )
元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。

    a = (x for x in range(1,10))
    a
    <generator object <genexpr> at 0x7faf6ee20a50>  # 返回的是生成器对象

    tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
    (1, 2, 3, 4, 5, 6, 7, 8, 9)

### Python运算符
算数运算符：+, -, *, /, %(取模), **(幂), //(向下取整除)  
比较运算符：==, !=, >, <, >=, <=  
赋值运算符：=, +=, -=, *=, /=, %=, **=, //=  
位运算符：&(与), |(或), ^(异或), ~(取反), <<(左移), >>(右移)  
逻辑运算符：and, or, not  
成员运算符：in, not in  
身份运算符：is, is not   

### 编程第一步
end关键字：关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：  
'print(b, end=',')'