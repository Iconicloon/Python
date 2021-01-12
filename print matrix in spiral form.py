m,n=4,4 #ending row 'm' and column index 'n'         k=>   1  2  3  4
a=[[1,2,3,4],                                       #      5  6  7  8
   [5,6,7,8],                                       #      9 10 11 12
   [9,10,11,12],                                    #m=>  13 14 15 16  
   [13,14,15,16]]                                   #      ^        ^
k=0 # starting row index 'k'                        #      l        n             
l=0 # starting column index 'l'                        
    #i is the iterator                              
while(k<m and l<n):                                 
    for i in range(l,n):
        print(a[k][i],end=" ")

    k+=1
    for i in range(k,m):
        print(a[i][n-1],end=" ")
        
    n-=1
    if(k<m):
        for i in range(n-1,l-1,-1):
            print(a[m-1][i],end=" ")
        m-=1

    if(l<n):
        for i in range(m-1,k-1,-1):
            print(a[i][l],end=" ")
        l+=1
