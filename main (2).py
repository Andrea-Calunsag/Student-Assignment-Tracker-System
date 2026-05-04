# Program: Student Asignment Tracker System
# Author: Group 6
# Subject: Computer Science
# Description: A Python program that allows users to add, view, and mark assignments as done using finctions, loops, and input validation
# Date: May 2026


#List to store assignments
assignment_list = []

# Function to add a new assignment
def AddAssignment():
     # Get assignment name (must not be empty)
    while True: 
        name = input('Enter assignment name:').strip()
        if name == '':
            print('Name cannot be empty.')
        else:
            break
             
     # Get subject (must not be empty)
    while True:
        subject = input('Enter subject:').strip()
        if subject == '':
            print('Subject cannot be empty.')
        else:
            break
    
    # Get deadline (must not be empty)
    while True:
        deadline = input('Enter deadline:').strip()
        if deadline == '':
            print('Deadline cannot be empty.')
        else:
            break

    # Default status of assignment
    status = 'Not Done'
    
    # Store assignment details in a list
    assignment = [name, subject, deadline, status]
    
    # Add assignment to main list
    assignment_list.append(assignment)
    print('Assignment added successfully!')
    
# Function to display all assignments    
def ViewAssignments():
    # Check if list is empty
    if len(assignment_list) == 0:
        print('No assignments available.')
    else:
        counter = 1 # Used to number assignments

        # Loop through each assignment
        for assignment in assignment_list:
            # Display assignment details
            print(f'{counter}: {assignment[0]}, {assignment[1]}, {assignment[2]}, Status: {assignment[3]}')
            counter = counter + 1

        
# Function to mark an assignment as done
def MarkAsDone():
    # Check if there are assignments to update
    if len(assignment_list) == 0:
        print('No assignments to update.')
        return
        
    while True:
         # Ask user for assignment number
        number_input = input('Enter assignment number:')
        
        # Check if input is a valid number
        if number_input.isdigit():
            number = int(number_input)
            
            # Check if number is within valid range
            if 1 <= number <= len(assignment_list):
                # Update status to Done
                assignment_list[number - 1][3] = 'Done'
                print('Assignment marked as done')
                break
            else:
                print('Invalid assignment number. Try again')
        else:
            print('Please enter a valid number.')
    
    


#MAIN PROGRAM LOOP (menu system)
while True:
    print('\n-----MENU-----')
    print('1. Add Assignment')
    print('2. View Assignments')
    print('3. Mark as Done')
    print('4. Exit')

     # Get user choice
    choice_input = (input('Enter the number of your choice:'))

    # Validate input (must be a number)
    if choice_input.isdigit():
        choice = int(choice_input)
   
        # Perform action based on user choice    
        if choice == 1:
            AddAssignment()
        
        elif choice == 2:
            ViewAssignments()
        
        elif choice == 3:
            MarkAsDone()
        
        elif choice == 4:
            print('Exiting program...')
            break # Exit loop

        else:
             print('Invalid choice. Try again.')
     
        
        
    else:
        print('Please enter a valid number')
    
    
