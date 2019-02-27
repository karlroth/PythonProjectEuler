
# coding: utf-8

# In[1]:

# returns factors of the number 
def factors(num):
    result = []
    for i in range(1,num + 1):
        if num%i == 0 :
            result.append(i)       
    return result
        
# Returns true if num is a prime
def isPrime(num):
    if num <= 1:
        return 
    elif num%2 == 0:
        return False
    elif:
        isPrime = len(factors(num)) == 2
    return isPrime

  
    


# In[ ]:

value = 600851475143

# iterates backwards through the list of factors for the value until it finds 
# a prime value. Since the factors are in increasing order we know that the 
# first prime we come accross is the largest.
for i in reversed(factors(value)):
    if i%2 != 0  & isPrime(i):
        print(i)
        break


# In[ ]:

value = 600851475143
oddFactors(600851475143)


# In[ ]:

value = 600851475143
for i in range(value):
    a = 2


# In[ ]:



