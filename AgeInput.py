# Question 1
birth_year = input("Please enter your born year:")
current_age = 2020-int(birth_year)
print("You are born in", birth_year)
print("In the year 2020, you will be", current_age, "years old.")

# Question 2

children_ticket = 8
adult_ticket = 10
senior_ticket = 8

if current_age <= 12:
    print("The children's ticket costs", children_ticket)

if current_age >= 65:
    print("The senior citizens ticket costs", senior_ticket)

if (current_age >= 13) and (current_age <= 64):
    print("The adult ticket costs", adult_ticket)
# OR
if current_age < 0:
    print("Ghost entry is free")

# Question 3
for i in range(0, 100):
    if i % 2 == 0:
        print(i)

# Question 4
for j in range(0, 100):
    if j % 2 != 0:
        print(j)
