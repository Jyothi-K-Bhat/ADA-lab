def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
def read_input():
    a=[]
    n=int(input("Enter the number of TV channels: "))
    print("Enter the numebr of viewers: ")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a;
array=read_input()
size=len(array)
labeldata="Quicksort"
quicksort(array,0,size-1)
print('sorted data: ')
print(array)