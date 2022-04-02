
#5명의 시험 점수를 확인하고 일정 점수가 되면 합격시키는 for문
marks = [90, 25, 67, 45, 80]
a=list(range(len(marks)))
print(a)


#입력받은 list의 요소로 인덱싱 번호를 입력해 줄 수 있나?
b=0
for m in marks:

    if m >=70:
        print("{}번 학생은 합격입니다.".format(b))
    else:
        print("{}번 학생은 불합격입니다.".format(a))




