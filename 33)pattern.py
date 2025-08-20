# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

n = 5
for rows in range(1,n+1):
    for cols in range(1,n+1):
        if rows == 1 or rows == n or cols == 1 or cols == n:
          print("*",end=" ")
        else:
          print(" ",end=" ")
    print() 
# __________________________________________________________________________________________________

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *

for rows in range (6):
    for cols in range(6 - rows - 1):
        print(" ",end=" ")
    for cols in range (2 * rows +1):
        print("*",end=" ")
    print()    

    # or

for i in range(7):
    print(" "*(7-i-1),"*"*(2*i+1))  
# _________________________________________________________________________________________________

#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * * 
for rows in range (6):
    for cols in range(6 - rows - 1):
        print(" ",end=" ")
    for cols in range (1 * rows +1):
        print("*",end=" ")
    print()

    #or

for i in range(7):
    print(" "*(7-i-1),"*"*i)
# _____________________________________________________________________________________________________


# *
# **
# ***
# ****
# *****
x = ("*****")
for index, x in enumerate(x):
    print(x*(index+1))

    # or
for i in range(7):
    print("*"*i)

    # or
for rows in range (6):                    
    for cols in range(rows + 1 ):             
        print("*",end=" ")                  
    print()    
# ___________________________________________________________________________________________________________

# + symbol         
for i in range (5):
    for j in range(5):
        if i==2 or j==2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()  