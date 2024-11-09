
import random
max_LINE=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symb_count={"A":2,"B":4,"C":6,"D":8}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols): 
     all_symbols=[]
     for symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbols)
        columns=[]
        for col in range(cols):
           columns = []

           current_symbols = all_symbols[:]

           for row in range (row):
              value=random.choice(current_symbols)
              current_symbols.remove(value)
              columns.append(value)

     columns.append(column)

     return columns

def print_slot_machine(column):
    for row in range (len(column[0])):
        for column in column in enumerate(column):
            if i !=len(column)-1:
               print(column[row],end="|")

            else:
                 print(column[row],end="")

                 print()


def deposit():
    while True:
      amount = input ("What would like to  deposit ? $")
      if amount.isdigit():
        amount=int(amount)
        if amount >0:
         break
        else:
            print("Amount must be greater than 0.")
      else:
        print("Please enter a number")
    return amount

def get_number_of_line():
 while True():
    lines = input("Enter the number of lines to bet on(1-"+str(max_LINE)+")?")
    lines= int(lines)
    if lines.isdigit():

        if 1 <= lines<=max_LINE:
           break
        else:
          print ("Enter the number of Lines. ")
    else:
        print("Please enter a number ")

    return lines

def get_bet():
    while True:
        amount = input("What wil")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
        else:
            print(f"amountmust be between${MIN_BET}-${MAX_BET}.")
    else:
         print("Please enter a number. ")
    return amount
        

def main():

     balance =deposit()
     line = get_number_of_line()
     while True:
      bet=get_bet()
      total_bet=bet*line

      if total_bet>balance:
        print(f"You do not have enough to bet that amount,Your current  balance is :{balance}")
        
      else:
             break

     print (f"Your betting ${bet}on{line} lines. Total bet is equal to :${total_bet}")
         
     print(balance,line)

     slots=get_slot_machine_spin(ROWS,COLS,symb_count)
     
     print_slot_machine(slots)




     main()
