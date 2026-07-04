# Vehicle Service System
A console-based Vehicle Service System developed using Core Python, Object-Oriented Programming (OOP), and TXT file storage. The system helps manage customers, vehicles, service requests, mechanic assignments, billing, payments, and reports in a vehicle service center environment.

## Features
### Authentication & Security
- Admin Login
- Customer Registration & Login
- Mechanic Login
- SHA-256 Password Hashing
- Role-Based Access Control

### Customer Management
- Add Customer
- Update Customer
- Delete Customer
- View Customers
- Duplicate Email Validation
- Duplicate Mobile Validation

### Vehicle Management
- Add Vehicle
- Update Vehicle
- Delete Vehicle
- View Vehicles
- Customer-wise Vehicle Tracking
- Vehicle Number Validation
- Duplicate Vehicle Number Prevention

### Mechanic Management
- Add Mechanic
- Update Mechanic
- Delete Mechanic
- View Mechanics
- Mechanic Specialization Management

### Service Request Management
- Create Service Request
- View Customer Requests
- Vehicle-wise Request Tracking
- Service Type Validation
- Customer-Vehicle Ownership Validation

### Mechanic Assignment
- Assign Mechanic to Service Request
- Prevent Duplicate Assignment
- Mechanic-wise Assigned Jobs

### Service Status Tracking
- Pending
- Assigned
- In Progress
- Completed

### Billing Management
- Generate Service Bill
- Service Charges
- Spare Part Charges
- Automatic Total Calculation

### Payment Management
- Record Payment
- Payment Validation
- Prevent Duplicate Payments

### Reports
- Pending Service Report
- Completed Service Report
- Revenue Report
- Mechanic Work Report

### Validations
- Required Field Validation
- Mobile Number Validation
- Email Validation
- Password Validation
- Manufacturing Year Validation
- Vehicle Number Validation
- Multiple Error Messages Displayed Together

## Technology Stack
- Core Python
- Object-Oriented Programming (OOP)
- TXT File Handling
- SHA-256 Password Hashing

## Default Admin Credentials
Username : admin
Password : admin123

admin.txt: admin|240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9

## Workflow
### Customer
Register -> Login -> Add Vehicle -> Create Service Request -> Track Service Status

### Admin
Login -> Manage Customers -> Manage Vehicles -> Manage Mechanics -> Assign Mechanics -> Generate Bills -> View Reports

### Mechanic
Login -> View Assigned Jobs -> Update Status -> Complete Service

## Sample Data
### Customer
Customer ID : C101 <br>
Name : Rahul Sharma <br>
Mobile : 9876543210 <br>
Email : rahul.sharma@gmail.com <br>
Address : Mumbai

### Vehicle
Vehicle ID : V101 <br>
Customer ID : C101 <br>
Vehicle Number : MH01AB1234 <br>
Vehicle Type : Car <br>
Company : Hyundai <br>
Model : Creta <br>
Manufacturing Year : 2022 

### Mechanic
Mechanic ID : M101 <br> 
Name : Rajesh Kumar <br>
Specialization : Engine Repair

## Future Enhancements
- MySQL Database Integration
- GUI Version using Tkinter
- Email Notifications
- SMS Notifications
- PDF Invoice Generation
- Search & Filter Features

## Author
Santosh Hinduja
