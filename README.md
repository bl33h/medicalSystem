# medicalSystem
MedicalSystem is a Python-based application that models a medical system and utilizes a PostgreSQL database for storing data related to doctors, healthcare facilities, medical supplies, diseases, and patients. The system is designed to provide a comprehensive and robust solution for managing medical information.

<p align="center">
  <br>
  <img src="https://i.imgur.com/y2V8fIb.png" alt="pic" width="400">
  <br>
</p>
<p align="center" >
  <a href="#entity-relationship-diagram">ERD</a> •
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Entity Relationship Diagram
<p align="center">
  <br>
  <img src="https://i.imgur.com/pSyecVi.png" alt="erd" width="1000">
  <br>
</p>


## Files

- src: the file that implements de solution.


## Features
The main features of the MedicalSystem application include:

- Database Setup: The system utilizes a PostgreSQL database to store all the necessary information. The database schema is designed to support the various entities involved in the medical system, such as doctors, patients, diseases, treatments, and healthcare facilities.
- User Authentication: The application includes a sign-in and login functionality to ensure secure access to the system. Users belonging to hospitals, healthcare centers, or clinics can authenticate themselves and access the system based on their roles and permissions.
- Patient Management: The system allows for the management of patient records, including personal information, medical history, diagnoses, treatments, and medications administered. The application provides a user-friendly interface for adding, updating, and retrieving patient data.
- Doctor Information: The system maintains a comprehensive database of doctors, including their contact information, and affiliations with healthcare facilities. This information is utilized for patient referrals, treatment assignments, and tracking doctor performance.
- Healthcare Facilities: The application supports the management of healthcare facilities such as hospitals, clinics, and healthcare centers. Information about the facilities, including their locations, services offered, and contact details, is stored in the database.
- Medical Supplies and Inventory: The system allows for the management of medical supplies and inventory. It provides features for tracking the availability of medications, equipment, and other medical resources. The application generates alerts when supplies are running low or approaching expiration to ensure timely restocking.

Reporting and Analytics: The system includes a reporting module that generates various reports for administrators. These reports provide insights into critical aspects of the medical system, such as the top diseases, doctors with the highest patient load, patients with the most frequent visits, and inventory status for different healthcare units.


## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

⚠️ **Note:** The AWS database mentioned in this project is no longer running. However, you can still set up a local database or use a different cloud-based database service to store the application data.

...
```bash
# Clone this repository
$ git clone https://github.com/bl33h/medicalSystem

# Install dependencies
$ pip install tkinter #

# Open the folder
$ cd src

# Run the app
$ python main.py

```
