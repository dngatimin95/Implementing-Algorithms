import random
#search for val, if not then return None

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

def insertion_sort():

def merge_sort(x, y):
    i,j = 0
    x[len(x)] = 10**10
    y[len(y)] = 10**10
    while i+j < len(x)+len(y):
        if x[i] < y[j]:
            z[i+j] = x[i]
            i += 1
        else:
            z[i+j] = y[j]
            j += 1
            
def bubble_sort():

def heap_sort():

def quick_sort(x):
    pivot = random.randint(0,len(x)-1)
    for i in range(len(x)):
        if
        
