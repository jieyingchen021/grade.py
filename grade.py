count=0
countA=countB=countC=countD=countE=countF=0

score=int(input('Enter a grade: \n'))
while score>=0:
    if 90<=score<=100:
        countA+=1
    if 80<=score<=90:
        countB+=1
    if 70 <=score<=80:
        countC+= 1
    if 60<=score<=70:
        countD+=1
    if 0<=score<=60:
        countF+=1
    score=int(input('Enter a grade or a negative value to stop:\n'))
count=countA+countB+countC+countD+countF
print('The number if scores entered',count)
print("A's=",countA)
print("B's=",countB)
print("C's=",countC)
print("D's=",countD)
print("E's=",countE)
print("F's=",countF)