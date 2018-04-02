import changes

# Gets a dictionary with all the teachers and the changes for the day
dictionary = changes.Changes().get_changes_dict()
# Number of changes for my class
count = 0

for teacher, changes in dictionary.items():
    for change in changes:
        if '3D' in change:
            if not count:
                print(teacher)
            count += 1
	            print(change)

print(count)
