def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
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
selectionsort(array,size)
print('sorted data: ')
print(array)