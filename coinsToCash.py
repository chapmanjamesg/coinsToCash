import math

def calc_dollar():
    piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32,
    "quarters": 40
    }
    dollarAmount = 0
    for coins in piggyBank:
        if coins == "pennies":
            coins * .01 += dollarAmount
        # elif coins == "nickles":
        #     coins * .05 += dollarAmount
    print(dollarAmount)
            



# cashToCoin

# def make_change():

#     dollar_amount = 8.69

#     piggy_bank = {
#         "pennies": 0,
#         "nickels": 0,
#         "dimes": 0,
#         "quarters": 0,
#     }

#     piggy_bank["quarters"] = math.floor(dollar_amount / .25)
#     dollar_amount = dollar_amount % .25
    
#     piggy_bank["dimes"] = math.floor(dollar_amount / .10)
#     dollar_amount = dollar_amount % .10
   
#     piggy_bank["nickels"] = math.floor(dollar_amount / .05)
#     dollar_amount = dollar_amount % .05
   
#     piggy_bank["pennies"] = math.ceil(dollar_amount / .01)
#     dollar_amount = dollar_amount % .01

#     return piggy_bank

# print(make_change())

#floor is rounding down ceiling rounds up