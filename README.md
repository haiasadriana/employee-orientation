# employee-orientation
The employee orientation web application aims to ease the orientation process of the new employees, as it is an essential process for every organization. 
An MVP employee orientation platform would:
- store the orientation documentation
- make the documentation available to the new employees
- track the progress of the training/see the status of the training

## User categories:
- admin (HR)
- mentor 
- employee

## User Flows:

An admin can add mentors and employees and assign a new employee to a mentor.

A mentor uploads and assigns documentation to the employees assigned to him. He must be able to see the status of a training session of an employee (Pending, In Progress, Completed). The mentor also sets deadlines (due dates) for completing the training. 

An employee must be able to access his training documentation, to see the start and due date.

## Entities and relationships between them
Models:
1. Mentor: mentorId, firstName, lastName, assignedProject, email, phoneNumber.
2. Employee: employeeId, firstName, lastName, position, assignedProject, trainingName, email, phoneNumber.
3. Projects: projectId, startDate, endDate, positions.
4. Training: trainingId, name, startDate, endDate.
5. Training status: statusId, name.

A project can have only a mentor, but many employees. An employee can work on a project and attend multiple trainings related to it. A training can have a single status.
