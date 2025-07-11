actuallylotto, actuallylottoinnumber = input().split()
yourlotto, yourlottonumber = input().split()

prizes = []

if actuallylotto == yourlotto and actuallylottoinnumber == yourlottonumber:
    prizes.append(1000000)

if actuallylottoinnumber == yourlottonumber:
    prizes.append(100000)

if yourlottonumber[-2:] == actuallylottoinnumber[-2:] and yourlotto == actuallylotto:
    prizes.append(1000)

if yourlottonumber[-3:] == actuallylottoinnumber[-3:] and yourlotto == actuallylotto:
    prizes.append(2000)

if yourlottonumber[-2:] == actuallylottoinnumber[-2:] and yourlotto != actuallylotto:
    prizes.append(100)

if yourlottonumber[-3:] == actuallylottoinnumber[-3:] and yourlotto != actuallylotto:
    prizes.append(200)

if yourlotto == actuallylotto:
    prizes.append(20)

if not prizes:
    print(0)
else:
    print(max(prizes))
