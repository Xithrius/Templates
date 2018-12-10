import time


def main():
    In = input('In: ')
    In = list(In)
    for i in range(len(In)):
        if In[i].isalpha():
            if i % 2 == 0:
                if In[i].isupper():
                    In[i] = In[i].lower()
                elif In[i].islower():
                    In[i] = In[i].upper()
    In = ''.join(str(e) for e in In)
    print(f'Ot: {In}')


main()
