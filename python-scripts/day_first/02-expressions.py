age = int(input("Enter your age: "))

if age < 18:
    print("Bye!")
else:
    print("Hello!")

print(age)

step = 1
max_step = 200

while step < max_step:
    print(step)
    step += 1