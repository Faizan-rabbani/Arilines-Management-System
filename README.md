# ✈️ Airlines Management System

A web-based Airlines Management System developed using **Python and Django** to organize and manage airline operations, including flights, passengers, bookings, airports, aircraft, employees, flight crews, tickets, payments, routes, and schedules.

The project demonstrates the development of a centralized airline management application using Django, relational database concepts, and web technologies.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Database Management](#-database-management)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [How to Run](#-how-to-run-the-project)
- [Application Workflow](#-application-workflow)
- [Benefits and Applications](#-benefits-and-applications)
- [Learning Outcomes](#-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Collaborators](#-collaborators)
- [Developer](#-developer)
- [License](#-license)

---

## 📖 Project Overview

The Airlines Management System is a Django-based web application designed to simplify the management of airline-related information.

Airline operations involve several interconnected activities, such as managing flights, maintaining passenger records, assigning aircraft, organizing employees, handling bookings, and maintaining ticket and payment information.

Managing these operations separately can create difficulties in maintaining accurate and organized records.

This project provides a centralized system where different airline entities can be managed through a structured database and a web-based interface.

It uses Django's Model-View-Template architecture and SQLite database to handle application data and operations.

## 🎯 Project Objectives

The main objectives of this project are:

- To develop a centralized airline management application.
- To organize flight and passenger information.
- To simplify airline record management.
- To maintain relationships between different airline entities.
- To manage bookings, tickets, and payment records.
- To organize employee and flight crew information.
- To implement database operations using Django ORM.
- To understand real-world web application development.

## ✨ Key Features

### 1. Flight Management
- Maintain flight information.
- Add, view, update, and delete flight records.
- Manage flight numbers and timings.
- Associate flights with airports and aircraft.

### 2. Passenger Management
- Maintain passenger records.
- Store passenger information.
- Manage passport-related information.
- Update and view passenger details.

### 3. Booking Management
- Maintain passenger bookings.
- Associate passengers with flights.
- Store booking information and dates.
- Manage booking records.

### 4. Airport Management
- Maintain airport information.
- Store airport names and locations.
- Manage airport records.

### 5. Aircraft Management
- Maintain aircraft information.
- Store aircraft models.
- Manage aircraft seating capacity.
- Associate aircraft with flights.

### 6. Employee Management
- Maintain employee information.
- Store employee positions and salaries.
- Organize employee records.

### 7. Flight Crew Management
- Assign employees to flights.
- Maintain crew information.
- Manage crew roles and assignments.

### 8. Ticket Management
- Maintain flight ticket information.
- Manage seat numbers.
- Associate tickets with flights and passengers.

### 9. Payment Management
- Maintain payment records.
- Store payment amounts and dates.
- Record payment methods.

*Note: Payment management refers to maintaining payment records and does not imply live payment gateway integration.*

### 10. Route Management
- Maintain flight routes.
- Manage departure and arrival airports.
- Store route-related information and distances.

### 11. Flight Schedule Management
- Maintain flight schedules.
- Manage departure and arrival timings.
- Associate schedules with flights.

### 12. User Management
- Manage application users.
- Support authentication through Django's authentication facilities.
- Provide a structured application environment.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django 5.1.1 | Web application framework |
| SQLite | Database management |
| Django ORM | Database operations |
| HTML5 | Web page structure |
| CSS3 | Interface styling |
| JavaScript | Frontend interactions |
| Django Templates | Dynamic web pages |

## 🗄️ Database Management

The project uses **SQLite** as its database.

Django ORM is used to interact with the database through Python models rather than writing SQL queries for every operation.

### Main Database Entities

| Entity | Description |
|---|---|
| Employee | Employee information |
| FlightCrew | Flight crew assignments |
| Airport | Airport information |
| Aircraft | Aircraft details and capacity |
| Flight | Flight information |
| Passenger | Passenger records |
| Booking | Flight booking records |
| Ticket | Ticket and seat information |
| Payment | Payment records |
| Route | Flight route information |
| Schedule | Flight scheduling information |

### Database Relationships

The database is designed to connect different airline entities.

- Flights are associated with departure and arrival airports.
- Flights are associated with aircraft.
- Passengers can have booking records.
- Bookings connect passengers and flights.
- Flight crew records connect employees with flights.
- Tickets maintain flight and passenger-related information.
- Payment records are associated with ticket transactions.
- Routes connect airports.
- Schedules are associated with flights.

These relationships help maintain consistency and organize information across the application.

---

## 📁 Project Structure

```text
Arilines-Management-System/
│
├── Airlines/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── DataBase/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── ...
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation and Setup

Follow these instructions to run the project on your local machine.

### Prerequisites

Make sure you have installed:

- Python 3.10 or later
- pip
- Git
- Visual Studio Code or another code editor

### Step 1: Clone the Repository

```bash
git clone https://github.com/Faizan-rabbani/Arilines-Management-System.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Arilines-Management-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux and macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Django

```bash
pip install Django==5.1.1
```

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator credentials.

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

## 🚀 How to Run the Project

After starting the Django development server, open your browser and visit:

```text
http://127.0.0.1:8000/
```

The application will run locally on your machine.

---

## 🔄 Application Workflow

The general application workflow consists of the following steps:

1. Access the airline management application.
2. Manage airport and aircraft information.
3. Create and maintain flight records.
4. Organize routes and flight schedules.
5. Maintain passenger information.
6. Create and manage flight bookings.
7. Maintain ticket information.
8. Manage payment records.
9. Organize employee and flight crew assignments.
10. Maintain centralized airline records.

---

## 💡 Benefits and Applications

This project demonstrates how a centralized management system can improve the organization of airline information.

### Benefits

- **Centralized Information:** Keeps airline records organized in one application.
- **Better Data Management:** Maintains relationships between different airline entities.
- **Reduced Manual Work:** Makes record management easier through a web interface.
- **Improved Organization:** Separates flights, passengers, bookings, employees, and other records.
- **Database Integration:** Demonstrates how multiple related entities work together.
- **Maintainability:** Uses Django's structured application architecture.

### Real-World Applications

The concepts used in this project can be applied to:

- Airline administration systems.
- Airport management applications.
- Flight scheduling platforms.
- Passenger information systems.
- Booking and ticket management systems.
- Employee and crew management applications.
- Database-driven business applications.

## 🎓 Learning Outcomes

Developing this project provides practical experience in:

- Python programming.
- Django web development.
- Model-View-Template architecture.
- Relational database design.
- Django ORM.
- CRUD operations.
- Database relationships.
- Form handling and validation.
- Web application architecture.
- Collaborative software development.
- Git and GitHub version control.

---

## 🔮 Future Improvements

The system can be enhanced with additional functionality:

- Online flight search and booking.
- Real-time seat availability.
- Automated ticket generation.
- PDF ticket downloads.
- Email booking confirmations.
- Online payment gateway integration.
- Role-based access control.
- Advanced dashboard and analytics.
- Flight status notifications.
- REST API integration.
- Improved reporting system.

---

## 👥 Collaborators

This project was developed collaboratively, with contributions and coordination through GitHub.

### Project Team

| Name | GitHub Username | Role |
|---|---|---|
| Faizan Rabbani | [@Faizan-rabbani](https://github.com/Faizan-rabbani) | Project Owner |
| Muhammad Israr Akram | [@imikhan](https://github.com/imikhan) | Repository Collaborator |

### Team Collaboration

The project uses GitHub for collaborative development and project management.

Team collaboration includes:

- Sharing and maintaining project source code.
- Coordinating development activities.
- Managing project updates.
- Reviewing and maintaining code.
- Working together on project development and documentation.

*Individual technical responsibilities can be added according to each member's actual contribution.*

---

## 👨‍💻 Developer

### Faizan Rabbani

**Web Developer | Computer Science Student**

- GitHub: [Faizan-rabbani](https://github.com/Faizan-rabbani)
- LinkedIn: [Faizan Rabbani](https://linkedin.com/in/faizan-rabbani-585b46346/)

## 📄 License

This project is intended for educational and learning purposes.

Please contact the repository owner before redistributing or reusing the project.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a star ⭐.

Your support and feedback are appreciated!

**Thank you for visiting the Airlines Management System repository!** ✈️

