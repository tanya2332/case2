"""Case-study #2 My first code "Progressive taxation"
Developers:
Kartashova A.,Lorents T., Taranetz D.

"""

# string constants
name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION,name_month[month], end ='')
    income = float(input())
    annual_income += income
print(annual_income)
subj_1 = "Если вы один субъект, то введите 1,"
subj_2 = "если вы супружеская пара, то введите 2,"
subj_3 = "если вы родитель-одиночка, то введите 3:"
print(subj_1,subj_2,subj_3)
familystatus = int(input())
if  familystatus == 1:
    D1 = 0
    D2 = 9076
    D3 = 36901
    D4 = 89351
    D5 = 186351
    D6 = 405101
    D7 = 406751
    if annual_income < D2:
        Sn = 10
        N = Sn * (annual_income - D1)
    elif D2 <= annual_income < D3:
        Sn = 15
        N = Sn * (annual_income - D2)
    elif D3 <= annual_income < D4:
        Sn = 25
        N = Sn * (annual_income - D3)
    elif D3 <= annual_income < D4:
        Sn = 28
        N = Sn * (annual_income - D4)
    elif D4 <= annual_income < D5:
        Sn = 33
        N = Sn * (annual_income - D5)
    elif D5 <= annual_income < D6:
        Sn = 35
        N = Sn * (annual_income - D6)
    elif D6 <= annual_income < D7:
        Sn = 39.6
        N = Sn * (annual_income - D7)

elif familystatus == 2:
    D1 = 0
    D2 = 18151
    D3 = 73801
    D4 = 148851
    D5 = 226851
    D6 = 405101
    D7 = 457601
    if annual_income < D2:
        Sn = 10
        N = Sn * (annual_income - D1)
    elif D2 <= annual_income < D3:
        Sn = 15
        N = Sn * (annual_income - D2)
    elif D3 <= annual_income < D4:
        Sn = 25
        N = Sn * (annual_income - D3)
    elif D3 <= annual_income < D4:
        Sn = 28
        N = Sn * (annual_income - D4)
    elif D4 <= annual_income < D5:
        Sn = 33
        N = Sn * (annual_income - D5)
    elif D5 <= annual_income < D6:
        Sn = 35
        N = Sn * (annual_income - D6)
    elif D6 <= annual_income < D7:
        Sn = 39.6
        N = Sn * (annual_income - D7)

else:
    D1 = 0
    D2 = 12951
    D3 = 49401
    D4 = 127551
    D5 = 206601
    D6 = 405101
    D7 = 432201
    if annual_income < D2:
        Sn = 10
        N = Sn * (annual_income - D1)
    elif D2 <= annual_income < D3:
        Sn = 15
        N = Sn * (annual_income - D2)
    elif D3 <= annual_income < D4:
        Sn = 25
        N = Sn * (annual_income - D3)
    elif D3 <= annual_income < D4:
        Sn = 28
        N = Sn * (annual_income - D4)
    elif D4 <= annual_income < D5:
        Sn = 33
        N = Sn * (annual_income - D5)
    elif D5 <= annual_income < D6:
        Sn = 35
        N = Sn * (annual_income - D6)
    elif D6 <= annual_income < D7:
        Sn = 39.6
        N = Sn * (annual_income - D7)

print(N)

