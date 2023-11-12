# To-Do-List
To-Do List Application Overview:  This To-Do List Application is a simple console-based task management system that allows users to add, display, mark tasks as completed, update, and remove tasks. The application is written in Python and provides a user-friendly interface for managing tasks.

Components:
Task Structure:

Each task has the following attributes:
Description
Due Date
Priority
Completion Status
Functions:

Add Task (add):

Adds a new task to the to-do list with the provided description, due date, and priority.
Display Tasks (Display):

Prints a formatted list of all tasks, including their descriptions, due dates, priorities, and completion status.
Complete Task (Complete_task):

Marks a task as completed and moves it to the completed tasks list.
Update Task (Update):

Modifies the description, due date, and priority of a task based on the user's input.
Remove Task (Remove):

Removes a task from the to-do list based on the user's input.
Usage:
Adding a Task:

Users can add a task by providing a description, due date, and priority.
Displaying Tasks:

The application can display all tasks, showing their descriptions, due dates, priorities, and completion status.
Marking a Task as Completed:

Users can mark a task as completed, and the application moves it to the completed tasks list.
Updating a Task:

Users can update a task by providing the task index and new information for description, due date, or priority.
Removing a Task:

Users can remove a task from the to-do list by specifying the task index.
Exiting the Application:

Users can exit the application by choosing the exit option.
Implementation Details:
The application uses a list to store tasks and a separate list for completed tasks.
Task information is stored as dictionaries with keys for description, due date, priority, and completion status.
Input validation is implemented to handle invalid task indices and user choices.
Future Improvements:
Adding date validation to ensure that due dates are in the correct format.
Implementing a more sophisticated priority system (e.g., high, medium, low).
Saving tasks to a file to persist data between application runs.
Adding user authentication for personalized to-do lists.
Overall, this To-Do List Application provides a basic yet functional task management system that can be extended and improved based on user needs and preferences.
