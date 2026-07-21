name = input("Name: ")
subject_1 = float(input("Subject 1 mark: "))
subject_2 = float(input("Subject 2 mark: "))
subject_3 = float(input("Subject 3 mark: "))
average = (subject_1 + subject_2 + subject_3)/3
Pass_status = True
print(f"\nsubject 1 mark: {subject_1}\nsubject 2 mark: {subject_2}\nsubject 3 mark: {subject_3}")

if average >= 80:
    print("Average letter grade A")
elif 70 <= average <= 79:
    print("Average letter grade B")
elif 60 <= average <= 69:
    print("Average letter grade C")
elif 50 <= average <= 59:
    print("Average letter grade D")
else:
    print("Average letter grade F")
    Pass_status = False

if Pass_status:
    print("Pass")
else:
    print('Fail')

if subject_3 < 40 or subject_2 < 40 or subject_1 < 40:
    print("Needs intervention")
