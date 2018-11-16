"""Case-study #2 My first code "Progressive taxation"
Developers:
Kartashova A. - 45%,Lorents T. - 40%, Taranets D. - 15%
"""
import local
# Enter revenue by month

jan = int(input(local.january))
feb = int(input(local.february))
mar = int(input(local.march))
apr = int(input(local.april))
may = int(input(local.may))
jun = int(input(local.june))
jul = int(input(local.july))
aug = int(input(local.august))
sep = int(input(local.september))
okt = int(input(local.october))
nov = int(input(local.november))
dec = int(input(local.december))
annual_income = jan + feb + mar + apr + may + jun + jul + aug + sep + okt + nov + dec

# Enter the martial status

subj_1 = local.one_subj
subj_2 = local.married
subj_3 = local.single_parent
print(subj_1,subj_2,subj_3)
familystatus = int(input())

# Tax percentage

Sn1 = 0.10
Sn2 = 0.15
Sn3 = 0.25
Sn4 = 0.28
Sn5 = 0.33
Sn6 = 0.35
Sn7 = 0.396

# Calculation of taxes

if  familystatus == 1:
    D1 = 0
    D2 = 9076
    D3 = 36901
    D4 = 89351
    D5 = 186351
    D6 = 405101
    D7 = 406751
    if annual_income < D2:
        N = Sn1 * (annual_income - D1)
    elif D2 <= annual_income < D3:
        N = Sn1 * (D2 - D1) + Sn2 * (annual_income - D2)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (annual_income - D3)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (annual_income - D4)
    elif D4 <= annual_income < D5:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (annual_income - D5)
    elif D5 <= annual_income < D6:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (annual_income - D6)
    elif D6 <= annual_income < D7:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (D7 - D6) + Sn7 * (annual_income - D7)

elif familystatus == 2:
    D1 = 0
    D2 = 18151
    D3 = 73801
    D4 = 148851
    D5 = 226851
    D6 = 405101
    D7 = 457601
    if annual_income < D2:
        N = Sn1 * (annual_income - D1)
    elif D2 <= annual_income < D3:
        N = Sn1 * (D2 - D1) + Sn2 * (annual_income - D2)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (annual_income - D3)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (annual_income - D4)
    elif D4 <= annual_income < D5:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (annual_income - D5)
    elif D5 <= annual_income < D6:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (annual_income - D6)
    elif D6 <= annual_income < D7:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (D7 - D6) + Sn7 * (annual_income - D7)

elif familystatus == 3:
    D1 = 0
    D2 = 12951
    D3 = 49401
    D4 = 127551
    D5 = 206601
    D6 = 405101
    D7 = 432201
    if annual_income < D2:
        N = Sn1 * (annual_income - D1)
    elif D2 <= annual_income < D3:
        N = Sn1 * (D2 - D1) + Sn2 * (annual_income - D2)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (annual_income - D3)
    elif D3 <= annual_income < D4:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (annual_income - D4)
    elif D4 <= annual_income < D5:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (annual_income - D5)
    elif D5 <= annual_income < D6:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (annual_income - D6)
    elif D6 <= annual_income < D7:
        N = Sn1 * (D2 - D1) + Sn2 * (D3 - D2) + Sn3 * (D4 - D3) + Sn4 * (D5 - D4) + Sn5 * (D6 - D5) + Sn6 * (D7 - D6) + Sn7 * (annual_income - D7)

print(N)
