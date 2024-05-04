import os, random
#byte array 
#1 byte is equal o one of those uint 8 thing
#call python byte array func, should be the same as however they generated b9

#Return an array of 4 bytes:
x = bytearray(4)

#array of 9 bytes?
y = bytearray(9)

#this is a string, can turn into array?
result = os.urandom(9)  

#not crypto secure but works for now
b9 = bytearray(random.getrandbits(8) for _ in range(9))


print(y)
print(result)
print(b9)

#generate input

#do the bytes to words

#check correctness of the bytes to words return