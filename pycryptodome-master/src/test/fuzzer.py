import os, random, subprocess

def main():
    arr = [random.randint(0,255) for _ in range(9)]
    #b_arr = bytearray(arr)
    print(arr)
    #print(b_arr)
    
if __name__ == "__main__":
    main()