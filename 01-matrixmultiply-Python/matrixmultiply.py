# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if(len(m1[0])!=len(m2)):
        return None
    arr=[]
    for i in range(0,len(m1)):
        #print (arr)
        arr.append([])
        #print
    for i in range (0,len(m1)):
        for j in range (0,len(m2[0])):
            arr[i].append(j)
            #print(arr)           
            arr[i][j]=0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                arr[i][j]+=m1[i][k]*m2[k][j]
    return arr