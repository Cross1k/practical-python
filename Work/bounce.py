# bounce.py
#
# Exercise 1.5
drop_height = 100
bounce = 3/5
i = 0
while i < 10:
    drop_height = drop_height * bounce
    i = i+1
    print (i, '=', round(drop_height, 4))
