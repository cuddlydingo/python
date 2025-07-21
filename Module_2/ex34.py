import sys

def my_loop():
    i = 0
    numbers = []
    max_num = int(sys.argv[1])
    inc_num = int(sys.argv[2])
    
    while i < max_num:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + inc_num
        
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        
    print("The numbers: ")
    
    for num in numbers:
        print(num)
        
my_loop()