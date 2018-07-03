#Andres Suarez
#Math 4330 Quiz 4

def IsNumber(vector):
  '''
  This function makes sure the values of a given vector are numbers. It checks each value, if they are not an int, float, or complex number it returns False. However, if those conditions are met it returns True.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True
  # This for loop will check each element of the vector to see if it's a number.
  for i in range(len(vector)):
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
    else:
      return inputStatus

def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # If the input is valid the function continues to compute the 2-norm
  if IsNumber(vector) == True:
    result = 0
    # This for loop will compute the sum of the squares of the elements of the vector.
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result
  else:
    return "invalid input"

def Normalize(vector):
  '''
  This function takes a vector as its argument. First it sets a temporary vector as the result of the 2 norm of our argument. Then it divides our argument by its 2 Norm. The result is stored in the initially empty result array.
  '''
  # If the input is valid the function continues to compute the Normalization of the vector
  if IsNumber(vector) == True:
    temp = twoNorm(vector)
    item = 0
    result = []
    #This for loop will compute a the division between the input and the its 2Norm then append it to result
    for i in range(len(vector)):
      item = (vector[i]) / temp
      result.append(item)
    return result
  else:
    return "invalid input"


def dot(vector1, vector2):
  '''
  This function takes 2 vectors of the same length and computes the dot product. First we check to see if the vectors are compatible. Then, a solution integer is initialized which will store our answer. The zip function is used to merge the 2 vectors of the same length into pairs. This way we match each element of the same index position to calculate the product and then add up the sum of the products. The final result is stored in the integer solution.
  '''
  # If the input is valid the function it will continue
  if IsNumber(vector1) == True and IsNumber(vector2):
    #if the length of the vectors are the same it will compute the dot product of the two
    if len(vector1) == len(vector2):
      result = 0
      #This for loop multiplies each of the elements of the vectors and stores it in result
      for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
      return result
    else:
      return "invalid input"
  else:
    return "invalid input"


def scalarVecMulti(scalar, vector):
  '''
  This function takes a scalar and a vector as it's arguments. An temporary integer "item" is created to store the product of the scalar with each element in the vector. Each result for "item" is stored in the empty "solution" list. Solution is returned which contains the product of the scalar and vector.
  '''
  # If the input is valid the function it will continue
  if IsNumber(vector) == True:
    item = 0
    result = []
    #This for loop multiplies the scalar by each element in the vector and stores it in result
    for i in range(len(vector)):
        item = scalar * vector[i]
        result.append(item)
    return result
  else:
    return "invalid input"

def vecSubtract(vector1, vector2):
  '''
  This function takes 2 vectors of the same length and computes the difference. A solution vector is initialized to return our final answer. Then a temporary result vector is initialized along with a temporary integer "item". The item integer computes the difference between the elements of the 2 vectors and stores it in our temporary result vector. The result vector now contains 3 lists inside of it with the difference between each element in vector1 with all elements of vector2. Since we are looking for the difference between the elements in matching index positions, we take out the correct difference from each list in our result vector and append it to our solution vector. The final result is solution = (vector1 - vector2)
  '''
  #Check if input is valid
  if len(vector1) == len(vector2):
    solution = []
    for i in range(len(vector1)):
      #temporary vector and integer
      result = []
      item = 0
      for j in range(len(vector2)):
        #takes difference between 1 element in vector1 and all elements in vector2
        item = vector1[j] - vector2[i]
        #appends all 3 lists into our temporary vector
        result.append(item)
      #appends only the correct difference into the solution
      solution.append(result[i])
    return solution
  else:
    return "The input is invalid"


def Gram_Schmidt(A):
  '''
  This function takes all functions listed above and combines them in order to form our Q and R matricies.
  '''
  #rows of matrix A
  m = len(A[0])
  #columns of matrix A
  n = len(A)
  #v are the vectors of A
  v = A
  #creates empty matricies Q and R based on the number of columns in A
  R = [[0]*n for i in range(n)]
  Q = [[0]*m for i in range(n)]
  #this for loop computes r11 and q1
  for i in range(n):
    R[i][i] = twoNorm(v[i])
    Q[i] = Normalize(v[i])
    #this for loop computes r12, r22, and q2
    for j in range(i+1,n):
      R[j][i] = dot(Q[i],v[j])
      temp = scalarVecMulti(R[i][j],Q[i])
      v[i] = vecSubtract(v[j],temp)
  return [Q,R]

A = [[1,0,1],[2,1,0]]

print(Gram_Schmidt(A))