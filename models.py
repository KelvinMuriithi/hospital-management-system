from sqlalchemy import Integer, Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# patient-doctor association table
treatments_made  = Table(
    "treatments_made", Base.metadata,
    Column("patient_id", Integer, ForeignKey("patients.id")),
    Column("doctor_id", Integer, ForeignKey("doctors.id"))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    user_name = Column(String)
    
class Patient(User):
    __tablename__ = "patients"
    id = Column(Integer,ForeignKey("users.id"), primary_key=True)
    patient_history = Column(String)
    
    # one patient can be treated by many doctors
    doctors = relationship("Doctor", secondary = "treatments_made", back_populates="patients")
    
class Doctor(User):
    __tablename__ = "doctors"
    id = Column(Integer, ForeignKey("users.id"),  primary_key=True)
    specialized_in = Column(String)
    
    # one doctor can treat many patients
    patients = relationship("Patient", secondary = "treatments_made", back_populates="doctors")
    # One doctor belongs to one department
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department",  back_populates ="doctors")
    

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer,  primary_key=True)
    department_name = Column(String)
    # one department has many doctors
    doctors = relationship("Doctor",  back_populates ="department")

    