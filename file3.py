def factorial(x):
    '''this is recursive function to find the factorial or integer '''


    if x==0 or x==1:
        return 1
    else:
        #calling funtion inside a funtion 
        return x*factorial(x-1)
    
#display result 
print(factorial.__doc__)
print("the facotrial of 0 :",factorial(0)) 
print("the factorial of 1 :",factorial(1))
print("the factorial of 2 :",factorial(2)) 
print("the factorial of 3 :",factorial(3)) 
print("the factorial of 4 :",factorial(4))
print("the factorial of 5 :",factorial(5))
print("the factorial of 10 :",factorial(10))    