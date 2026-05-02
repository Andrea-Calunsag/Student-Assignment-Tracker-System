
assignment_list = []


def AddAssignment():
    while True: 
        name = input('Enter assignment name:').strip()
        if name == '':
            print('Name cannot be empty.')
        else:
            break
    
    while True:
        subject = input('Enter subject:').strip()
        if subject == '':
            print('Subject cannot be empty.')
        else:
            break
    
    
    while True:
        deadline = input('Enter deadline:').strip()
        if deadline == '':
            print('Deadline cannot be empty.')
        else:
            break
    
    status = 'Not Done'
    
    assignment = [name, subject, deadline, status]
    
    assignment_list.append(assignment)
    print('Assignment added successfully!')
    
    
def ViewAssignments():
    if len(assignment_list) == 0:
        print('No assignments available.')
    else:
        counter = 1
        for assignment in assignment_list:
            print(f'{counter}: {assignment[0]}, {assignment[1]}, {assignment[2]}, Status: {assignment[3]}')
            counter = counter + 1

        

def MarkAsDone():
    if len(assignment_list) == 0:
        print('No assignments to update.')
        return
        
    while True:
        number_input = (input('Enter assignment number:'))
        
        if number_input.isdigit():
            number = int(number_input)
            
            if 1 <= number <= len(assignment_list):
                assignment_list[number - 1][3] = 'Done'
                print('Assignment marked as done')
                break
            else:
                print('Invalid assignment number. Try again')
        else:
            print('Please enter a valid number.')
    
    



while True:
    print('\n-----MENU-----')
    print('1. Add Assignment')
    print('2. View Assignments')
    print('3. Mark as Done')
    print('4. Exit')
    
    choice_input = (input('Enter the number of your choice:'))
    
    if choice_input.isdigit():
        choice = int(choice_input)
        
        if choice == 1:
            AddAssignment()
        
        elif choice == 2:
            ViewAssignments()
        
        elif choice == 3:
              MarkAsDone()
        
        elif choice == 4:
            print('Exiting program...')
            break
        
        
        else:
            print('Invalid choice. Try again.')
    
    else:
        print('Please enter a valid number.')