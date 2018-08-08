
http://wiki.c2.com/?FizzBuzzTest

"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”." 




# shortest fizzbuzz challenge https://www.sololearn.com/Discuss/1007334/challenge-how-short-can-your-fizzbuzz-be


#v5
#56 characters
#using ideas from Вадим Сухотин (Vadim Sukhotin) (58 characters)
#https://code.sololearn.com/cMt98pF54144/#py
for x in range(101):
	print("Fizz"[x%3*4:]+"Buzz"[x%5*4:] or x)

#v4
#61 characters
#for i in range(1, 101):
#	print ("fizzbuzz"[(i%3)*4:(i%5==0)*8+4] or i)

#v3
#64 characters
#for i in range(1, 101):
#	print ("fizzbuzz"[(i%3!=0)*4:(i%5==0)*8+4] or i)

#v2
#65 characters
#[print("fizzbuzz"[(n%3!=0)*4:(n%5==0)*8+4] or n) for n in range(1,101)]

#v1
#print("\n".join(["fizzbuzz"[(n%3!=0)*4:(n%5==0)*8+4] or str(n)for n in range(1,100)]))
#86 characters

#v0
#87
#for i in range(1, 101):
	#print(("fizzbuzz" if i%5==0 else "fizz") if i%3==0 else "buzz" if i%5==0 else i)

#v-1
#130 characters
#import math
#print ("\n".join([["fizzbuzz",["buzz",["fizz",str(n)][math.ceil(n%3/n)]][math.ceil(n%5/n)]][math.ceil(n%15/n)] for n in range(1,100)]))
