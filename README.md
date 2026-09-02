\# CampusHubERP



CampusHubERP is a Python-based College Management System developed as part of the OJT assignment.



The project demonstrates Object-Oriented Programming, database management, REST APIs, asynchronous programming, file handling, testing, logging, debugging, and software design patterns.



\---



\## Project Features



\- Student Management

\- Faculty Management

\- Course Management

\- Enrollment Management

\- CRUD operations

\- Input validation

\- Service layer architecture

\- SQLAlchemy database integration

\- Repository Pattern

\- Singleton Pattern

\- Factory Method Pattern

\- Logging

\- Error handling and debugging

\- JSON file handling

\- CSV file handling

\- Pickle file handling

\- Regular expressions

\- Generators and iterators

\- Functional programming

\- Threading

\- Multiprocessing

\- Async programming

\- REST APIs using FastAPI

\- Automated testing using Pytest

\- Report generation



\---



\## Technologies Used



\- Python 3.10

\- FastAPI

\- Uvicorn

\- SQLAlchemy

\- SQLite

\- Pytest

\- Requests

\- aiohttp



\---



\## Project Structure



```text

CampusHubERP/

│

├── app/

│   ├── api/

│   │   ├── course\_api.py

│   │   ├── enrollment\_api.py

│   │   ├── faculty\_api.py

│   │   ├── main.py

│   │   └── student\_api.py

│   │

│   ├── core/

│   │   ├── abc\_interfaces.py

│   │   ├── descriptors.py

│   │   ├── factory.py

│   │   └── metaclasses.py

│   │

│   ├── database/

│   │   ├── db.py

│   │   ├── models.py

│   │   └── repository.py

│   │

│   ├── models/

│   │   ├── course.py

│   │   ├── faculty.py

│   │   └── student.py

│   │

│   ├── services/

│   │   ├── async\_service.py

│   │   ├── course\_service.py

│   │   ├── enrollment\_service.py

│   │   ├── faculty\_service.py

│   │   └── student\_service.py

│   │

│   └── utils/

│       ├── api\_tasks.py

│       ├── async\_tasks.py

│       ├── csv\_manager.py

│       ├── decorators.py

│       ├── file\_manager.py

│       ├── generators.py

│       ├── iterators.py

│       ├── logger.py

│       ├── module\_loader.py

│       ├── multiprocessing\_tasks.py

│       ├── pickle\_manager.py

│       ├── serializers.py

│       └── threading\_tasks.py

│

├── data/

│   ├── courses.json

│   ├── enrollments.json

│   ├── faculty.json

│   ├── student.json

│   ├── students.csv

│   └── students.pkl

│

├── logs/

│   └── application.log

│

├── reports/

│   ├── courses.txt

│   ├── faculty.txt

│   └── student.txt

│

├── tests/

│   ├── test\_course.py

│   ├── test\_enrollment.py

│   ├── test\_faculty.py

│   └── test\_student.py

│

├── campushub.db

├── requirements.txt

├── .gitignore

└── README.md

