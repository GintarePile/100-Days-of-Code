from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to auction!")

auction = {}

#funkcija surasti laimetoja
def winner(bid_records):
  winner_sum = 0
  winner_name = "abc"
  for key in bid_records:
    bid_amount = bid_records[key]
    if bid_amount > winner_sum:
      winner_sum = bid_amount
      winner_name = key
      
  print(f"Winner of bid is {winner_name.upper()}, price: $ {winner_sum}.")
 
  

end_game = True
while end_game:
  name = input("What is your name? ")
  price = int(input("What is your bid? "))
  auction[name] = price #papildom zodyna nauju dalyvius
  stop_game = input('Are there any bidders? Type "y" as YES or "n" as NO. ')
  clear() #pradedam rasytu naujam lange
  if stop_game == "n":
    end_game = False
    winner(auction) #kvieciam funkcija kad rastu laimetoja
    


    
  

  