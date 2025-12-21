# StudentSphere
### 
#### Video Demo:

## Description

This project is a web-based Student Management System developed using the Flask framework. It
was created to provide teachers with an intuitive and efficient platform for managing student 
information, tracking academic performance, and interacting with a simplified chatbot 
assistance module. The system combines traditional CRUD functionality with modern user-
experience features, including dynamic page loading via AJAX and a modular routing structure.

## Project Objectives
1. To design and implement a web application for managing student records.
2. To provide authenticated access for teachers ensuring data is protected from unauthorized use.
3. To allow teachers to add, view, update and manage student information efficiently.
4. To apply database design principles using a relational database system.

## Source Files
\__init__.py - App factory for app
models.py - Flask SQLAlchemy ORM objects for app's database tables
routes.py - Code for website's routing
index.js - For implementing website's AJAX navigation
edit-students.js - Logic for updating student's records in the database


## Technology Stack
### Backend
Flask - Flask was used as my main web framework because it has a lot of libraries which make development of the website easier.
Flask-SQLAlchemy - I used this for handling the database and it's easily integrated with Flask. It is used as the Object Relational Mapper allowing database operations using Python objects instead of raw SQL queries.

### Frontend
HTML5 - For providing the structure of the various webpages
CSS3 - For designing the webpages
Vanilla JavaScript - To the enable the webpages be interactive and for AJAX navigation

## Hosting
The app and the database are both hosted on render.com. Render offers a free tier which is why opted for it on this project. Due to this the website appears to be a bit laggy sometimes.

## Key Features of the website
1. I used Flask-Login to handle user login.
2. Session-based access control allows only authenticated teacher to access student information.
3. Teachers can add, view, update and delete student profiles
4. Teachers can enter grades for the various subjects (currently set to just English and Math) and the total grade is automatically calculated and updated in the frontend.
5. JavaScript fetch requests submit updates asynchronously.
6. Immediate UI feedback on save, update or delete actions within the student records table.
7. Table layout fully responsive to accomodate all columns
8. CSRF protection to ensure all post requests are not vulnerable to attackers.

### Chatbot Assistant
1. Integrated chatbot panel with predefined set of task options(eg. Add Student, View Students)
2. Chatbot assists teachers by doing some common actions teachers will usually do.
3. Toggle-based "AI-Mode" for extended generative assistance.

## Teacher Dashboard
When teachers are authenticated, they are redirected to a personalized dashboard that provides them with a summary of available student records. This was made to allow the teachers get an overview of the student information.

## Deployment 
The application is deployed on a cloud hosting platform making it accessible over the internet. Deployment configuration includes a production wsgi server (Gunicorn) and automatic database initialization on startup.
This deployment process demonstrates an understanding of transitioning from a local development environment to a production environment.

## Future Work
The current implementation of StudentSpehere only caters to the needs of teachers. Future version will introduce additional user roles such as administrators, school heads and parents to monitor the work of the students and the teachers alike. Another area that will be to provide analytical and reporting tools. The system could be extended to generate performance reports and academic trends over time. Visual dashboards with charts and graphs would provide users with insights into student and teacher performance. Additionally, mobile responsiveness and accessibility can be enhanced. Future versions may include a fully responsive design optimized for mobile devices or a dedicated mobile application. The system could incorporate audit logging and backup mechanisms. Tracking changes made to student records and implementing automated database backups would improve data integrity and reliability, particularly in production environments. In summary, while the current system provides a strong and functional foundation, these future enhancements would transform it into a more comprehensive, scalable, and intelligent student management platform suitable for broader institutional use.

## Conclusion
StudentSphere is meant to demonstrate practical application of web development concepts using Python and Flask. It addresses a real-world problem by digitizing student data especially in my country Ghana where majority of student data entry is still paper based.
Overall, this project serves as a strong foundation for future enhancements, such as advanced reporting, expanded user roles, or more intelligent assistant features, and represents a meaningful academic and technical achievement.








