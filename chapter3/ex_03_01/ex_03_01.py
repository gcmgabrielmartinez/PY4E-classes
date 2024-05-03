hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter rate:"))

if h <= 40:
    gross_pay = 40*rate
else:
    gross_pay = (40 + (h-40)*1.5)*rate

print(gross_pay)