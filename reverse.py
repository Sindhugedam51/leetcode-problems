def revarr(arr,n):
    st=[]
    for i in range(n):
        st.append(arr[i])
    i=0
    while len(st)>0:
        top=st.pop()
        arr[i]=top
        i+=1
    for i in range(n):
        print(arr[i],end=" ")
n=4
arr=[100,200,300,400]
revarr(arr,n)