from art import logo
import os
#clear the output in the console = os.system("clear")
#Cool judge hammer looking logo
print(logo)
print('''Welcome to the secret auction
Grab your friends and let's get started''')

#Empty dictionary for all bidders with their bid price
auctioners = {}
#Function to calculate the highest bidder
def find_highest_bidder(bidder_log):
  #To compare bid prices against one another
  highest_bid = 0
  #Empty string to store key from dictionary auctioners{}
  winner = ''
  
  for bidder in bidder_log:
    #Amount is the value in dictionary
    bid_amount = bidder_log[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}. Congrats {winner}!")

def main():
  #As long as user chooses 'Yes' to add another bidder then this will stay true
  multiple_bidders = True
  
  while multiple_bidders:
    name = input("What is your name?:\n")
    bid = int(input("\nWhat is your bid? :\n$"))
    bidders = input("\nAre there any other bidder? 'Yes' or 'No':\n").lower()
    #Adding name and bid to the dictionary
    auctioners[name] = bid
    #Clear screen after recieving all user inputs
    os.system("clear")
    #No more bidders = false to exite while loop
    if bidders == 'no':
      #Call function to calculate who the winning bidder is
      find_highest_bidder(auctioners)
      multiple_bidders = False
#Call main function to get user inputs
main()