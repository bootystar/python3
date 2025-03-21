"""
range() 函数
如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:
range(5) # 生成一个从0到4的数列
range(5,9) # 生成一个从5到8的数列
range(0,10,3) # 生成一个从0到9的数列, 步长为3
range(-10,-100,-30) # 生成一个从-10到-99的数列, 步长为30()

注意:
range()生成的序列为不可变的, 不能添加或删除元素
"""

for i in range(5,15,3):
    print(i)
print("=============")
for i in range(-10, -100, -30):
    print(i)