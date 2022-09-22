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
| \(在行尾) | 续行符 | 
| \b |  退格  |
| \n | 换行 |


### List: 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
列表是写在方括号 [] 之间、用逗号分隔开的元素列表  
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表  
与Python字符串不一样的是，列表中的元素是可以改变的  
List可以使用+操作符进行拼接  
Python 列表截取可以接收第三个参数，参数作用是截取的步长  
如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：  

### Tuple: 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
元组写在小括号 () 里，元素之间用逗号隔开  
元组中的元素类型也可以不相同  
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置  
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则  
tup1 = ()    # 空元组  
tup2 = (20,) # 一个元素，需要在元素后添加逗号  

### Set:可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
基本功能是进行成员关系测试和删除重复元素  
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}  
set可以进行集合运算  
a = set('abracadabra')  

### Dictionary: 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合  
键(key)必须使用不可变类型  
在同一个字典中，键(key)必须是唯一的  
dic.keys() dic.values() 输出所有键或值  
构造函数 dict() 可以直接从键值对序列中构建字典如下：  
实例  

    dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  
    > {'Runoob': 1, 'Google': 2, 'Taobao': 3}  

    {x: x**2 for x in (2, 4, 6)}  
    > {2: 4, 4: 16, 6: 36}  

    dict(Runoob=1, Google=2, Taobao=3)  
    > {'Runoob': 1, 'Google': 2, 'Taobao': 3} 

创建空字典使用 { }  

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