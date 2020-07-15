import random

#different types of searches for val, if not then return None

def linear_search(x,val):
    for i in range(len(x)):
        if x[i] == val:
            return i
    return None
    
def binary_search(x,val):
    low = 0
    high = len(x)-1
    while (low <= high):
        mid = int((low + high)/2)
        if x[mid] > val:
            high = mid-1
        elif x[mid] < val:
            low = mid+1
        else:
            return mid
    return None

# different types of sort for list x

def insertion_sort(x):
    for i in range(1,len(x)):
        j = i
        temp = x[j]
        while temp < x[j-1] and j > 0:
            x[j] = x[j-1]
            j -= 1
        x[j] = temp
    return x

def merge_sort(x):
    if len(x)>1:
        l = x[:len(x)//2]
        r = x[len(x)//2:]
        i = j = k = 0

        merge_sort(l)
        merge_sort(r)

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                x[k] = l[i]
                i += 1
            else:
                x[k] = r[j]
                j += 1
            k+=1

        while i < len(l): 
            x[k] = l[i] 
            i+= 1
            k+= 1
          
        while j < len(r): 
            x[k] = r[j] 
            j+= 1
            k+= 1
    return x
            
def bubble_sort(x):
    for i in range(len(x)):
        for j in range(0,len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1],x[j]
    return x

def quick_sort(x, start, stop):
    if(start < stop): 
        pivot = pr(x, start, stop) 
        quick_sort(x , start , pivot) 
        quick_sort(x, pivot + 1, stop) 
    return x

def pr(x, start, stop): 
    rpiv = random.randrange(start, stop) 
    x[start], x[rpiv] = x[rpiv], x[start] 
    return p(x, start, stop)

def p(x,start,stop): 
    temp = start
    i = start - 1
    j = stop + 1
    while True: 
        while True: 
            i = i + 1
            if x[i] >= x[temp]: 
                break
        while True: 
            j = j - 1
            if x[j] <= x[temp]: 
                break
        if i >= j: 
            return j 
        x[i] , x[j] = x[j] , x[i]
        
