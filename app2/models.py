import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.utils import timezone

class Report(models.Model):
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100, null=True)
    lab_name = models.CharField(max_length=100, null=True)
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=20)
    sample_type = models.CharField(max_length=50)
    hemoglobin = models.FloatField()
    range = models.CharField(max_length=100)
    prescription = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    report_pdf = models.FileField(upload_to='reports/', max_length=250, null=True, default=None)
    report_as_pdf = models.FileField(upload_to='reports/', max_length=250, null=True, default=None)

    def __str__(self):
        return f"Report for {self.patient} - {self.appointment}"

class Invoice(models.Model):
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    room_cost = models.DecimalField(max_digits=10, decimal_places=2)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2)
    case_fee = models.DecimalField(max_digits=10, decimal_places=2 , null=True)
    medicine_cost = models.DecimalField(max_digits=10, decimal_places=2 , null=True)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2 , null=True)

    def __str__(self):
        return f"Invoice #{self.id} for {self.patient.username}"

from django.urls import reverse

class Notification(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    patientid = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    room_type = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    medical = models.OneToOneField('Medical', on_delete=models.CASCADE, related_name='notification', null=True, blank=True)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE , null=True,) 

    def get_notification_link(self):
        return reverse('notification_detail', kwargs={'notification_id': self.pk})
    
    def __str__(self):
        return f"Notification for {self.patient.username}"

class Room(models.Model):
    ROOM_TYPES = [
        ('AC', 'AC Room'),
        ('Non-AC', 'Non-AC Room'),
        ('General', 'General Room'),
    ]

    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.quantity} available"

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    medicine_id = models.CharField(max_length=50, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.medicine_id:
            self.medicine_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        # Example: Generate a unique ID using UUID
        return str(uuid.uuid4().hex)[:10]  # Adjust the length as needed

    def __str__(self):
        return f"{self.name} ({self.medicine_id})"

class Medical(models.Model):
    appointment_date = models.DateField(default=datetime.date.today)
    admit_date = models.DateField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    patient = models.CharField(max_length=100, default=2)
    doctor = models.ForeignKey('staff', on_delete=models.CASCADE)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    patientid = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    appointment_id = models.IntegerField(default=27)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    prescription = models.TextField(default='No prescription')
    medicine_time = models.TextField(default='N/A')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=50, choices=[('medicine', 'Medicine'), ('service', 'Service')], default='medicine')
    service_name = models.CharField(max_length=100, null=True, blank=True)  # Add service name field for service entries
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    doctor = models.ForeignKey('staff', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=100) 
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    is_full = models.BooleanField(default=False) 
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    patient_username = models.CharField(max_length=100 , default="NA")
    is_history = models.BooleanField(default=False)
    medical_type = models.CharField(max_length=20, choices=[('Emergency', 'Emergency'), ('Normal', 'Normal')], default='Normal')
    case_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return f"Appointment {self.id} - {self.name} with Dr. {self.doctor} on {self.date} at {self.time}"

class staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    department = models.CharField(max_length=20)
    staff_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='on')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    medical_license = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    medical_school = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    languages = models.CharField(max_length=255)
    publications = models.TextField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    capacity_per_hour = models.IntegerField(default=4) 
    submission_date = models.DateField()
    submitted_registration = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Laboratory(models.Model):
    labstaff = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    owner_manager_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    services_provided = models.ManyToManyField(Service)
    operating_hours = models.CharField(max_length=50)
    insurance_accepted = models.TextField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=20)
    sugar = models.CharField(max_length=20)
    concerns = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name 
    
    
class Slot(models.Model):
    staff = models.ForeignKey('staff', on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # 'monday', 'tuesday', etc.
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.staff} - {self.day} - {self.start_time} to {self.end_time}"
    

