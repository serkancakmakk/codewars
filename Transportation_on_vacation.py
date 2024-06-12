# After a hard quarter in the office you decide to get some rest on a vacation.
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. T
#     he manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. 
# If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).
def rental_car_cost(d):
    daily_rate = 40
    total_cost = daily_rate  * d 
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20
    return total_cost

# Argüman olarak gün sayısını belirleyip fonksiyonu çağırma
d = 8
result = rental_car_cost(d)
print("Rental car cost:", result)