# Mohammad Zafari
# mhdzafari80@gmail.com


TEST = False

def tostring(i,j,arr3):
    str1=''
    for k in range(i,j):
        str1 += (str(arr3[k])+' + ')
    str1 += str(arr3[j])
    return str1

def fsum(a,b,arr2):
    sum_def=0
    while(a <= b):
        sum_def += arr2[a]
        a += 1
    return sum_def

def find_subarray(arr1,given_sum):
    global TEST
    for i in range(len(arr1)-1):
        for j in range(i+1,len(arr1)):
            if given_sum == fsum(i,j,arr1):
                print(f"{tostring(i,j,arr1)} = {given_sum}")
                TEST = True
    if(TEST == False):
        print('-1')
        return False
    else:
        return True
    

"""
given_sum =int(input("Enter the sum: "))
arr= [1, 4, 0, 0, 3, 10, 5]
find_subarray(arr,given_sum)
"""
