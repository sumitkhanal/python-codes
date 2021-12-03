a=[1,2,3,4]
n=5
pos=-1

def search(a,n):
    global pos
    for i in range(len(a)):
        if a[i]==n:
            pos=i+1
            return True
    return False

if search(a,n):
    print("found",pos)
else:
    print("not found")
