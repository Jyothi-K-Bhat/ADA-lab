def mergesort(aray):
    if len(aray)>1:
        r=len(aray)//2
        L=aray[:r]
        M=aray[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                aray[k]=L[i]
                i+=1
            else:
                aray[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            aray[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            aray[k]=M[j]
            j+=1
            k+=1
def read_input():
    a=[]
    n=int(input("Enter the number of TV channels: "))
    print("Enter the numebr of viewers: ")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a;
array=read_input()
mergesort(array)
print('sorted data: ')
print(array)