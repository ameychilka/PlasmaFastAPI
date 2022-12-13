from sqlalchemy import Column, ForeignKey, Integer, String

import database


class Donors(database.Base):
    __tablename__ = "donors"
    id = Column(Integer, autoincrement=True, primary_key=True)
    fullName = Column(String)
    age = Column(Integer)
    emailId = Column(String, unique=True)
    bloodGroup = Column(String)
    contactNo = Column(String)
    eligibility = Column(String)
    availability = Column(String)

    def __init__(self, name, age, mobile, email, eligibility, availability, bloodGroup):
        self.fullName = name
        self.age = age
        self.contactNo = mobile
        self.emailId = email
        self.eligibility = eligibility
        self.availability = availability
        self.bloodGroup = bloodGroup