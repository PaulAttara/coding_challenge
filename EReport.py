#!/usr/bin/env python
import sys

#sorting function with n1 and n2 determining whether sort by number or lastname
def sort(list, n1, n2):
    for iteration in range(len(list[n1]) - 1, 0, -1):
        for index in range(iteration):
            if list[n1][index] > list[n1][index + 1]:
                
                temp = list[n1][index]
                temp2 = list[n2][index]
                temp3 = list[2][index]
                
                list[n1][index] = list[n1][index + 1]
                list[n2][index] = list[n2][index + 1]                
                list[2][index] = list[2][index + 1]                
               
                list[n1][index + 1] = temp
                list[n2][index + 1] = temp2
                list[2][index + 1] = temp3

#check number of command line arguments
if len(sys.argv) <= 1:
    print("Please type filename as second argument")
    sys.exit()

#store in string argument 1 (filename to read)
text_file = sys.argv[1]

#store in array each line
with open(text_file) as f:
    content = f.readlines()
content = [x.strip() for x in content] 

#initialize array that will hold arrays(strings) 
# and arrays that will hold numbers, fistnames, lastnames
strings = []
string_firstnames = []
string_lastnames = []
string_numbers = []

#iterate through each line in file and split into appropriate arrays
for element in content:
    if "#" in element:
        continue
    else:
        #split each line into 2 elements in array arr delimited by ","
        arr = element.split(",")
        #remove first whitespace in number
        arr[0] = arr[0].strip()
        #remove first whitespace in name
        arr[1] = arr[1].strip()
    
        string_numbers.append(arr[0])
        string_firstnames.append(arr[1].split()[0])
        string_lastnames.append(arr[1].split()[1])

#store in strings 3 arrays that hold numbers, firstnames and lastnames
strings.append(string_numbers)
strings.append(string_firstnames)
strings.append(string_lastnames)

print("Processing by employee number...")
sort(strings, 0, 1)
for i in range(0, len(strings[0])):
    print(strings[0][i] + "," + strings[1][i] + " " + strings[2][i])

print("\nProcessing by last (family) Name...")
sort(strings, 1, 0)
for i in range(0, len(strings[0])):
    print(strings[0][i] + "," + strings[1][i] + " " + strings[2][i])

