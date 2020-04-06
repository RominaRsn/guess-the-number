import random

x=random.randint(1,100)

#print(x)
print("guess the number from 1 to 100:")
flg=0

while(flg==0):
    k=int(input())

    if k==x:
        print("correct ;)")
        flg=1
    elif k>x:
        print("the answer is lower than your guess :(")
    else:
        print("the answer is higher than your guess :(")
