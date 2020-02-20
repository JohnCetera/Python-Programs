fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
total = 0

for line in fhand:

    if line.startswith('X-DSPAM-Confidence'):
        colon = line.find(":")
        count += 1
        num = float(line[20:])
        total = num+total
        average = total / count
        print('Confidence level: ', num)

print('Count: ', count)
print("Total: ", total)
print('Average: ', average)
