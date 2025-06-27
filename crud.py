import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"
def create_student(name, details):
	data={'title':name,
	'body':details,
	'userId':1}
	response=requests.post(API_URL,json=data)
	print(response.status_code)
	
	
	
def read_student(student_id):
	response=requests.get(f"{API_URL}/{student_id}")
	print(response.status_code)
	print(response.json())
	
	
def update_student(student_id,name, details):
	data={'title':name,
	'body':details,
	'userId':1}
	response=requests.put(f"{API_URL}/{student_id}",json=data)
	print(response.status_code)
	print(response.json())

	
def delete_student(student_id):
	response=requests.delete(f"{API_URL}/{student_id}")
	print(response.status_code)
	print(response.json())
	
	
while True :
	print("Welcome to student records")
	print("choose the opiton code from below and enter it")
	print("1: create new student entry")
	print("2: read student entry")
	print("3: update student entry")
	print("4: delete student entry")
	print("5:EXIT")

	choice = input("enter the code :")

	match choice:
		case "1":
			name = input("enter the name")
			details =input("details")
			create_student(name,details)
			
		case '2':
			sid= input("enter student id:")
			read_student(sid)
		case '3':
			sid= input("enter student id:")
			name = input("enter the updated name")
			details =input("updated details")
			update_student(sid,name,details)
		case '4':
			sid=input("enter student id:")
			delete_student(sid)
		case"5" : 
			print("exiting")
			break
			
		

		
	
	
