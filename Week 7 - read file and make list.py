# program to open file, read, strip info, put into list, sort, print
def create_list_from_file():
    # ask for file name
    fname = input("Enter a file name: ")
    # start with empty list
    my_list = []
    # try to open the file
    try:
        fhand = open(fname)
        # split line into individual words
        for line in fhand:
            words = line.split()
            # check words with list before adding
            for word in words:
                # add words not already in the list
                if word not in my_list:
                    # add words to list
                    my_list.append(word)
                    # sort list
                    my_list.sort()
        # Print list
        print(my_list)

        # pause program
        input("Press enter to quit.")
    # if not a file name or cannot access, restart
    except:
        print("That file will not open.")
        # end or try again
        end = input("quit? (y/n)")
        # yes will quit
        if end == "y":
            quit()
        # no will run again
        else:
            # start program again
            create_list_from_file()


create_list_from_file()
