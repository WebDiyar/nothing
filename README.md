1) ![image](https://github.com/user-attachments/assets/0f494b78-2ae0-4164-800a-6214535c4ea6)
2) ![image](https://github.com/user-attachments/assets/6a3dfa98-cb9c-4229-911d-e8ffd1232e42)
3) ![image](https://github.com/user-attachments/assets/bc2f2c39-88fd-486a-b47c-d12a27e3ba9e)
4) ![image](https://github.com/user-attachments/assets/a2ecd3e3-6f15-43e9-ae42-745128844ee1)
5) ![image](https://github.com/user-attachments/assets/7d404214-aa6e-44b6-ab46-3f3671d3dee5)

6)**User Roles Availability Requirements**
Users must be able to register, update, and delete accounts.
Admins should have the ability to approve or deactivate user accounts.
Role-based access control (RBAC) must be implemented to define permissions for different user types (students, instructors, admins).
**Security Requirements**
User data should be encrypted at rest and in transit.
Two-factor authentication (2FA) should be required for admin accounts.
The system should log all access and modifications to maintain an audit trail.
**Compatibility Requirements**
The platform should be accessible via both web and mobile devices.
Cloud-based infrastructure should be used to enhance accessibility.
API integration with video conferencing tools should be supported.
**Course Management**
Instructors should be able to create, edit, and delete courses.
Courses should support multiple content formats, including videos, text, quizzes, and assignments.
The system should track student progress and course completion.
**User Management**
Users should be able to register, update, and delete their accounts.
Admins should be able to approve or deactivate user accounts.
Role-based access control (RBAC) should be implemented to manage permissions.
**Performance Requirements**
The platform should provide a smooth and engaging learning experience.
The system should scale efficiently to support a large number of users.
Content delivery should be optimized for fast loading times and minimal latency.
**Assessment and Grading**
The system should support quizzes, assignments, and exams.
Instructors should be able to manually grade assignments.
Automated grading should be available for multiple-choice assessments.
**Operational Constraints**
The system must comply with data protection regulations (e.g., GDPR, HIPAA if applicable).
Maintenance and updates should be scheduled without disrupting user activities.
The platform should ensure high uptime and availability through cloud-based hosting.
7)

8)
private int intEmployeeID; // Hungarian Notation (int prefix for Integer)

public Employee(int employeeID, String firstName, String lastName, String ssn, Date dob, String pin) // Pascal Case (Constructor)

public void setEmployeeID(int employeeID) { this.intEmployeeID = employeeID; } // Hungarian Notation for field

private String strDepartmentName; // Hungarian Notation (str prefix for String)

private String strCEO; // Hungarian Notation (str prefix for String)

private String strCTO; // Hungarian Notation (str prefix for String)

public void AddDepartment(Department department) // Pascal Case (Method, should be `addDepartment` in Java convention)

9)
![image](https://github.com/user-attachments/assets/e4f0540d-30c2-422e-8227-078ee110b95c)

10)

A: Syntax Error Bug
Reason: In the constructor, the assignment to dblOrderTotal is missing a semicolon.

B: Logical Error Bug
Reason: The discount is applied using addition instead of subtraction.

C: OK Case
Reason: All operations are implemented correctly without errors.

D: Uninitialized Field Bug
Reason: The field dblOrderTotal is never assigned a value in the constructor.

E: Method Call Error Bug
Reason: The main method calls CalcFinalPrice() which does not exist (the method is named CalculateFinalPrice()).

F: Method Call Error Bug
Reason: The main method calls a non-existent method substract instead of the correct subtract.

G: Uninitialized Field Bug
Reason: The local variable dblResult in the subtract method is declared but never initialized.

H: Logical Error Bug
Reason: The multiply method incorrectly performs addition instead of multiplication.

I: OK Case
Reason: All methods work as expected without any errors.

J: Syntax Error Bug
Reason: The add method is missing a semicolon after the return statement.
