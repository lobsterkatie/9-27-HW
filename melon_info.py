"""
Prints out all the melons in our inventory
"""


def main():
    melon_data = get_melon_data("melons.txt")
    melon_names = sorted(melon_data.keys())
    print_melon_data(melon_names, melon_data)


def get_melon_data(filepath):
    melons_file = open(filepath)

    # create an empty dictionary to hold the melon data and an empty list of
    # categories
    melon_data = {}
    categories = []

    for line in melons_file:
        #first line of file holds data category names; get them
        if line.startswith("TEMPLATE"):
            line = line.strip()  # strip off whitespace
            line = line[14:]  # strip off 'TEMPLATE' label and 'name' category
            categories = line.split("|")  # get categories

        #remaining lines hold data
        else:
            line = line.strip()  # strip off whitespace
            line = line[5:]  # strip off 'data' label
            data = line.split("|")  # get data
            name = data.pop(0)  # get overall key for melon (its name)

            #create a dictionary of data for this particular melon
            this_melons_data = {}
            for i, category in enumerate(categories):
                this_melons_data[category] = data[i]

            #add that dictionary to the overall melon list
            melon_data[name] = this_melons_data

    melons_file.close()

    return melon_data


def print_melon_data(melon_names, melon_data):
    for melon_name in melon_names:
        print "\n" + melon_name.upper() + ":"
        print melon_data[melon_name]

# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

main()
