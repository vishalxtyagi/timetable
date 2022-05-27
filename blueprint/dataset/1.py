import csv


def day():
    day_name = input("Enter the day: ").lower()
    Teachers = []
    if day_name == 'monday':
        with open('monday.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
    elif day_name == 'tuesday':
        with open('tuesday.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
    elif day_name == 'wednesday':
        with open('wednesday.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
    elif day_name == 'thursday':
        with open('thursday.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
    elif day_name == 'friday':
        with open('friday.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
            for row in list_of_csv:
                Teachers.append(row)
    return Teachers


teachers = day()
possible_sub = {}
no_class = []
sub_possible_sub = []
sub_no_class = []

ab_lect = int(input("Enter the lecture: "))
subject = input("Enter the preferred subject: ").lower()


# first priority (if subsequent lecture is free too)
for i in teachers:
    count = 0
    if i[ab_lect] != '1' and i[ab_lect-1] != '1' and i[ab_lect+1] != '1':             # looks for the possible substitutes
        possible_sub[i[0]] = i[-1]
        for j in i:                 # counts the total number of free periods
            if j == '0':
                count += 1
        no_class.append(count)

# second priority
if possible_sub == {}:
    for i in teachers:
        count = 0
        if i[ab_lect] == '0':
            possible_sub[i[0]] = i[-1]
            for j in i:
                if j == '0':
                    count += 1
            no_class.append(count)

print(possible_sub)  # prints the possible substitutes
print(no_class)     # prints the total number of free periods

# to see if the teacher specializes in the same subject
for i, (key, value) in enumerate(possible_sub.items()):
    count = 0
    if value == subject:
        sub_possible_sub.append(key)
        sub_no_class.append(no_class[i])
if sub_possible_sub != []:
    suited_teacher = max(sub_no_class)  # gives the teacher with the most amount of free time
    print("The recommended teacher would be:")
    for i in range(len(sub_possible_sub)):
        if no_class[i] == suited_teacher:
            print(sub_possible_sub[i])  # prints the teacher to that index

# if the possible candidates do not teach the preferred subject
else:
    suited_teacher = max(no_class)  # gives the teacher with the most amount of free time
    print("The recommended teacher would be:")
    for i, (key, value) in enumerate(possible_sub.items()):
        if no_class[i] == suited_teacher:
            print(key)  # prints the teacher to that index
