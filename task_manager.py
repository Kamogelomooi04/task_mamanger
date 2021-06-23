# Program is running perfectly fine on  my side all functions working when called. 
# If they are not working on your side, would you kindly let me know exactly which functions it is.


# Module imported for delay in execution of some code.
import time

# Module imported for displaying date in tasks file.
import datetime


def login():

    # Opening up the 'user.txt' file, to read through its contents.
    with open("user.txt","r") as uf:

        users = ""

        for lines in uf:

            users += lines

    uf.close()        

    print()

    # Prompt for user to enter their username.
    username = input("Please enter your username. \n") 

    print()
    # Prompt the user to enter their password.
    password = input("Please enter your password. \n")
    
    # Checking if the username entered is in the contnts of the file.
    username_check = (users.find(username))

    # Checking if the password enterd is in the contnts of the file.
    password_check = (users.find(password))

    # Code in this function checks and makes sure the user enters a 
    # password that belongs to the username that accompanies it.
    # Prevents users logging in with just any password that's in the file.
    def password_validity_check():

        # What I'm doing here is trying to find how many characters are in the username that is entered.
        length_of_username = len(username)

        # Here I'm trying to find the las character in the username, to use as a reference point.
        last_char_of_username = username[length_of_username -1]

        # If the letter 2 indices before the position of the first letter of the password is equal to 'last_char_of_username'
        # Then the password belongs to the that username.
        first_letter_of_password_position = (password_check - 3)

        last_letter_of_usernme = users[first_letter_of_password_position]

        # If the password entered does not belong to the username that accompanies it,
        # an error message will be displayed to the user.
        if last_letter_of_usernme != last_char_of_username:
            
            print()

            print(" Incorrect Password.")

            print()

            login()

        # If the user enters a password that belongs to th username that accompanies it,
        # Then the user will be granted access.
        if last_letter_of_usernme  == last_char_of_username:

            print()

            print("successfully logged  in")

        
    # This function contains the code that will run when the option to reguster a user is chosen.
    def register_username():

        if username != "admin":
        
            # prompt to enter username of the user to be added.
            reg_username = input("Please enter a username for the new user.\n")

            # This here checks if the new username entered already exist in the "user.txt" file or not.
            reg_usernameCheck = (users.find(reg_username))

            # if the new username exists in the file, an error message will be displayed to the user.
            if  reg_usernameCheck != -1:

                print()

                print("Username entered already exist.")

                print()

                register_username()

            # If the new username entered does not exist in the "user.txt" file the program will continue.
            if reg_usernameCheck == -1:

                with open("user.txt","a") as f:
            
                    f.write("\n" + reg_username + ", ")
        
                    f.close()    

                    print()

                    register_password()


        # This function contains the code that will run when the option to register a new user is chosen.
    def register_password():
    
        # This line prompts the user to enter the new password for the new user being registered.
        reg_password = input("Please enter a password for the new user.\n")

        print()
        
        # This line prompts the user to confirm the password entered.
        reg_passwordConfirm = input("Please confirm the password.\n")

        # If the two passwords don't match the user will be notified via an error message,
        # and then prompted to try the process again.
        if reg_passwordConfirm != reg_password:
            
            print()
        
            print("Passwords don't match.")

            print()

            register_password()    

        # If both the passwords match, the new password and the username will be written to the "user.txt" file.
        if reg_passwordConfirm == reg_password:
        
            with open("user.txt","a") as f:
            
                f.write(reg_passwordConfirm)
        
            f.close()              


    # This function contains the code that will run when the option to add a task is chosen.
    def add_tasks():

        task_username = input("Enter the username name of the person the task is assigned to. \n")
        
        print()

        task_title = input("Enter the title of the task. \n")
        
        print()

        task_description = input("Enter the task description. \n")

        # Datetime module used here to display the current date the task is added.
        current_date = datetime.date.today()

        print()

        due_date = input("Enter the due date of the task, in the format DD-MM-YYYY: \n")

        print()

        task_completion = "No"

        # Once all info about the task is stored, it is written to the task file.
        with open("tasks.txt","a") as tf:
            tf.write(task_username + ", " + task_title + ", " + task_description
            + ", " + str(current_date) + ", " + due_date + ", " + task_completion + "\n")
        tf.close()  
    

    def view_all():

        # Opening the file to read its contents.
        with open("tasks.txt","r") as tf:

            tasks = tf.readline()

            while tasks:

                print(tasks)

                tasks = tf.readline()
        
        tf.close()

        
        tf.close() 


    def view_mine():
        
        # Opening the file to read its contents.
        tf = open("tasks.txt","r")

        # This the file that the program will write the user's tasks to.
        ut = open("user_tasks.txt","w")

        while True:

            line = tf.readline()

            if line == "":

                break

            if username in line:

                ut.write(line)

        tf.close()
        ut.close()

        # This is to add the number in which the user will use to access the task for editing.
        line_count = 0
        with open("user_tasks.txt","r") as ut:

            for line in ut:

                line_count += 1

                print(str(line_count) + ". " + (line))

        ut.close()
            
        # Prompting user to enter the number of the task they would like to edit or enter '-1' to exit.
        edit_access = int(input("Enter the number of the task you would like to edit. If you like to exit, enter '-1'. \n"))

        if edit_access == -1:

            login()

        if edit_access != -1:

            with open("user_tasks.txt","r") as ut:

                listed_edit_tasks = ut.readlines()

            ut.close()

            edit_taskIndex = (edit_access - 1)

            print()

            edit_taskline = (listed_edit_tasks[edit_taskIndex])

            print(edit_taskline)

            print()  

            # Prompt choice on what they would like to edit, mark as complete or edit user name and due date.
            update_choice = input("mac - mark task as complete\net - edit the task. \n")

            # If user chooses to mark the task as complete.
            if update_choice == "mac":

                # The "No" will be changed to a "Yes" to indicate that the task has ben completed.
                mark_as_complete = (edit_taskline.replace("No", "Yes"))

                with open("tasks.txt","r") as tf:

                    tasks = ""

                    for i in tf:

                        tasks += i

                tf.close()        

                # The old line that contain the "No" is then replaced with the new line that contains the "Yes".
                updated_task_lines = tasks.replace(edit_taskline, mark_as_complete)

                with open("tasks.txt","w") as tf:

                    tf.write(updated_task_lines)

                tf.close()

            if update_choice == "et":

                # If the user chooses to edit the task, the progrm will check if the task is complete or not.
                # If the task has not been completed, it can be edited.
                # If the user enters 'et' to edit task, they will be asked what they would like to edit.
                if update_choice == "et":

                    # This line checks if the task has been completed or not.
                    task_complete_check = edit_taskline.find("Yes")

                    with open("tasks.txt","r") as tf:

                        tasks = ""

                        for n in tf:

                            tasks += n

                    tf.close()        
                    # If the task has been completed, task cannot be edited.
                    # An error message will be displayed to the user.
                    if task_complete_check != -1:

                        print()

                        print("Task has been completed, therefore cannot be edited.")

                    # If the task has not been completed, the program will continue with prompts.
                    if task_complete_check == -1:
                        
                        print()
                        
                        edit_choice = input("cu - to change username to whom task is assigned\ncd - to change the due date of the task. \n")
                
                        # Here the user can edit the uername of the task.
                        if edit_choice == "cu":

                            print()

                            current_username = input("Enter the current username. \n")

                            print()

                            edit_username = input("Enter the new username. \n")

                            edited_username = edit_taskline.replace(current_username, edit_username)

                            updated_username = tasks.replace(edit_taskline,edited_username)

                            with open("tasks.txt","w") as tf:
                        
                                tf.write(updated_username)
                    
                            tf.close()    

                    # Here the user can edit the due date of the task
                        if edit_choice == "cd":

                            current_due_date = input("Enter the current dute as is. \n")

                            new_due_date = input("Enter the new due date. \n")

                            edited_due_date = edit_taskline.replace(current_due_date, new_due_date)

                            new_dates = tasks.replace(edit_taskline,edited_due_date)

                            with open("tasks.txt","w") as tf:
                                
                                tf.write(new_dates)
                            
                            tf.close()


    def generate_reports():

        # Total number of tasks.
        with open("tasks.txt","r") as tf:
            
            num_of_tasks = 0
            
            for line in tf:
                
                num_of_tasks += 1
        
        tf.close()    
        
        with open("task_overview.txt","a") as to:

            to.write("Total number of tasks generated and tracked using task_manager.py: {}".format(str(num_of_tasks) + "\n"))
    
        to.close()

    
        # Total number of complete tasks.
        with open("tasks.txt","r") as tf:

            num_of_complete_tasks = ""
            
            for i in tf:
                
                num_of_complete_tasks += i
                
                complete_tasks = (num_of_complete_tasks.count("Yes"))    
        
        tf.close()

        with open("task_overview.txt","a") as to:
            
            to.write("Total number of complete tasks: {}".format(str(complete_tasks) + "\n"))
        
        to.close()

        # Total number of incomplete tasks.
        incomplete_tasks = (num_of_tasks - complete_tasks)
 

        with open("task_overview.txt","a") as to:
            
            to.write("Total number of incomplete tasks: {}".format(str(incomplete_tasks) + "\n"))
        
        to.close()

        # Pecentage of tasks that are incomplete.
        percentage_of_incomp_tasks = (incomplete_tasks / num_of_tasks)
        
        with open("task_overview.txt","a") as to:
            
            to.write("{} of the tasks are incomplete".format(format(percentage_of_incomp_tasks, ".0%")))
        
        to.close

    # Opening up the 'task_overview' file to read its contents and display them to the user 
    
        print()

        reports = ""
        
        with open("task_overview.txt","r") as to:
            
            for line in to:
                
                reports += line
            
            print(reports) 
        
        to.close()       


    def generate_stats():

        # Reaching into the file to get the total nunmber of registered users.
        num_of_users = 0
        
        with open("user.txt","r") as f:
            
            for line in f:
                
                num_of_users += 1
        
        f.close()    
    
        # Write the total number of registered users with to 'user_overview.txt'.
        with open("user_overview.txt","a") as uo:
            
            uo.write("Total number of users registered with task_manager.py: {}".format(str(num_of_users) + "\n"))
        
        uo.close()    

        # Getting the total number of tasks.
        with open("tasks.txt","r") as tf:
            
            num_of_tasks = 0
            
            for line in tf:
                
                num_of_tasks += 1
        
        tf.close()    

        # Writig the total number of tasks to 'user_overview.txt'.   
        with open("user_overview.txt","a") as uo:
            
            uo.write("Total number of tasks generated and tracked using task_manager.py: {}".format(str(num_of_tasks) + "\n"))
        
        uo.close()

        # Number of tasks assigned to that user.
        with open("tasks.txt","r") as tf:
            
            tasks_assigned = ""
            
            for line in tf:
            
                tasks_assigned += line
        
        tf.close()

        num_of_tasks_assigned = (tasks_assigned.count(username))

        # Writing total number of tasks assigned to the user, to 'user_overview.txt'.
        with open("user_overview.txt","a") as uo:
            
            uo.write("Total number of tasks assigned to you: {}".format(str(num_of_tasks_assigned) + "\n"))
        
        uo.close()

        # Percentage of tasks that have assigned to user.
        percentage_of_tasks_assigned_to_user = (num_of_tasks_assigned/num_of_tasks)
    
        with open("user_overview.txt","a") as uo:
            
            uo.write("{} of the tasks are assigned to you.".format(format(percentage_of_tasks_assigned_to_user, "0%")))
        
        uo.close()

        # Display the stats to the user.
        with open("user_overview.txt","r") as uo:
        
            statistics = ""
        
            for line in uo:
            
                statistics += line
            
            print(statistics)
        
        uo.close()    


    # If both the username and the password entered by the user are incorrect,
    # an error message will be displayed and they will be prompted again.
    if username_check == -1 and password_check == -1:

        print()

        print("The login details enetered are incorrect.")

        print()

        login()

    # If the username is correct and the password enterd by the user is incorrect,
    # an error message will be displayed and they will be prompted again.
    if username_check != -1 and password_check == -1:
        
        print()

        print("The password entered is incorrect.")

        print()

        login()

    # If the username is incorrect and the password entered by the user is correct,
    # an error message will be displayed and they will be prompted again
    if username_check == -1 and password_check != -1:

        print()

        print("The username entered is incorrect.")

        print()

        login()

    # If both the username and the password entered by the user are correct,
    # the 'password_validity_check' function will be called.
    if username_check != -1 and password_check != -1:

        print()

        password_validity_check()

        print()

        if username == "admin":
            
            time.sleep(2)

            options_menu = input("r - register user\na - add task\nva - view all tasks\nvm - view my tasks\nds - display stats\ngr - generate reports\ngs - generate statistics\ne - exit\n")

        else:
            
            time.sleep(2)   

            options_menu = input("va - view all tasks\nvm - view my tasks\ne - exit\n")
    
        # If the user selects option to register a new user, the 'reg_user" function will be called and executed.
        if options_menu == "r":
            
            print()

            register_username()

        # If the user selects option to add a task, the 'add_task' will be called and excuted.
        if options_menu == "a":

            print()

            add_tasks()

        if options_menu == "va":

            print()
            
            print("Displayed below are all the tasks assigned.")

            print()    

            view_all()

        if options_menu == "vm":

            print()

            view_mine()

        if options_menu == "gr":

            print()

            generate_reports()     

        if options_menu == "gs":

            print()

            generate_stats()
        
login()