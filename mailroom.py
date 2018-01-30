# import OrderedDict

donor_data = {'Charly': [100.00], 'Andrew': [80.00], 'Jacob': [400.00], 'Charlie': [125.00], 'Jack': [75.00, 30.00]}

while True:
    choice = '0'
    if choice == '0':
        choice = input('1: Send a Thank You \n2: Create a Report \n3: Quit')

    if choice == '1':
        name = input('Full Name:')
        while name.lower() == 'list':
            print(list(donor_data.keys()))
            name = input("Full name:")
        donation = float(input("Donation amount:"))
        # # Verify that the amount is in fact a number, and re-prompt if it isn’t.

        if name in donor_data:
            donor_data[name] = donor_data[name] + [donation]
        else:
            donor_data[name] = [donation]
        print("Dear {0}, Thank you for your generous donation of {1}! We will be sure to put it to good use! Sincerely, Your Local Charity".format(name, "{0:.2f}".format(donation)))
    if choice == '3':
        break

# if choice =='2':
#     #Print a list of your donors, sorted by total historical donation amount.
#     #Include Donor Name, total donated, number of donations and average donation amount as values in each row.
#     #Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)    
# #After printing this report, return to the original prompt (choice == 0 might work for this!) .