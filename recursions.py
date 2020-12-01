
def fact(n):
    print(n)
    if n == 0:
        print(f'if----->{n}')
        return 1
    else:
        print(f'else---->{n}')
        return n * fact(n-1)

# print(fact(5))


def sum(n):
    print(n)
    if n == 0:
        print(f'if----->{n}')
        return 0
    else:
        print(f'else---->{n}')
        return n + sum(n-1)

# print(sum(10))


def innersum(n):
    print(f'n----> {n}')
    if n == 0:
        print(f'if ----> {n}')
        return 0
    else:
        print(f'else ---> {n}')
        return n % 10 + innersum(n//10)
# print(innersum(123))


def word_spit(s, words):
    words_set = list()
    for word in words:
        if word in s:
            words_set.append(word)
    print(words_set)

word_spit('themanran', ['clown', 'ran', 'man'])
# word_spit('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])

