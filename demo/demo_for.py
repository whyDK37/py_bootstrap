#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""
for letter in 'Python':     # 第一个实例
   print( '当前字母 :', letter)

print("------------------------------------------")
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前字母 :', fruit)

print("------------------------------------------")
fruits = ['banana', 'apple',  'mango']
print("fruits length : ",len(fruits))
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])

print("------------------------------------------")
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print( '%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ("质数:",num), '是一个质数'