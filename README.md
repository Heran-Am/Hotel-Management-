# Hotel-Management
This is a simple project about Hotel management system with python using object-oriented programming (OOP) and functional programming concepts.

## General
The Hotel Management System offers a user-friendly interface for efficient hotel operations. Key features include:

- User-Friendly Interface: Intuitive GUI for easy navigation and task execution.

- Efficient Data Management: Stores and manages guest information effectively.

- Functional Programming: Utilizes functional programming concepts for enhanced code readability.

- Data Storage Layer (DSL): Handles data storage and retrieval, ensuring reliability.

- Flexible and Extensible: Easily customizable to adapt to changing needs.

- Open-Source: Source code available for modification and distribution.

## Features

- Check-in: Add guests to the hotel database with their details.
- Check-out: Remove guests from the hotel database.
- List Guests: View a list of all guests currently staying at the hotel.
- Get Guest Info: Retrieve detailed information about a specific guest.
- Generate Receipt: Generate a receipt for a guest.
- [GUI](https://github.com/Heran-Am/Hotel-Management-/blob/main/pictures/GUI.png)
- [GUI2](https://github.com/Heran-Am/Hotel-Management-/blob/main/pictures/GUII.png)


## 1. Git 
My experience on GitHub as a beginner has been enriching. Through exploration and experimentation, I've delved into the world of version control, discovering the power of collaborative development. With each commit, push, and pull request, I've gained invaluable insights and honed my skills. As I continue this journey, I look forward to further growth and contribution within the vibrant GitHub community.

## 2. UML

I have use three diagrams for this project and those diagrams are,
- [Class diagram](https://github.com/Heran-Am/Hotel-Management-/blob/main/UML/Class%20diagram.png)
- [Sequence diagram](https://github.com/Heran-Am/Hotel-Management-/blob/main/UML/Hotel%20Management%20System%20-%20Sequence%20Diagram%20-%20Room%20Booking.jpg)
- [Usecase diagram](https://github.com/Heran-Am/Hotel-Management-/blob/main/UML/Usecasediagram.png)


 ## 3. DDD
In my project, I embraced Domain-Driven Design (DDD) because it emphasizes understanding the core domain, setting clear boundaries.

To kicked off the project, I organized a brainstorming session [brainstorming session](https://github.com/Heran-Am/Hotel-Management-/blob/main/DDD/brainstorming.png) where I outlined my goals and features collaboratively. Techniques like mind mapping helped me generate ideas and prioritize requirements, laying the groundwork for my development plan.

  Next, I dived deep into understanding key domain concepts, aiming for clarity and insight. This informed better decision-making as I moved forward.

With a solid grasp of [domain ideas ](https://github.com/Heran-Am/Hotel-Management-/blob/main/DDD/DomainIdeas.png).


Finally, I distilled our core domain into a chart, providing a clear overview of its components and interactions. [Core domain](https://github.com/Heran-Am/Hotel-Management-/blob/main/DDD/CoreDomain.png)


## 4.Metrics
These are the metrics listed below :


Quality Gate Status(Passed):[Status](https://sonarcloud.io/summary/new_code?id=Heran-Am_Hotel-Management-)

Maintainability(0 Code Smells):[Maintainability Rating](https://sonarcloud.io/component_measures?metric=Maintainability&id=Heran-Am_Hotel-Management-)

Duplications(Duplicated Lines (%)0.0%):[Duplications](https://sonarcloud.io/component_measures?id=Heran-Am_Hotel-Management-&metric=new_duplicated_lines_density&view=list)
Security (0 Vulnerabilities)(A):[Review](https://sonarcloud.io/component_measures?metric=Security&id=Heran-Am_Hotel-Management-)

Security Review(0 Security Hotspots)(A):[Review](https://sonarcloud.io/component_measures?metric=new_security_hotspots&id=Heran-Am_Hotel-Management-)
Reliability Rating(0 Bugs)(A): [Rating](https://sonarcloud.io/component_measures?metric=new_bugs&id=Heran-Am_Hotel-Management-)


![passed](https://github.com/Heran-Am/Hotel-Management-/blob/main/pictures/Screenshot%202024-03-30%20170410.png)


## 5. Clean Code Development
Clean code Developement [Cheatsheet](https://github.com/Heran-Am/Hotel-Management-/blob/main/cheatsheet.txt) is here and example from the code.

Comments/Doctstrings : Use Docstrings or comments to explain the function/methods.

Modularity: The code is structured into smaller components for improved. Indentation, spacing, and line breaks are used effectively to enhance code quality. 

DRY (Don't Repeat Yourself): Reusable functions, modules, or libraries can help prevent code [duplication](https://sonarcloud.io/component_measures?id=Heran-Am_Hotel-Management-&metric=duplicated_lines_density&view=list). In sonarcloud metrics, we can see no duplication Duplicated Lines.

Unittest: There is a also comprehensive unit test [Unittest](https://github.com/Heran-Am/Hotel-Management-/blob/main/test.py)

[Readability](https://sonarcloud.io/component_measures?metric=Reliability&id=Heran-Am_Hotel-Management-): Make the code easy to read and understand.

## 6. & 7. Build and CI/CD  Workflow

As points 6 and 7 seamlessly integrate into my development process. Leveraging GitHub Actions for build and Continuous Integration/Continuous Deployment (CI/CD) has been a game-changer. Since my project is in Python, GitHub Actions felt like the natural choice.

[Test](https://github.com/Heran-Am/Hotel-Management-/blob/main/test.py):  GitHub Actions empowers me to execute these tests seamlessly, catching bugs before they become problems. The CI/CD pipeline defined in a YAML-based configuration file within my GitHub repository keeps everything organized and efficient.
![test](https://github.com/Heran-Am/Hotel-Management-/blob/main/pictures/test.png)


[Build](https://github.com/Heran-Am/Hotel-Management-/actions/runs/8711759514/job/23896578005): My pipeline handles everything from compiling source code to bundling assets and generating artifacts for deployment.
![buil](https://github.com/Heran-Am/Hotel-Management-/blob/main/pictures/testbuild.png)

GitHub Actions enables me to set up CI/CD pipelines directly within my GitHub repository, streamlining our development process and ensuring that my code is always in top shape.github/workflows directory of my GitHub repository..[ymlfile](https://github.com/Heran-Am/Hotel-Management-/blob/main/.github/workflows/python-publish.yml)

## 8. Unitest
I have written two unitest 
1, test_import:

Purpose: This test ensures that the module getinfoui is imported successfully.
Assertion: It checks if the imported module getinfoui is not None.

And the Second unitest
2, test_hotel_management_class_exists:

Purpose: This test verifies if the HotelManagementApp class exists in the imported module.
Assertion: It checks if the getinfoui module has an attribute named 'HOTEL_MANAGEMENT', which should correspond to the HotelManagementApp class.

here is the [unitest](https://github.com/Heran-Am/Hotel-Management-/blob/main/test.py)


## 9. IDE

I've opted for Visual Studio as my IDE for this project for several reasons. It offers a rich set of features and tools essential for software development.
Here are some of my favorite shortcuts in Visual Studio:

1.Ctrl + D: Duplicate line or selection.

2.Ctrl + /: Toggle line comment.

3.Ctrl + Shift + K: Delete line.

4.Ctrl + Shift + P: Open command palette. 

5.Ctrl + F5: Run without debugging.

6.Ctrl + F9: Toggle breakpoint.

These shortcuts help streamline my coding workflow and boost productivity in Visual Studio.


## 10. DSL (Data Storage and Loading)
The DSL.py module provides functionality for storing and loading data used in the hotel management application. It includes the following functions:

####1. save_guest_data(guest_data):

Saves guest data to the "hotel.dat" file using pickle serialization.
Parameters: guest_data (list) - List of guest objects to be saved.
Exceptions: Handles FileNotFoundError if the "hotel.dat" file is not found.
load_guest_data():

####2. Loads guest data from the "hotel.dat" file.
Returns: List of guest objects loaded from the file.
Exceptions: Handles FileNotFoundError if the "hotel.dat" file is not found.
save_receipt_data(receipt_data):

####3. Saves receipt data to the "receipt.txt" file.
Parameters: receipt_data (list) - List of strings representing receipt lines.
Exceptions: Handles FileNotFoundError if the "receipt.txt" file is not found.
load_receipt_data():

####4. Loads receipt data from the "receipt.txt" file.
Returns: List of strings representing receipt lines loaded from the file.
Exceptions: Handles FileNotFoundError if the "receipt.txt" file is not found.
These functions are essential for managing the persistence of guest and receipt data within the application.

[Click here](https://github.com/Heran-Am/Hotel-Management-/blob/main/DSL.py)


## 11. Functional Programming
The functionalprogramming.py module contains functions that leverage functional programming techniques to interact with guest data stored in the hotel management application.

***1. filter_guests_by_room(room_number):

*Filters guest data by room number.
*Parameters: room_number (str) - The room number to filter by.
*Returns: List of guest objects filtered by the specified room number.
*calculate_total_bill(guest_name):

***2. Calculates the total bill for a guest.
*Parameters: guest_name (str) - The name of the guest.
*Returns: Total bill amount for the specified guest.
*generate_receipt(guest_name):

***3. Generates a receipt for a guest.
*Parameters: guest_name (str) - The name of the guest.
*Returns: List of strings representing the receipt details for the specified guest.

These functions are designed to provide convenient ways to extract and manipulate guest data within the hotel management system using functional programming paradigms.
[Clickhere](https://github.com/Heran-Am/Hotel-Management-/blob/main/functinal_programming.py)




