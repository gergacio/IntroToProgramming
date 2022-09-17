# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

def even_num(list):
    even = []
    for num in list:
        if num % 2 == 0:
            even.append(num)
    return even
print(even_num(numbers))    
# 2. Print the difference between the largest and smallest value:

def max_nim_diff(list):
    return max(list) - min(list)
print(max_nim_diff(numbers))    
# 3. Print True if the list contains a 2 next to a 2 somewhere.
#using enumerate object give us counter (i) as a key
def next_same_as_prev(list, n):
    for i, num in enumerate(numbers):
        if num == n and numbers[i + 1] == n:
            return True
print(next_same_as_prev(numbers, 2))            

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

def check_range(list):
    have_range = False
    six_pos = numbers.index(6)
    seven_pos = numbers.index(7)
    if (six_pos < seven_pos):
        del numbers[six_pos:seven_pos + 1]
    return have_range
check_range(numbers)
# check for more cases...   
while True:
    if check_range(numbers) == True:
        continue
    else:
        break
         
print(sum(numbers))

# 5. HARD! Print the sum of the numbers. 

#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.

#    initialize list again..
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
index_13 = numbers.index(13)
del numbers[index_13:]
print(sum(numbers))
#    HINT - You will need to track the index throughout the loop.
#    
#    So [5, 13, 2] would have sum of 5.  ????


