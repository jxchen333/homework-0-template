"""
fizzbuzz

Write a python script which prints the numbers from 1 to 100,
but for multiples of 3 print "fizz" instead of the number,
for multiples of 5 print "buzz" instead of the number,
and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.
"""

for i in range(100):
    j = i + 1 # 1~100
    if j%15 == 0:
        print('fizzbuzz')
    elif j%3 == 0:
        print('fizz')
    elif j%5 == 0:
        print('buzz')
    else:
        print(j)