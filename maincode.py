import math
import random

# Demo Loops
'''
print ('While Loop 1:')
i=0
while (i<5):
  print(i)
  i+=1

print('For Loop 1:')
for i in [3, 8, 1, 2]:
  print (i)

print('For Loop 2:')
for i in range(10):
  x=range(3)
  print(x)
'''  

# While Loop
iteration = int(input("How many numbers should be added?"))
counter = 0
finalnum = 0
while counter < iteration:
  num = random.randint (0,20)
  print num
  finalnum += num
  counter += 1
print 'The total is',finalnum

# For Loop
iteration = int(input("How many numbers should be added?"))
finalnum = 0
for count in range(iteration):
  num = random.randint (0,20)
  print num
  finalnum += num
print 'The total is',finalnum
