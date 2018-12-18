
# coding: utf-8

# ### Chinese remainder theorem

# In[14]:


from functools import reduce
def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    inv = eea(a,b)[0]
    if inv < 1: inv += b
    return inv


# In[15]:


n = [3, 5, 7]
a = [2, 3, 2]
print(crt(n, a))


# ### Extended euclidean algorithm

# In[16]:


def eea(a,b):
    if b==0:return (1,0)
    (q,r) = (a//b,a%b)
    (s,t) = eea(b,r)
    return (t, s-(q*t) )

def find_inverse(x,y):
    inv = eea(x,y)[0]
    if inv < 1: inv += y
    return inv


# In[17]:


find_inverse(17, 10)

