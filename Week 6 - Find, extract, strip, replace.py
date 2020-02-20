def original_string():
    # provided stored string
    str = 'X-DSPAM-Confidence: 0.8475'
    print("Original string:", str)

    # find the colon
    colon = str.find(':')
    print("Colon position:", colon)

    # find the end of the string
    end = len(str)
    print("Length of string:", end, "\n")

    # Extract after
    after_colon = str[colon+1:end]
    print("Everything after colon:", float(after_colon), "\n")


original_string()


def replace():
    # provided stored string
    str = 'X-DSPAM-Confidence: 0.8475'
    print("Original string:", str)

    # find the colon
    colon = str.find(':')
    print("Colon position:", colon)

    # find the end of the string
    end = len(str)
    print("Length of string:", end, "\n")

    # Extract after
    after_colon = str[colon + 1:end]

    # strip and replace
    print("Strip the '0' and Replace with a '9':", after_colon.replace("0", "9"))


replace()

input("Press enter to quit.")
