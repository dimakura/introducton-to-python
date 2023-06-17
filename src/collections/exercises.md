# Exercises

## 1. Student grades

Create an empty dictionary `grades`. Ask user to enter name of a student and his grade. Add student name and grade to the `grades` dictionary as a key-value pair.

Ask user if he wants to enter another student. If he enters `"yes"`, repeat the process, otherwise print the `grades` dictionary and exit the program.

If user enters grade less than `1` or greater than `5`, print message "Grade is not in range".

If user enters name of a student that already exists in the list, print message "Student already exists". Give an option to the user to overwrite existing grade or to enter new name.

## 2. Student grades 2

Rewrite program from the previous exercise but use a list instead of a dictionary. Put student name and grade in a tuple and append it to the list.

## 3. Job match

We have a list of requiements for a job:

```python
requirements = ["Python", "C++", "Math"]
```

Allow user to enter his skills into another list.

Now compare list of skills which user has to the list of requirements. Print message "You are hired" if user has at lease two matching skills, otherwise print message "Sorry, you are not hired".
