from Speak import speak
# Python code to create a file
def task():
    tasks=[]
    no_tasks = int(input("Enter the no. of tasks :- "))
    for i in range(no_tasks):
        tasks.append(input(f"Enter the task {i}:"))
        file = open("task.txt","a+")
        file.write(f"{i}. {tasks[i]}\n")
        speak(f"task {i} added Successfully.")
    file.close()
from plyer import notification
from pygame import mixer
def show():
    file = open("task.txt","r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load("notification.mp3")
    mixer.music.play()
    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

