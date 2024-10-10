# License Management and Validation System

This is a Django-based License Management and Validation System designed for Software as a Service (SAAS) products. The system ensures secure and centralized license validation for all clients, enhancing control and security of software licenses.

## Features

- **License Validation:** Validates the authenticity and status of licenses across all SAAS products.
- **License Creation and Revocation:** Admins can create and revoke licenses.
- **License Integrity:** Implements strong encryption to protect license data.
- **Offline Mode:** Supports offline mode for limited license functionality when clients cannot connect to the server.
- **Admin Dashboard:** Provides an intuitive web-based interface for managing licenses, viewing usage statistics, and generating reports.

## System Architecture

The project follows a modular and secure architecture inspired by Microsoft's Software Architectural principles, consisting of:

### 1. Client-Side Component:
   - **License Validator**: Embedded in every SAAS product delivered to clients. This component is responsible for communicating with the central server and validating licenses.

### 2. Central Server Component:
   - **License Management Server**: Handles incoming license validation requests from clients and manages the central database of valid licenses.

### 3. Administrative Interface:
   - **Web-based Dashboard**: A secure, role-based access dashboard for administrators to manage licenses and generate reports.

## Technologies Used

- **Django**: Backend framework used for building the project.
- **Django Rest Framework (DRF)**: For building API endpoints.
- **PostgreSQL/MySQL**: For the database (you can choose depending on your preferences).
- **HTML/CSS**: For the admin interface and templates.
- **JavaScript**: For dynamic elements in the web interface.

## Setup and Installation

### Prerequisites:

- Python 3.8 or higher
- Django 4.0+
- PostgreSQL/MySQL database (with proper setup)
- Git

### Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/himanshu-sharmav/license-management-system.git
   cd license-management-system
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Configure the database in the `settings.py` file:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',  # Default PostgreSQL port, change to '3306' for MySQL
       }
   }
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   Open your browser and go to `http://127.0.0.1:8000/admin/` to access the admin panel.

## Usage

1. **Register a user:**
   Visit `/register/` to create a new account.

2. **Login:**
   After registration, visit `/login/` to log in as a registered user.

3. **License Management:**
   - Visit `/licenses/` to view all licenses.
   - Click "Revoke" to revoke an active license.
   - Visit `/licenses/create/` to create a new license.

### License Creation and Revocation:

- **Create License:**
  After logging in as an admin, navigate to `/create_license/` to create a new license.

- **Revoke License:**
  You can revoke a license by clicking the "Revoke" button next to a license in the license list.

## API Endpoints

The system also exposes a set of API endpoints for managing licenses:

1. **Get All Licenses (GET):**
   ```
   GET /api/licenses/
   ```

2. **Get License by ID (GET):**
   ```
   GET /api/licenses/<license_id>/
   ```

3. **Create New License (POST):**
   ```
   POST /api/licenses/
   {
       "license_key": "ABC1234XYZ",
       "is_active": true
   }
   ```

4. **Revoke License (PUT):**
   ```
   PUT /api/licenses/<license_id>/revoke/
   ```

## Security

1. **CSRF Protection:** All forms and POST requests are protected by Django’s CSRF mechanism.
2. **Role-Based Access Control:** Admin access is restricted by Django’s built-in `login_required` and custom permissions for actions like license revocation.
3. **Encryption:** All data transmission between the client and the server is encrypted using HTTPS.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
