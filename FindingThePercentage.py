def avrg(user_list):
    nSum = 0.0
    #user_list
    for I in user_list:
        nSum = nSum + I
    return nSum/len(user_list)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    SList= student_marks.pop(query_name)
    print("{:.2f}".format(avrg(SList)))


