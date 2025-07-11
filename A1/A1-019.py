a = int(input(''))
b = int(input(''))
c = int(input(''))

if a == b == c:
    print('all the same')
elif a == b != c:
    print('neither')
elif a != b == c:
    print('neither')
elif a == c != b:
    print('neither')
else:
    print('all different')
