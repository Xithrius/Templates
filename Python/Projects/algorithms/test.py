In = '1234'
for i in range(len(In)):
    In = In[-1] + In[:-1]
    print(f'In: {In}, i: {i}')
