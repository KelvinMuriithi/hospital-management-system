from sqlalchemy.orm import Session
from db import engine, Base
from models import Patient, Department, Doctor

Base.metadata.create_all(bind=engine)

def hospital_sampe_data():
    session  =Session(bind=engine)
    
    # department
    psychiatry = Department(department_name = "Psychiatry")
    session.add(psychiatry)
    
    # doctors
    doc_one = Doctor(user_name = "John", specialized_in ="Brain surgery", department=psychiatry)
    doc_two = Doctor(user_name = "Jane", specialized_in ="Mental-health", department=psychiatry)
    # patients
    patient_one = Patient(user_name = "Alice",  patient_history ="Brain tumor")
    patient_two = Patient(user_name = "Leo",  patient_history ="Psychosis")
    patient_three = Patient(user_name = "Cassy",  patient_history ="Autism")
    
    # setup treatment
    doc_one.patients.append(patient_one)
    doc_one.patients.append(patient_two)
    doc_two.patients.append(patient_one)
    doc_one.patients.append(patient_three)
    
    session.add_all([doc_one, doc_two,patient_one, patient_two, patient_three])
    session.commit()
    session.close()
    print("Hospital data created successfully.")
    
if __name__ == "__main__":
    hospital_sampe_data()