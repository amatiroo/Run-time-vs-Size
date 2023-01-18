import random
import math
import time


def bubble_sort(x):
    
   
    swap = False
    for i in range(0,len(x)):
    
        for j in range(0,len(x)):
            if x[i]<=x[j]:
                swap=True
                temp = x[i]
                x[i]=x[j]
                x[j]=temp

        if swap==False:
            break
    
    return x


#Insertion Sort
def Insertion_sort(arr):
 
  
  for i in range(1,len(arr)):
      key = arr[i]
      
      j=i-1

      while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1

      arr[j+1]=key
  
  return arr


#Selection Sort
def Selection_sort(x):
    
    
    min = x[0]
    index=0
    for i in range(0,len(x)):
        min = x[i]
        
        for j in range(i,len(x)):
        
            if min > x[j]:
                
                min=x[j]
                index = j
        
        if min < x[i]:
            temp = x[i]
            x[i]=x[index]
            x[index]=temp
        
    
    return x




#Merge Sort


def merge (a , b):
  c = []
  
  
  while len(a)!=0 and len(b)!=0:
    if a[0] > b[0]:
      c.append(b[0])
      b.pop(0)
    else:
      c.append(a[0])
      a.pop(0)


  while len(a)!=0:
    c.append(a[0])
    a.pop(0)

  while len(b)!=0:
    c.append(b[0])
    b.pop(0)
  

  return c

def merge_sort(a):

  n = len(a)
  if n==1:
    
    return a

  mid = n//2

  l1 = a[0:mid]
  l2 = a[mid:n]

  l1 = merge_sort(l1)
  l2 = merge_sort(l2)


  return merge(l1,l2)



def merge_sort_main(arr):
  x = merge_sort(arr)
  return x


#Heap SOrt


def HeapSort(a):
  n=len(a)
  #Build Heap
  for i in range(math.floor(n/2),-1,-1):
    Heapify(a,n,i)

  for i in range(n-1,0,-1):
    temp=a[i]
    a[i]=a[0]
    a[0]=temp
    Heapify(a,i,0)

def Heapify(a,n,i):
  max=i
  left = 2*i +1
  right = 2*i+2
  
  if( (left< n) and (a[left] > a[i])):
    max=left
  
  if (right< n) and (a[right] > a[max]):
    max=right
  
  if (max!=i):
    temp=a[i]
    a[i]=a[max]
    a[max]=temp
    Heapify(a,n,max)


def Heap_sort_main(arr):
  HeapSort(arr)
  return arr


#Normal Quick SOrt using last element as pivot 
def quick_sort(arr,low,high):

  if low<high:
    pi = partition(arr,low,high)
    quick_sort(arr,low,pi-1)
    quick_sort(arr,pi+1,high)

def partition(arr,low,high):
  pivot = arr[high]
  i = low-1
  for j in range(low,high):
    if arr[j]<=pivot:
      i+=1
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp

  temp=arr[i+1]
  arr[i+1]=arr[high]
  arr[high]=temp

  return i+1


def Quick_sort_main(arr):
  quick_sort(arr,0,len(arr)-1)
  return arr


def median(a, b, c):
    lst = [a,b,c]
    lst.sort()
    return lst[1]

#A method to partition around the median
def partition_median(arr, low, high):
    left = arr[low]
    right = arr[high-1]
    length = high - low
    if length % 2 == 0:
        mid = arr[low + length//2 - 1]
    else:
        mid = arr[low + length//2]
  
    

    pivot = median(left, right, mid)

    pivotindex = arr.index(pivot) 

    arr[pivotindex] = arr[low]
    arr[low] = pivot

    i = low + 1
    for j in range(low + 1, high):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    temp = arr[low]
    arr[low] = arr[i-1]
    arr[i-1] = temp
    
    return i - 1 

    


 
def quick_sort_median(arr, low, high):
     
     if low < high:

         pivotindex = partition_median(arr, low, high)
         quick_sort_median(arr, low, pivotindex)
         quick_sort_median(arr, pivotindex + 1, high)




def Quick_median(arr):
  quick_sort_median(arr,0,len(arr))
  return arr


#below functions runs the sorting functions and calculate run time based on the size and return the array back to plot function to plot the graph
def Compare_all(sizen):
  y = []
  data = random.sample(range(1, 1000000),sizen)
  start_time = time.time()
  res =  Insertion_sort(data)
  time_taken = time.time() - start_time
  y.append(time_taken)
  
  start_time = time.time()
  res =  bubble_sort(data)
  time_taken = time.time() - start_time
  y.append(time_taken)

  start_time = time.time()
  res =  merge_sort_main(data)
  time_taken = time.time() - start_time
  y.append(time_taken)

  start_time = time.time()
  res =  Selection_sort(data)
  time_taken = time.time() - start_time
  y.append(time_taken)
  
  start_time = time.time()
  res =  Heap_sort_main(data)
  time_taken = time.time() - start_time
  y.append(time_taken)

  return y


  
  
  