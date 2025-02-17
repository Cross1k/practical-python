# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
month = 0
over_paid = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print(month, round(total_paid, 2), round(principal, 2))
else:
    over_paid = principal
    total_paid = total_paid + over_paid
    print('over_paid', round(-over_paid, 2))
    principal = 0

print(f'Total paid is ${total_paid:0.2f} and over paid was ${-over_paid:0.2f} in {month} months')