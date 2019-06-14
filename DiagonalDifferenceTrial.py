# A basic code for matrix input from user 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()

def diagonalDifference(matrix):
    prim =0
    sec=0
    length = len(matrix[0])
    i=0
    for count in range(length):
        prim += matrix[count][count]
        sec += matrix[count][(length-count-1)]
    return abs(prim-sec)

print(diagonalDifference(matrix))        

        
