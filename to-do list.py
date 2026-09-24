import sqlite3
from datetime import date
task_date = date.today()
print(task_date)
print(type(task_date))
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

#create a tasks table which has 3 columns (id,task,date)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            date TEXT
             
        )
""")

connection.commit()


#user insert a task#

task = input("Add a task:")

cursor.execute(
    "INSERT INTO tasks (task, date) VALUES (?,?)",
    (task,task_date)
)
connection.commit()

#show the todo list
cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()
print("Your Tasks:")
for show_task in tasks:
   
    print(show_task[0],show_task[1],show_task[2])
connection.close()

