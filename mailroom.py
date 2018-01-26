# You want to write a small command-line script that can handle some of the tasks associated with this job for you. Here’s a list of the things you want to be able to do:

# The script should have a data structure that holds a list of your donors and a history of the amounts they have donated.
donor_data = {'name': ['amounts in floats']}

# When run, the script should prompt the user to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
choice = '0'
while choice == '0':
    print('Choose 1 to Send a Thank You')
    print('Choose 2 to Create a Report')

    choice = input('Please make your choice:')
    return choice



# If the user selects ‘Send a Thank You’, prompt for a Full Name.
if choice == '2':
    ask FULL NAME
    raw_input

# If the user types ‘list’, show them a list of the donor names and re-prompt
if input.lowercase == 'list':
    return all names
    user = raw_input("What is your full name?")
    donor_data[user]

# If the user types a name not in the list, add that name to the data structure and use it.
if donor_data[user] not in donor_data:
    donor_data[len(donor_data)-1] =  ...
    #or is it donor_data[user]=[] ? 

# If the user types a name in the list, use it.
if donor_data[user] 

# Once a name has been selected, prompt for a donation amount.
value = input("please enter a donation amount")

# Verify that the amount is in fact a number, and re-prompt if it isn’t.
if type(value)!=int:
    value = input("Please enter an integer dollar amount")

# Once an amount has been given, add that amount to the donation history of the selected user.
donor_data[user] = donor_data[user] += value

# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
if choice == '1':
    "Dear {0}, Thank you for your donation of {1}! We will be sure to put it to good use! Sincerely, Your Local Charity" [user, last value in users donations list]