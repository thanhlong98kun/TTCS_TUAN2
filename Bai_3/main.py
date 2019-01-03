import os

NUMBER_ANSWER = 4 # So cau tra loi co trong 1 cau hoi
NUMBER_LINE_A_QUESTION = NUMBER_ANSWER + 2 # = So cau tra loi 1 cau + 1 cau hoi + 1 cau t ra loi 

OUTPUT = 'output3.txt'
DIR_EXAMS = './de'     # Dung de luu thu muc chua cac de
 # Danh sach cau hoi se luu bang mang 2 chieu, moi hang se la 1 cau hoi + so cau tra loi + 1 cau tra loi dung
questions = [[]]
numberQuestions = 0
score = 0            # Diem nguoi choi

# Ham kiem tra nhap vao co phai la so hay ko va co nam trong doan tu n => m hay k
def checkIsIntAndInArray(value, n, m):
    while True:
        value = input()
        try:
            value = int(value)
            if value >= n and value <= m:
                return value
            else:
                print("So phai tu %d den %d" %(n, m))
        except:
            print("Hay nhap 1 so: ")

# Lay so luong de co trong thu muc
def numExamInDir(path):
    return len(os.listdir(path))

# Lay danh sach cau hoi tu file roi luu vao mang 2 chieu questions[][], moi hang la 1 cau hoi
def arrayQuestions(path):
    global questions
    global numberQuestions
    questions = [[]]
    numberQuestions = 0
    ls = []

    if os.path.exists(path):
        with open(path, 'r') as f:
            ls = [x.strip() for x in f]

    size = len(ls)
    numberQuestions = int(size/NUMBER_LINE_A_QUESTION)
    questions = [ls[i:i+NUMBER_LINE_A_QUESTION] for i in range(0, size, NUMBER_LINE_A_QUESTION)]
    f.close()

# Luu diem cua nguoi choi
def saveScoreOfPlayer(path, name, score):
    if os.path.exists(path):
        with open(path, 'a') as f:
            f.write(name + '\n')
            f.write(str(score) + '\n')
        f.close()

# Hien diem cua nhung nguoi choi truoc
def getScoreOfPlayers(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            ls = [l.strip() for l in f]
        f.close()
        os.system("cls")
        for i in range(0, len(ls), 2):
            print("%s co diem la %d" %(ls[i], int(ls[i + 1])))
    else:
        print("Chua co nguoi choi nao")



# Hien cau hoi va tra loi
def showQuestionsAndAnswer():
    global score
    score = 0
    answer = 0
    for i in range(0, numberQuestions):
        print("Cau %d: %s" %(i + 1, questions[i][0]))
        for j in range(1, NUMBER_ANSWER + 1):
            print("%d. %s" %(j, questions[i][j]))

        print("Dap an cua ban la: ")    
        answer = checkIsIntAndInArray(answer, 1, NUMBER_ANSWER)
        if (questions[i][answer] == questions[i][NUMBER_LINE_A_QUESTION - 1]):
            score += 1


# Choi game
def playGame(name):
    n = numExamInDir(DIR_EXAMS)
    for i in range(0, n):
        print("%d. De so %d" %(i + 1, i + 1))

    select = int(input("Ban chon de so: "))
    pathExam = DIR_EXAMS + '/de' + str(select) + '.txt'

    arrayQuestions(pathExam)
    os.system("cls")
    showQuestionsAndAnswer()
    os.system('cls')
    saveScoreOfPlayer(OUTPUT, name, score)
    print("Diem cua \'" + name + "\' la:", score)


# Xuat menu ra man hinh
def menu():
    print('='*15 +'MENU'+ '='*15)
    print("1. Choi")
    print("2. Xem diem cua cac nguoi choi khac")
    print("3. Thoat")


def select():
    n = 0
    while True:
        menu()
        print("Ban chon: ")
        n = checkIsIntAndInArray(n, 1, 3)
        if n == 1:
            name = input("Ten cua ban la: ")
            os.system("cls")
            playGame(name)
        elif n == 2:
            getScoreOfPlayers(OUTPUT)
        else:
            break

# HAM CHINH CUA CHUONG TRINH
# ===============================================
def main():
    os.system('cls')
    select()

main()