import sys

print("Welcome to SplitWiser")


def fileinput():
    
    with open(sys.argv[1]) as f:
        linecount = 1
        for line in f:
            if linecount == 1:
                amt_list = {k:[] for k in line.strip().split(' ')}
            else:
                amt, *patrons = line.strip().split( )
                for patron in patrons:
                    amt_list[patron].append(float(amt)/len(patrons))
            linecount += 1

    print("Overview: ")
    print(amt_list)

    tax = float(input("Enter Tax: "))
    gratuity = float(input("Enter gratuity: "))
    caculate_splits(amt_list, tax, gratuity)


def commandline():

    print("For any prompt, type quit and enter to exit.")
    initials = input("Enter each person's initials separated by space: ")
    amt_list = {k:[] for k in initials.strip().split(' ')}

    print("Calculating splits for:\n"+"\n".join(amt_list.keys())+"\n")
    while True:
        amt = input("Enter new amount or quit: ")
        if amt == 'q' or amt == 'quit':
            break
        amt = float(amt)
        patrons = input("Enter initials: ")
        patrons = [patron for patron in patrons.strip().split(' ') if patron != '']
        for patron in patrons:
            amt_list[patron].append(amt/len(patrons))

    print("Overview: ")
    print(amt_list)

    tax = float(input("Enter Tax: "))
    gratuity = float(input("Enter gratuity: "))
    caculate_splits(amt_list, tax, gratuity)


def caculate_splits(amt_list, tax, gratuity):
    person_total = {patron:sum(amts) for patron,amts in amt_list.items()}
    total_total = sum(person_total.values())
    person_total_and_proportion = {patron:(total,total/total_total) for patron,total in person_total.items()}

    print("Splits:")
    tally = 0
    for person, t_p in person_total_and_proportion.items():
        total = t_p[0]
        prop  = t_p[1]
        final_amt = total + prop*tax + prop*gratuity
        tally += final_amt
        print("{} pays {}".format(person,final_amt))

    print("\nTally\nBill total : {}".format(tally))


if len(sys.argv) > 1:
    fileinput()
else:
    commandline()
