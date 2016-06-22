#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 3. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def ex3():
  x = 1; y = 2
  while y * y - x * x != 68:
    if y * y - x * x > 68:
      x += 1
    else:
      y += 1
  return (x, y)

print(ex3());


# 1. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def three():
  array = [1, 2, 3, 4]
  for x in array:
    a = array[:]
    a.remove(x);
    for y in a:
      b = a[:]
      b.remove(y)
      for z in b:
        print(x, y, z)

def three2():
  array = [1, 2, 3, 4]
  for x in array:
    for y in array:
      for z in array:
        if x == y or y == z or x == z:
          continue
        print(x, y, z)

#three2()

#array = [8, 4, 9, 2, 3, 1]
#maxValue = array[0];
#for index in range(1, len(array)):
#  if array[index] > maxValue:
#    maxValue = array[index]
#
#print(maxValue)

def func(x, n):
  result = 1
  for i in range(0, n):
    result = result * x
  return result

#print(func(2, 3));

#aList = [123, 'xyz', 'zara', 'abc'];
#aList.append( 2009 );
#print "Updated List : ", aList

def factors(n):
  i = 1
  array = []
  while i * i <= n:
    if n % i == 0:
      array.append(i);
      if n / i != i:
        array.append(n / i);
    i += 1
  return array

#print(factors(36));

def factors2(n):
  i = 1
  array = []
  while i <= n:
    if n % i == 0:
      array.append(i);
    i += 1
  return array

#print(factors2(36));
