import os, random, subprocess
from ctypes import CDLL, create_string_buffer
import ctypes

libc = CDLL("libc.so.6") 
#byte array 
#1 byte is equal o one of those uint 8 thing
#call python byte array func, should be the same as however they generated b9

#Return an array of 4 bytes:
#x = bytearray(4)

#array of 9 bytes?
y = bytearray(9)
#print(y)

#this is a string, can turn into array?
#result = os.urandom(9)  

#not crypto secure but works for now
#b9 = bytearray(random.getrandbits(8) for _ in range(9))


# print(y)
# print(result)
# print(b9)

#generate input
#b9 = bytearray(random.getrandbits(8) for _ in range(9))

#print(b9)
#print(3)
#do the bytes to words

#check correctness of the bytes to words return


def main():
    arr = [random.randint(0,255) for _ in range(9)]
    print(arr)
    
    # b9 = bytearray(9)
    # #b9 = bytearray(random.getrandbits(8) for _ in range(9))
    # # Convert the Python bytearray to a C array of char
    # #(ctypes.c_char*len(b9).from_buffer(bytearray(b9)))

    # p = create_string_buffer(bytes(b9), len(b9))

    # #Shuffle the bytes before the NUL terminator byte, in-place.
    # libc.strfry(p)

    # # Convert the modified C array back to a Python bytearray
    # newdata = bytearray(p.raw)
    # print(newdata)
    # #print(b9)
    # #return b9

if __name__ == "__main__":
    main()