n = []

for i in range(1,100 + 1):
    n.append(i**2)

def find_sum(k):
    nums = []
    for el in str(k):
        nums.append(int(el))
    return sum(nums)

def check_1(lst):
    k = 0
    for el in lst:
        if len(str(el)) > 1:
            return False
        k += 1
        if k == len(lst):
            return True

def transform_lst(lst):
    new_n = []
    for el in lst:
        new_n.append(find_sum(el))
    return new_n

while check_1(n) != True:
    n = transform_lst(n)
    print(n)




