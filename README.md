# employee-orientation
The employee orientation web application aims to ease the orientation process of the new employees, as it is an essential process for every organization. 
An MVP employee orientation platform would:
- store the orientation documentation
- make the documentation available to the new employees
- track the progress of the training/see the status of the training

## User categories:
- admin (HR)
- employee

## User Flows:

An admin can add projects and employees. 

An admin uploads and assigns documentation to the employees and sets deadlines to projects and trainings. He must be able to see the status of a training session of an employee (Pending, In Progress, Completed). The mentor also sets deadlines (due dates) for completing the training. 

An employee must be able to access his training documentation, to see the start and due date.

## Entities and relationships between them
Models:
1. Employee: firstName, lastName, assignedProject, position, trainingName, email, phoneNumber, username, password.
3. Project: name, startDate, endDate, trainingNeeded.
4. Training: name, startDate, endDate, trainingStatus.
5. TrainingMaterial: name, materialResource, trainingName.

A project can have many trainings. An employee can work on a project and attend multiple trainings related to it. A training can have a single status.
