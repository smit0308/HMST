
# 🏥 Hospital Management System

Welcome to the Hospital Management System project! This Django-based web application is designed to efficiently manage various hospital operations, including patient management, staff administration, appointment scheduling, room allocation, and more.

## 🌟 Features

- **Patient Management**: Handle patient registration, admission, discharge, and medical records.
- **Staff Management**: Manage staff details, including roles like doctors, nurses, and administrative staff.
- **Appointment Scheduling**: Allow patients to book, view, and manage appointments with doctors.
- **Room Management**: Allocate rooms to patients based on availability and update statuses in real-time.
- **Medical Records**: Maintain comprehensive medical histories and generate bills for services rendered.
- **Billing System**: Generate, view, and manage bills for patients, including medicine assignments and other services.
- **Email Notifications**: Send automated notifications to patients and staff regarding appointments, admissions, and more.
- **User Roles & Permissions**: Secure the application with role-based access control for Admin, Staff, and Patients.
- **Laboratory Management**: Assign and manage laboratory tests, including linking with specific laboratories.
- **File Management**: Upload and manage files related to patients, staff, and hospital operations.

## ⚙️ Technology Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Other Tools**: Jinja2, SMTP for email notifications, 'xhtml2pdf' for PDF generation

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- PGAdmin
- Virtual Environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/smit0308/hospital-management-system.git
   cd hospital-management-system
   ```

2. **Set up the virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   - Create a PostgreSQL database and update the `DATABASES` settings in `settings.py` with your credentials.

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/`.

## 📂 Project Structure

```
hospitalmanagement/
├── app2/                  # Additional services (appointments, billing, lab management)
├── static/                # Static files (CSS, JavaScript, Images)
├── media/                 # media files (Lab Report)
├── templates/             # HTML templates
├── hospitalmanagement/    # Project settings
├── manage.py              # Django management script
└── README.md              # Project README file
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Author

- **Smit Patel** - [GitHub Profile](https://github.com/smit0308)

## 🎯 Acknowledgements

- Django Documentation
- PostgreSQL Documentation
- Community contributors
