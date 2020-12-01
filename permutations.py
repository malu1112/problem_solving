from itertools import permutations

def permutations(word):
    if len(word) == 1:
        return word
    perms = permutations(word[1:])
    chars = word[0]
    results = []
    for perm in perms:
        print(f'------> perm ---> {perm}')
        for i in range(len(perm) + 1):
            results.append(perm[:i] + chars + perm[i:])
    return results

print(permutations('Malathi'))
