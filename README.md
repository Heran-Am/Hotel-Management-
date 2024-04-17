# Hotel_Management
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


## 1. Git 
My experience on GitHub as a beginner has been enriching. Through exploration and experimentation, I've delved into the world of version control, discovering the power of collaborative development. With each commit, push, and pull request, I've gained invaluable insights and honed my skills. As I continue this journey, I look forward to further growth and contribution within the vibrant GitHub community.

## 2. UML


 ## 3. DDD
In my project, I embraced Domain-Driven Design (DDD) because it emphasizes understanding the core domain, setting clear boundaries, and fostering collaboration through shared language.

To kicked off the project, I organized a brainstorming session [brainstorming session](DDD/brainstorming.png) where we outlined our goals and features collaboratively. Techniques like mind mapping helped us generate ideas and prioritize requirements, laying the groundwork for our development plan.

  Next, I dived deep into understanding key domain concepts, aiming for clarity and insight. This informed better decision-making as we moved forward.

With a solid grasp of domain ideas [DDD](DDD/domainideas.png), I focused on developing a 'ubiquitous language' [ubiquitous language](DDD/domainUbiquitious%20language.png) shared vocabulary for smooth communication and understanding among team members.

To visualize our project's structure, I created a context map [context map](DDD/content%20mapping.png), outlining key content and its relationships. This served as a visual roadmap for our development journey.

Finally, I distilled our core domain into a chart, providing a clear overview of its components and interactions. [Core domain](DDD/core%20domain.png)


## 4.Metrics
These are the metrics listed below :


Quality Gate Status(Passed):[Status](https://sonarcloud.io/summary/new_code?id=Heran-Am_Hotel-Management-)

Maintainability(0 Code Smells):[Maintainability Rating](https://sonarcloud.io/component_measures?metric=Maintainability&id=Heran-Am_Hotel-Management-)

Duplications(Duplicated Lines (%)0.0%):[Duplications](https://sonarcloud.io/component_measures?id=Heran-Am_Hotel-Management-&metric=new_duplicated_lines_density&view=list)
Security (0 Vulnerabilities)(A):[Review](https://sonarcloud.io/component_measures?metric=Security&id=Heran-Am_Hotel-Management-)

Security Review(0 Security Hotspots)(A):[Review](https://sonarcloud.io/component_measures?metric=new_security_hotspots&id=Heran-Am_Hotel-Management-)
Reliability Rating(0 Bugs)(A): [Rating](https://sonarcloud.io/component_measures?metric=new_bugs&id=Heran-Am_Hotel-Management-)

![Screenshot 2024-03-30 170410]()

![passed](https://github.com/Heran-Am/hotel_managment/assets/149790376/abf383c3-e54d-414f-9919-53d43d1c280b)


## 5. Clean Code Development
Clean code Developement [Cheatsheet](https://github.com/Heran-Am/Hotel-Management-/blob/main/cheatsheet.txt) is here and example from the code.

Comments/Doctstrings : Use Docstrings or comments to explain the function/methods.

Modularity: The code is structured into smaller components for improved. Indentation, spacing, and line breaks are used effectively to enhance code quality. 

DRY (Don't Repeat Yourself): Reusable functions, modules, or libraries can help prevent code [duplication](https://sonarcloud.io/component_measures?id=Heran-Am_Hotel-Management-&metric=duplicated_lines_density&view=list). In sonarcloud metrics, we can see no duplication Duplicated Lines.

Unittest: There is a also comprehensive unit test [Unittest](https://github.com/Heran-Am/Hotel-Management-/blob/main/test.py)

[Readability](https://sonarcloud.io/component_measures?metric=Reliability&id=Heran-Am_Hotel-Management-): Make the code easy to read and understand. Avoid long lines of code that require horizontal scrolling.

## 6. & 7. Build and CI/CD  Workflow

As points 6 and 7 seamlessly integrate into my development process. Leveraging GitHub Actions for build and Continuous Integration/Continuous Deployment (CI/CD) has been a game-changer. Since my project is in Python, GitHub Actions felt like the natural choice. While other build management systems like Ant, Maven, and Gradle are more commonly associated with Java projects, I found GitHub Actions to be a perfect fit for Python.


[Test](https://github.com/Heran-Am/Hotel-Management-/blob/main/test.py): Unit tests and integration tests play a crucial role in ensuring the quality and reliability of our codebase. GitHub Actions empowers me to execute these tests seamlessly, catching bugs before they become problems. The CI/CD pipeline defined in a YAML-based configuration file within my GitHub repository keeps everything organized and efficient.


[Build](https://github.com/Heran-Am/Hotel-Management-/actions/runs/8711759514/job/23896578005): Our pipeline handles everything from compiling source code to bundling assets and generating artifacts for deployment. But it wasn't all smooth sailing – during testing, I encountered some stubborn error messages that brought the pipeline to a halt. With persistence and determination, I tackled each issue head-on, refusing to give up until the tests passed. It was a journey of trial and error, but in the end, it was worth it.

GitHub Actions enables us to set up CI/CD pipelines directly within our GitHub repository, streamlining our development process and ensuring that our code is always in top shape.github/workflows directory of my GitHub repository..[ymlfile](https://github.com/Heran-Am/Hotel-Management-/blob/main/.github/workflows/python-publish.yml)





Functional Programming
The functional_programming.py file contains functions that demonstrate functional programming concepts such as filtering and mapping over guest data.

Data Storage Layer (DSL)
The Dsl.py file implements the Data Storage Layer, providing functions to handle hotel data storage and retrieval.

Contributors





