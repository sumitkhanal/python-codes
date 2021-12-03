a=[26,641,1,0,-1,3]
n = 3
potion  =  0
def linear(a,n):
    global postion
    for i in range(len(a)):
        if a[i]==n:
            postion = i+1
            return True
    return False

if linear(a,n):
    print('found at ', postion)
else:
    print('not found')

def min(a):
    m=a[0]
    global postion
    for i in a:
        if i<m: 
            m=i
            postion=a.index(i)+1
    return m

q=min(a)
print("the min is and found ar t",q,postion)

def bubble(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j+1]<a[j]:
                c=a[j+1]
                a[j+1]=a[j]
                a[j]=c
    return a

z=bubble(a)
print('bubble',z)

def binary(z):
    global postion
    u=len(z)-1
    for l in range(u+1):
        mid=(l+u)//2
        if z[mid]==n:
            postion= mid+1
            return True
        elif z[mid]<n:
            l=mid+1
        elif z[mid]>n:
            u= mid-1
    return False
 
if binary(z):
    print("using binary found at",postion)
else:
    print('using binary not found')

a=[5,6,1,3,0,3] 
def insertion(a):
    for i  in range(len(a)):
        j=i
        while a[j-1]>a[j] and j>0:
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
    print('insertion',a)

insertion(a) 

a=[5,4,-1,2,0,3,-1]
def mergesort(a):
    if len(a)>1:
        l=a[:len(a)//2]
        r=a[len(a)//2:]
        mergesort(l)
        mergesort(r)
        i=0 #index of left
        j=0 #index of right
        k=0 #index of merged
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

mergesort(a)
print('mergesort',a)

a=[26,641,1,0,-1,3]
def quicksort(a,l,r):
    if l<r:
       pi=partion(a,l,r)
       quicksort(a,l,pi-1)
       quicksort(a,pi+1,r)

def partion(a,l,r):
    i=l #index leftside
    j=r-1 #index rightside less than pivot index
    pivot=a[r]

    while i<j:
        while i<r and a[i]<pivot:
            i+=1
        while j>l and a[j]>=pivot:
            j-=1
        if i<j:  #i has not crossed j so we swap
            a[i],a[j]=a[j],a[i]
    if a[i]>pivot:
        a[i],a[r]=a[r],a[i]
    return i

quicksort(a,0,len(a)-1)
print("quicksort",a)

a=[26,641,1,0,-1,3]
def selection(a):
    for i in range(len(a)):
        m=i
        for j in range(i,len(a)):
            if a[m]>a[j]:
                m=j
        a[m],a[i]=a[i],a[m]
    print('selection',a)
selection(a)

a=[1,6,1,2,1,0,5,1]
def counting(a):
    k=max(a)+1
    n=len(a)
    c=[0]*k
    b=[0]*n
    for i in range(n):
        c[a[i]]+=1
    for i in range(1,n-1):
        c[i]+=c[i-1]
    for i in range(n-1,-1,-1):
        b[c[a[i]]-1]=a[i]
        c[a[i]]-=1
    for i in range(n):
        a[i]=b[i]
    print(a)
counting(a)


    