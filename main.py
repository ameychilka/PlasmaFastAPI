from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine
from pydantic import BaseModel
import hashlib
from sqlalchemy.orm import sessionmaker
import datetime

models.database.Base.metadata.create_all(bind=engine)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# With this we get a session to do whatever
# we want to do
session = Session()
app = FastAPI()


class DonorsFields(BaseModel):
    fullName : str
    age : int
    contactNo : str
    emailId : str
    eligibility : str
    availability : str
    bloodGroup : str


@app.get("/api/getplasmadonors")
def getplasmadonors():
    my_cursor = engine.execute("SELECT * FROM Donors")
    data = my_cursor.fetchall()
    return data


@app.post("/api/addplasmadonors")
def addplasmadonors(data: DonorsFields):
    donor = models.Donors(data.fullName, data.age, data.contactNo, data.emailId,
                         data.eligibility, data.availability,data.bloodGroup)
    session.add(donor)
    session.commit()
    return "Donor Successfully Registered !!"

@app.post("/api/plasma/getemail")
def getemail(email: str):
    verificationQuery = engine.execute("SELECT * FROM Donors where emailId='"+email+"'")
    data = verificationQuery.fetchone()
    return data




