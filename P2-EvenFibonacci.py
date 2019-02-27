
# coding: utf-8

# In[56]:

import time


# In[41]:

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


# In[63]:

start = time.time()

result = 0
current = 0
i = 1
while current < 4000000: 
    current = fib(i)
    if current%2 == 0:
        result += current
    i += 1

print(result)

end = time.time()
elapsed = str(end - start)
print("Runtime: "+elapsed+" sec")


# In[ ]:



