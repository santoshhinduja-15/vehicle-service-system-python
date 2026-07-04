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
Username : admin <br>
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

## Screenshots
1. Main Menu
<img width="824" height="292" alt="image" src="https://github.com/user-attachments/assets/887e0f21-5928-4129-ac5f-8ca61e16f3c0" />

2. Customer Registration
<img width="816" height="595" alt="image" src="https://github.com/user-attachments/assets/2d109a5a-b9df-45e3-9d92-87749ef8c099" />

3. Validation Messages
<img width="809" height="698" alt="image" src="https://github.com/user-attachments/assets/e0c6461e-0788-48a7-a0d6-636248ad6a50" />

4. Admin Login
<img width="813" height="472" alt="image" src="https://github.com/user-attachments/assets/2e85f270-7bea-42fa-b0a3-409dcfde9807" />

5. Add Mechanic
<img width="814" height="492" alt="image" src="https://github.com/user-attachments/assets/cba48dc2-e88e-460e-8cab-232b9e01d042" />

6. Add Another Mechanic
<img width="816" height="469" alt="image" src="https://github.com/user-attachments/assets/c3bca910-3656-4bc0-bd28-d78574557c32" />

7. View Mechanics
<img width="813" height="669" alt="image" src="https://github.com/user-attachments/assets/3b544a98-5d21-41cf-96af-c291239db37e" />

8. Add Vehicle
<img width="811" height="547" alt="image" src="https://github.com/user-attachments/assets/636291a7-e674-4d2e-ae8f-ed7c6c6ed3f4" />

9. View Vehicles
<img width="813" height="577" alt="image" src="https://github.com/user-attachments/assets/6e874c83-fec8-489f-b50b-550fee92a424" />

10. Customer Login
<img width="820" height="471" alt="image" src="https://github.com/user-attachments/assets/fac15134-c34e-4f02-a9da-6c09c26ff81a" />

11. Create Service Request
<img width="850" height="517" alt="image" src="https://github.com/user-attachments/assets/105bd987-e6e2-4412-bd41-cc918b7d83e8" />

12. Assign Mechanic
<img width="808" height="351" alt="image" src="https://github.com/user-attachments/assets/edd19b3d-46ca-49ac-accf-b7fa7b631ada" />

13. Mechanic Login
<img width="813" height="469" alt="image" src="https://github.com/user-attachments/assets/272a480e-9948-4001-94a0-40dd03b8b7ba" />

14. Assigned Jobs
<img width="820" height="549" alt="image" src="https://github.com/user-attachments/assets/b020a1a3-ffa8-4294-89e2-3337fba6112b" />

15. Status Update
<img width="818" height="468" alt="image" src="https://github.com/user-attachments/assets/2240f3c8-8ede-4ad4-8599-b94b2ab07204" />
<img width="816" height="464" alt="image" src="https://github.com/user-attachments/assets/e4388009-20e4-4400-843c-8b7a9cbac26b" />

16. Generate Bill
<img width="737" height="874" alt="image" src="https://github.com/user-attachments/assets/82f2bee2-3740-412f-8430-fc9ffbe12998" />

17. Record Payment
<img width="717" height="325" alt="image" src="https://github.com/user-attachments/assets/05585a7c-9e20-4dfe-8bd4-61277e3b26ee" />

18. Revenue Report
<img width="715" height="312" alt="image" src="https://github.com/user-attachments/assets/554b0381-2430-4de0-93d6-40d3a0c3d390" />
