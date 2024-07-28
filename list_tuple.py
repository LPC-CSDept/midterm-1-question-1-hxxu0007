import random
""" n = 5
numbers = []
for i in range(n):
    user_input = int(input("Enter your input:"))
    numbers.insert(i, user_input)
for num in numbers:
    print(num, numbers) """
    

    
""" nums = [10, 20, 25, 30, 35]
delete_key = int(input('Enter a number'))
nums.remove(delete_key)
print(nums) """


""" nums = [1,3,5,7,9,11,13,15,17,15,13,11,9,7,5,3,1]
del nums[0]
try:
    delete_key = 17
    nums.remove(delete_key)
except ValueError:
    print ('Key error: There is no value ', delete_key)
print(nums, min(nums), max(nums)) """

""" a = 10
b = a
print(a is b)
c = 'string'
d = c
print(c is d) 
l1 = [10, 20, 30]
l2 = l1
print(l1 is l2) """

#1) Take the row and column number from the user
#2) Fill in the matrix with the random numbers
#3) Find the greatest number in the matrix
rnum = int(input('Give the row numbers of the list: '))
cnum = int(input('Give the column numbers of the list: '))
numbers = []
for _ in range(rnum):
    row = []
    for _ in range(cnum):
        row.append(random.randint(0,100))
    numbers.append(row)  
print(numbers)
greatest_num = numbers[0][0]
for i in range(rnum):
    for j in range(cnum):
        if numbers[i][j] > greatest_num:
            greatest_num = numbers[i][j]  
print(f'The greatest number of list {numbers} is {greatest_num}')