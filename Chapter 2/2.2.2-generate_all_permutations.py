## Generate all permutations

# Each function call appends a new element to permutation and records that it
# has been included in chosen. If the size of permutation equals the size of the
# set, a permutation has been generated.

n = 3
lst = list(range(n))
chosen = [False]*n
permutation = []

def search():
    if len(permutation) == n:
        print(permutation)
    else:
        for i in range(n):
            if chosen[i]:
                continue
            chosen[i] = True
            permutation.append(lst[i])
            search()
            chosen[i] = False
            permutation.pop()

search()