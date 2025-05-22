def add(a=0,b=0):
    return a + b
res = add(15,20)
print(res)


#Finding max number
def find_max(numbers):
    max_numbers= numbers[0]
    for num in numbers:
     if num>max_numbers:
        max_numbers = num
    return max_numbers
print(find_max([60,8,6,0,4]))