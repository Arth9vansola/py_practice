def pal(n):
    reversed_st = ''
    for char in n:
        reversed_st = char + reversed_st
    return reversed_st    

print(pal("hello"))