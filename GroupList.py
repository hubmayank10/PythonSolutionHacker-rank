L1 =[50,60,70,30,20,80,40]

input=100

def check(n1, n2):
    sumIt = n1 + n2
    if sumIt == input:
        return True
    else:
        return False

FinalList=[]
for E in L1:
    for E2 in L1:
        if (E2 != E):
            if check(E2, E):
                FinalList.append([E2, E])

print(FinalList)

needList = [sorted(inList) for inList in FinalList]
setIs = set()
for E in needList:
    setIs.add(tuple(E))

print(setIs)