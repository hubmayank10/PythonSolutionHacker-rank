import builtins

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    myList = []
    for obj in integer_list:
        myList.append(obj)
    tyTuple = tuple(myList)
    FinalHash = builtins.hash(tyTuple)
    print(FinalHash)
