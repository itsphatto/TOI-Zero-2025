N, S = map(int, input().split())
forwardconstant= [0]

for i in range(N):
    forwardconstant.append(int(input()))

amountofpeoplewhogetmessage = set()
constant = S


while constant != 0 and constant not in amountofpeoplewhogetmessage:
    amountofpeoplewhogetmessage.add(constant)
    constant = forwardconstant[constant]

print(len(amountofpeoplewhogetmessage))
