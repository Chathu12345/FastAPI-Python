from ast import Delete
from unicodedata import name
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    #1 is a student id#
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return{"name":"First Date"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return{"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student: Student):
    if student_id in students:
        return{"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    students[student_id] = student
    return students[student_id]