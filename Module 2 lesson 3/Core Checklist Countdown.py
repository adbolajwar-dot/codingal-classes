total_chores = 4 
orignal_count = total_chores
print(f"You have {orignal_count} chores to complete today.")

completed_chores = 0
chore_num = 1
while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no) ")
    if answer == "yes":
        completed_chores += 1
        chore_num += 1
        print("Great job! Chore completed.")
    else:
        print("OKay, finish it and check again")

    print("Chores remaining: ", total_chores - completed_chores)
    print()


print("==== ALL CHORES COMPLETE! ====")
print("Great work finishing your entire checklist today!\n")


print("Now let's safely peel at the infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition is always true, so we need to break out of the loop.")
    safety_counter += 1
    if safety_counter == 3:
        print("Breaking out of the loop now!")
        break


print("\n==== CHORE CHECKLIST SUMMARY ====")
print(f"Total chores: {orignal_count}")
print(f"Completed chores: {completed_chores}")
print(f"Remaining chores: {total_chores - completed_chores}")