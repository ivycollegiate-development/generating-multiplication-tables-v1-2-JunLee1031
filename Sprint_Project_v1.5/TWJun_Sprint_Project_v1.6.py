def main():
    while True:
        try:
            a= float(input('Please enter a numeber here'))
            multi_table(a)
    except ValueError:
        print('Invalid input, please enter a numener value.')
        continue 
    choice = input("Do you want to generate another table?"). lowwer()
    if choice !='y'
    print('Thank for using the multiplication table generator!') 
    break
