driving = input("請問你有沒有開過車?")
age = input("請問你的年齡是?")
age = int(age)
if driving == "有":
    if age >= 18:
        print("讚讚")
    else:
        print("你是不是偷開車?")
elif driving == "沒有":
    if age >= 18:
        print("你可以試著去考駕照")
    else:
        print("很棒哦!認真讀書賺錢買車18歲就可以開了!")



