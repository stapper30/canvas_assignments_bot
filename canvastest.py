import requests
from datetime import date
import dotenv
import os

dotenv.load_dotenv()
canvas_token = os.getenv("CANVAS_KEY")
chat_id = os.getenv("CHAT_ID")
TOKEN = os.getenv("TELEGRAM_TOKEN")
date_output_format_string = "%A, %B %d"

# define Course
class Course:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        
    def __str__(self):
        return f"{self.name}"

def assignments_message():
    message_body = """"""

    message_body += "Upcoming assignments:\n"
    message_body += "\n"
    print(canvas_token)
    for course in courses:
        response = requests.get(f"https://canvas.auckland.ac.nz/api/v1/courses/{course.id}/assignments", headers={"Authorization": canvas_token}, params={"order_by": "due_at", "bucket": "upcoming"})

        message_body += str(course)
        message_body += "\n"
        message_body += "\n"
        
        response_dictionary = response.json()                    
        for assignment in response_dictionary:
            print(assignment)
            if assignment['due_at']:
                print(assignment['due_at'])
                print(assignment)
                due_date = date.fromisoformat(assignment['due_at'].split("T")[0])
                message_body += f"{assignment['name']} - {due_date.strftime(date_output_format_string)}\n"
            
        message_body += "\n"
        message_body += "\n"
        
    send_message(message_body)
    
def send_message(text):    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    print(requests.post(url, params={"chat_id": f"{chat_id}", "text": f"{text}"}).json()) # this sends the message 
        
#list courses
courses = [
    Course(120882, "ENGSCI 211"),
    Course(122116, "SOFTENG 281"),
    Course(122117, "SOFTENG 282"),
    Course(121181, "COMPSYS 201")
]

assignments_message()    
