from ast import Delete
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    #1 is a student id#
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return{"name":"First Date"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]