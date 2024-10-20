# import fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# FastAPI "instance"
app = FastAPI()
'''
GET - GET an info
POST - Create something new
PUT - UPDATE
DELETE - DELETE Something 
'''

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "grade 12",
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
    return {'name': 'First Data'}
# endpoint

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,/ description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

# gt greater than,lt,ge greater than equal to,le

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data":"not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int,student : Student):
    if student_id in students:
        return{"error": "Student exists"}
    students[student_id]=student
    return students[student_id]

@app.put("/update-student/{student-id}")
def update_student(student_id: int,student: UpdateStudent):
    if student_id not in students:
        return {'Error': 'Student does not exist'}
    
    if student.name != None:
        students[student_id].name =student.name
    if student.age != None:
        students[student_id].age =student.age
    if student.year != None:
        students[student_id].year =student.year
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}

    del students[student_id]
    return {"Message":"Student deleted"}