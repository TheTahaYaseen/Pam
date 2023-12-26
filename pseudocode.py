
# PAM Or Project Assistant Manager

"""

PS: For Now, It Will Be Single Consumer Based But Later, To Be Organization Level    
    As Organizations Can Divide Tasks Or Projects Among Branches
    Which Can Further Divide Among Teams 
    & Then, To Assign Those To Single Personel 
    And The Person Can Divide It To Make it Easier To Manage For Himself 

: To Manage My Projects

(With All The CRUD Operations)
- Project  
- Todos

"""

# Data / Models 

"""

Auth: Username & Password

Projects: Name, Abbreviation(If Any), Description, Creator(User), Status & Progress, Deadline(If Any), Pseudocode & Interdependency(If On Other Projects)
Todos: Task, Detail, Status & Progress, Associated(Project), SubTaskOf(If Is), Creator(User), Deadline(If Any) & Interdependency(If On Other Tasks)

"""

# User Flow

"""

Authentication (If Not) ->

Navigation
    -> Home
    -> Projects
    -> Todos

Layout
    -> General Standard Layout
    -> Navigation

- All Below Will Follow The Layout -

Delete Template 
    -> Some Confirmation And A Form To Submit

Home
    -> Some Todos Of Projects You Can Tackle (Sorted By Urgency And Status & Progress)
    -> Some Projects (Sorted By Urgency And Status & Progress)

Projects
    -> Create Project 
    
    -> All The Projects (Sorted By Urgency And Status & Progress)
        -> For Each Project; Project Component

Project Component
    -> Update & Delete Button
    -> Project Name & Abbreviation
    -> Status & Progress, Deadline And Interdependency
    -> Project Description
    -> Create Todo
    -> Todos
    
Create And Update Project
    -> Creator To Be Fetched From Request
    -> Inputs For All Of The Project Data With Proper Validation

Delete Project 
    -> Following Delete Template, Deleting The Project

Todos (Will Also Used Within Project Layouts) 

    -> All The Todos You Can Tackle (Sorted By Urgency And Status & Progress)
        -> For Each Task; Task Component

Todo Component 
    -> Update And Delete Button
    -> Task & Subtask Of
    -> Status & Progress, Deadline And Interdependency
    -> Task Details

Create And Update Todo
    -> Creator To Be Fetched From Request
    -> Associated Project & Sub Task Of To Be Fetched From Url 
    -> Inputs For All Of The Task Data With Proper Validation

Delete Todo 
    -> Following Delete Template, Deleting The Todo

"""

# User Interface

"""

: To Be Made In The Web (Only)

Color Scheme;

Came From Batman -> 
    #574d4e
    #968b8a
    #e1d7dd

Just Make It Rather Simple For Now

"""

# Backend APIs In Django

"""

: To Be Divided In Different Apps

"""