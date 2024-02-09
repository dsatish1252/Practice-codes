c_type = input().lower()
annual_income = int(input())
tax = 0
if c_type == "individual":
    if annual_income <= 250000:
        tax = 0
    elif annual_income > 250000 and annual_income <= 500000:
        tax = (5 / 100) * annual_income
    elif annual_income > 500000 and annual_income <= 1000000:
        tax = 12500 + (20 / 100) * annual_income
    else:
        tax = 112500 + (30 / 100) * annual_income
    print(tax)
elif c_type == "senior citizen":
    if annual_income <= 300000:
        pass
    elif annual_income > 300000 and annual_income <= 500000:
        tax = (5 / 100) * annual_income
    elif annual_income > 500000 and annual_income <= 1000000:
        tax = 10000 + (20 / 100) * annual_income
    else :
        tax = 110000 + (30 / 100) * annual_income
    print(tax)
elif c_type == "super senior citizen":
    if annual_income <= 500000:
        pass
    elif annual_income > 500000 and annual_income <= 1000000:
        tax = (20 / 100) * annual_income
    else :
        tax = 100000 + (30 / 100) * annual_income
    print(tax)
else:
    print(-1)