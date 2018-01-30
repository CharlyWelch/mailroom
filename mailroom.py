from collections import OrderedDict

donor_data = {'Charly': [100.00], 'Andrew': [80.00], 'Jacob': [400.00], 'Charlie': [125.00], 'Jack': [75.00, 30.00]}

def main():
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

            if name in donor_data:
                donor_data[name] = donor_data[name] + [donation]
            else:
                donor_data[name] = [donation]
            print("Dear {0}, Thank you for your generous donation of {1}! We will be sure to put it to good use! Sincerely, Your Local Charity".format(name, "{0:.2f}".format(donation)))
        if choice == '3':
            break

        if choice == '2':
            orderD = OrderedDict(sorted(donor_data.items()))
            for key, val in orderD.items():
                numdon = len(val)
                total = sum(val)
                avg = total/numdon
                print("Name: {0} \t Total: {1} \t Number Donations: {2} \t Average donation: {3}".format(key, total, numdon, avg))

main()