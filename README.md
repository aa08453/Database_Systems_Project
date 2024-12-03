# Club Website Database Project

This project is a club website built using Django. It allows users to interact with a database via a web interface, with distinct modes for **Admins** and **Users**. Admins can manage the database through CRUD operations (Create, Read, Update, Delete), while users have limited interaction capabilities.

---

## Features
- Two modes: **Admin** and **User**.
- Admin functionalities:
  - Add, update, and delete records via forms.
  - Access to restricted pages for data management.
- User functionalities:
  - View records and interact with the user interface.
- Default views for listing, updating, and deleting records (`views.py`).
- Custom forms for CRUD operations (`forms.py`).
- URLs connected via `urls.py`.

---

## Project Directory Structure
```
club_website/
│
├── manage.py                 # Entry point for Django commands
├── club_website/             # Project configuration directory
│   ├── settings.py           # Project settings
│   ├── urls.py               # Global URL configuration
│   └── wsgi.py               # WSGI entry point for deployment
│
├── app_name/                 # Replace with your app name
│   ├── migrations/           # Database migration files
│   ├── templates/            # HTML templates for views
│   ├── static/               # Static files (CSS, JS, images)
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Form classes for CRUD operations
│   ├── models.py             # Database models
│   ├── tests.py              # Unit tests
│   ├── views.py              # View logic (CRUD)
│   └── urls.py               # App-specific URLs
```

---

## Setup Instructions

### 1. Prerequisites
- Python 3 installed on your system.
- SQL Server Management Studio (SSMS) or Azure Data Studio installed for database management.
- A web browser to access the generated IP.

### 2. Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/Abdullah-Mujtaba/Database_django_project.git
cd Mathclub_Website/
```

### 3. Configure the Database
1. Open SQL Server Management Studio (SSMS) or Azure Data Studio.
2. Run the provided SQL script to set up the database.

### 4. Install Dependencies
Install required Python packages using `pip`:
```bash
pip install django mssql-django django-mssql
```

### 5. Apply Migrations
Run the following command in the project directory to apply database migrations:
```bash
python3 manage.py migrate
```

### 6. Start the Server
Start the Django development server:
```bash
python3 manage.py runserver
```

### 7. Access the Website
- An IP (e.g., `http://127.0.0.1:8000/`) will be generated in the terminal.
- Open the IP in your browser to view and interact with the website.

---

## Admin and User Credentials

| **Role** | **Username** | **Password** |
|----------|--------------|--------------|
| Admin    | `admin`      | `123`        |
| User     | `user`       | `123`        |

---

## Functionality Details

### Admin Mode
- Accessible by logging in with admin credentials.
- Exclusive access to pages for managing database records.
- CRUD operations enabled:
  - **List View**: Displays all records.
  - **Update View**: Updates existing records.
  - **Delete View**: Deletes records.
  - **Add Records**: Handled via custom forms in `forms.py`.

### User Mode
- Accessible by logging in with user credentials.
- Limited access to viewing pages and interacting with data.

---

## Key Files

| **File**       | **Purpose**                                                                               |
|-----------------|-------------------------------------------------------------------------------------------|
| `views.py`      | Contains logic for default list, update, and delete views.                               |
| `forms.py`      | Defines forms for creating and updating records.                                         |
| `urls.py`       | Maps URLs to views for navigation across pages.                                          |
| `models.py`     | Defines database models and their relationships.                                         |

---

## Notes
- Ensure you have a working SQL Server setup before running the project.
- Run the script given in `mathclub/tests/` directory in SSMS or Azure Studios. 
- For additional customization, modify the `settings.py` file to configure your database settings and other project configurations.

---

## License
This project is created by Abdullah Amir, Hamad Asif Khan, Ahmed MUjtaba, Umar Habib.
