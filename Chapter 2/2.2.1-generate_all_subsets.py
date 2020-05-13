## Task: Generate all subsets of a set

# When the function *search* is called with parameter k, it decides whether to
# include the element k in the subset or not, and in both cases, then calls itself with
# parameter k +1. Then, if k = n +1, the function notices that all elements have been
# processed and a subset has been generated.

subset = []
a = [1, 2, 3]

def search(k):
    if k == len(a):
        print(subset)
    else:
        subset.append(a[k])
        search(k + 1)
        subset.pop()
        search(k + 1)

search(0)
    

