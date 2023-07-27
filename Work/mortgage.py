# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month <= 12:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

print('total_paid', round(total_paid,7))
print('Month', month)