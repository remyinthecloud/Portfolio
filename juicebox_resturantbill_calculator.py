#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Juicebox's infamous greetings. Gotta love it
print("Hey! This is Juicebox calculator mode. Cool, huh?")

#Ask the user for the total bill number and store that number as a decimal
bill = input("What was the total bill? $")
new_bill = float(bill)

#Ask the user how much percent they would like to tip and store that number as a decimal
tip = input("How much tip would you like to give? 10, 12, or 15? ")
new_tip = float(tip)


#Ask the user how many lovely humans they are eating with. Actually splitting the bill because I hear some humans are freeloaders
split = input("How many people to split the bill? " )
new_split = int(split)

#Divide the bill by the number of users splitting the bill to get the price each user has to pay for the bill
final_bill = (new_bill / new_split)
#Divide the tip by 100 to get the decimal number of the tip percentage. Then multiply that decimal by the bill each person has to pay to get how much each user has to tip.
final_tip = final_bill * (new_tip / 100)


#Take the bill for each user and tip for each user and add them together to get the final bill price for each user.
pay = final_bill + final_tip

#Format the bill price to two decimals
pay_price = "{:.2f}".format(pay)

#Congrats! You get to pay money for that good or bad food!
print(f"Each person should pay: ${pay_price}")
print("Hope it was good! Juicebox out")