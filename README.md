
•Purpose of the software development process
Using Agile as the software development process. The reason for using Agile is to release new releases constantly so that users can give more feedback, improve quality and maximize resources. The target market for this software is likely people who enjoy word games and puzzles, The target market for this software is likely people who enjoy word games and puzzles, such as children or adults who want to challenge their language and creativity skills. The software could also be used for educational purposes, such as teaching language arts or vocabulary, or for entertainment purposes.
•Development Process
Requirements gathering:
The first step would be to gather requirements for the Mad Libs game. This could involve discussions with stakeholders or end users to determine the desired features and functionality of the game. Based on the requirements, the developer could determine the necessary inputs, outputs, and logic for the game.

Design:
The next step would be to design the GUI and overall architecture of the game. This would involve creating a mockup of the user interface, as well as planning the data structures and algorithms necessary for the game logic. The developer could use a tool like Sketch, Figma or Adobe XD to create the UI mockup.

Implementation:
The code could be implemented using Python and the tkinter library for GUI.  The developer could start by creating the input fields, radio buttons, and buttons for the GUI.  They would also define the default values for each input field and the stories for each difficulty level. The developer would then create the generate_story() function, which would retrieve user input values, select a random story based on the difficulty level, and display the story in the output label.  They would also create the save_story() function to save the generated stories to a file. The start_game() function would be responsible for clearing the input fields, hiding the timer label, and enabling/disabling the generate button based on the selected difficulty level.  Finally, the start_timer() and update_timer() functions would be responsible for starting and updating the timer for the hard difficulty level.

Testing:
Testing would involve manually testing the GUI and game logic to ensure that it meets the requirements and functions correctly. The developer could also use automated testing tools like pytest to automate testing and ensure that the code is robust and error-free.

Deployment:
Once the code has been tested and finalized, it could be deployed to end users.  This could involve packaging the code as an executable or distributing it as a Python script. The developer could also create documentation or user guides to help users understand how to use the game.

Maintenance:
After deployment, the developer would need to maintain the code by fixing bugs and adding new features as necessary. They would also need to update the code to ensure that it remains compatible with new versions of Python and the tkinter library.

• Members (Roles & Responsibilities & Portion)
Billy: project manager
Liyus: software developer 
Kyler: user experience designer
Leo: quality assurance analyst
Billy: technical writer
• Schedule

We have to start this project in April then after six months we have to finish the project the deadline is in October, we estimate the project resource use 5 people and 5 devices each person’s salary is 1000 dollars per month and the device cost is 1000 dollars each one so it is 5000 dollars and we temporarily didn't need to sever something like that so our cost is 35000 dollars to develop this project.
•Algorithm
1.Define the Mad Libs stories for each difficulty level:
Create a list of easy, medium, and hard stories, each containing a string with placeholders for user input values.
2.Define the default values for each input field:
Create a dictionary of default input values for each input field.
3.Define the timer duration (in milliseconds) for the hard difficulty level:
Set a variable to the duration of the timer in milliseconds.
4.Define the generate_story() function:
Retrieve user input values from the input fields.
Select a random story based on the difficulty level and replace the placeholders with the user input values.
Display the generated story in the output label.
Save the generated story to a file using the save_story() function.
5.Define the save_story() function:
Open a file in append mode.
Write the generated story to the file.
Close the file.
6.Define the start_game() function:
Clear the input fields and output label.
Hide the timer label.
Disable the generate button until the difficulty level is selected.
Enable the generate button and start the timer (if applicable) when the difficulty level is selected.
7.Define the start_timer() function:
Set a global variable to the duration of the timer in seconds.
Update the timer label with the remaining time.
Schedule the update_timer() function to be called every second.
8.Define the update_timer() function:
Decrement the global timer variable by 1.
Update the timer label with the remaining time.
If the timer has expired, cancel the timer and call the generate_story() function.
Otherwise, schedule the update_timer() function to be called again in one second.
9.Create the main window and GUI elements:

• Current status of your software
The current status of our software is in the maintenance phase, we need to performance optimization, user interface design, and improve the simple interface.
• Future plan
The future plan is to develop account functions in the future to record the problems we have done and publish functions, we can share the problems you have completed with the in-game community for others to enjoy.

Demo link:https://youtu.be/OYs98zKJRSI
