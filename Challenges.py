if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print(arr)
    arr1 = list(set(arr))
    arr1.sort(reverse = True)
    print(arr1[1])
    
#leap year
def is_leap(year):
    # Write your logic here
    leap = False
    if year % 400 ==0:
        leap =  True
    elif year % 100 ==0: 
        leap =  False
    elif year % 4 ==0: 
        leap = True
    return leap

#There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the #integers in set  and #dislike all the integers in set . Your initial happiness is . For each  integer in the array, #if , you add  to your happiness. If , you #add  to your happiness. Otherwise, your happiness does not change. #Output your final happiness at the end.
if __name__=='__main__':
    s=input().split()
    array1=map(int,input().split())
    a=set(map(int, input().split()))
    b=set(map(int, input().split()))
    happy = 0
    sad = 0

    for i in array1:
        if i in a:
            happy = happy + 1
        elif i in b:
            sad = sad -1
    
    tot = happy + sad
    print(tot)
