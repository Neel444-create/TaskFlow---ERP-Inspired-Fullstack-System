# TaskFlow – ERP-Inspired Full-Stack System

A lightweight, ERP-inspired full-stack application designed to simplify business operations by integrating task management, user management, workflow tracking, and centralized data handling.

TaskFlow demonstrates how core Enterprise Resource Planning (ERP) concepts can be implemented through a modern web application, providing practical exposure to enterprise software architecture and business process management.

## Overview

Organizations use ERP systems to integrate different business functions into a centralized platform. TaskFlow applies this concept to a simplified business environment by providing a common platform for managing tasks, tracking progress, and organizing operational workflows.

The project focuses on understanding how frontend applications, backend services, APIs, databases, and business logic work together in an enterprise-style application.

## Key Features

- **User Authentication:** Secure login and authentication workflow.
- **Task Management:** Create, view, update, and manage tasks.
- **Centralized Data Management:** Store and retrieve application data through a backend database.
- **REST API Integration:** Communication between frontend and backend through APIs.
- **Workflow Management:** Organize tasks and track their progress.
- **Modular Architecture:** Separate frontend, backend, and business logic for easier maintenance.

## ERP Concepts Demonstrated

| ERP Concept | TaskFlow Implementation |
|---|---|
| User Management | User authentication and access |
| Process Management | Task creation and assignment |
| Workflow Tracking | Task status and progress |
| Centralized Database | Persistent data storage |
| System Integration | Frontend and backend API communication |
| Business Logic | Backend validation and processing |

## Technology Stack

### Frontend
- React.js
- JavaScript
- HTML5
- CSS3

### Backend
- Python
- FastAPI
- REST APIs

### Database
- [Add your actual database here]

### Development Tools
- Git and GitHub
- VS Code
- Postman

## System Architecture

```text
           USER
             |
             v
      REACT FRONTEND
             |
             v
        REST APIs
             |
             v
       FASTAPI BACKEND
             |
             v
       BUSINESS LOGIC
             |
             v
          DATABASE
```

## Application Workflow

1. User accesses the TaskFlow application.
2. User authenticates through the login interface.
3. Frontend sends requests to the backend using REST APIs.
4. Backend validates requests and executes business logic.
5. Application retrieves or updates information in the database.
6. Updated information is returned to the frontend and displayed to the user.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Neel444-create/TaskFlow---ERP-Inspired-Fullstack-System.git
cd TaskFlow
```

### 2. Backend Setup

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend server:

```bash
uvicorn main:app --reload
```

Adjust the application entry point if your FastAPI application is located elsewhere.

### 3. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
npm install
npm run dev
```

## Learning Outcomes

- Understanding full-stack application development.
- Practical implementation of REST API architecture.
- Understanding ERP fundamentals and integrated business workflows.
- Database connectivity and data management.
- Backend development using FastAPI.
- Frontend and backend integration.
- Version control and project management using Git and GitHub.

## Future Enhancements

- Role-Based Access Control (RBAC).
- Employee and department management.
- Task assignment and approval workflows.
- Project and resource management.
- Reporting dashboards and analytics.
- Inventory and procurement modules.
- ERP integration concepts inspired by SAP, Oracle, and Microsoft Dynamics.

## Author

**Neel Prajapati**

Mechanical Engineering | IIT Hyderabad

GitHub: [Neel444-create](https://github.com/Neel444-create)

---

*TaskFlow is an academic and learning-oriented project designed to demonstrate fundamental ERP concepts through full-stack software development.*