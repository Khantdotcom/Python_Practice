'''engine.py'''
from datetime import datetime

class DatabaseFunction():
    def __init__(self,database,input):
        self.database = database
        self.command = input[0]
        self.id = input[1] if len(input) > 1 else None
        if len(input) > 2:
           self.description = input[2]
        else:
           self.description = self.database.get(self.id, {}).get('description')
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def match_command(self):
        match self.command:
            case 'add':
                self.add()
            case 'update':
                self.update()
            case 'delete':
                self.delete()
            case 'list':
                self.list()
            case 'mark-in-progress':
                self.progress()
            case 'mark-done':
                self.done()
            case 'mark-to-do':
                self.todo()    
    def add(self):
        if self.id in self.database.keys():
            self.update()
        else:
            self.database[self.id] = {'status' :'to-do', 'description': self.description, 'create-at': self.now, "updated-at": self.now}
        self.print_task()
    def update(self):
        self.database[self.id]['description'] = self.description
        self.database[self.id]['updated-at'] = self.now
        self.print_task()

    def print_task(self):
        print(f"{self.command.capitalize()}ed:\nTask Name : {self.description}\nStatus: {self.database[self.id]['status']}\nTask Id :{self.id}\nCreate-at: {self.database[self.id]['create-at']}\nLast-Updated: {self.database[self.id]['updated-at']}")
    def delete(self):
        self.print_task()
        del self.database[self.id]
    def list(self):
        match self.id:
            case 'all':
                for _key,value in self.database.items():
                    print(f"{value['description']} : {value['status']}")
            case 'to-do':
                print("To-do Tasks")
                for key,value in self.database.items():
                    if value['status'] == 'to-do':
                        print(f"{value['description']}")

            case 'done':
                print("Done Tasks")
                for key,value in self.database.items():
                    if value['status'] == 'done':
                        print(f"{value['description']}")
            case 'in-progress':
                print("In progress Tasks")
                for key,value in self.database.items():
                    if value['status'] == 'in-progress':
                        print(f"{value['description']}")

            
    def progress(self):
        self.database[self.id]['status'] = 'in-progress'
        self.database[self.id]['updated-at'] = self.now
        self.print_task()
        
    def done(self):
        self.database[self.id]['status'] = 'done'
        self.database[self.id]['updated-at'] = self.now
        self.print_task()
    def todo(self):
        self.database[self.id]['status'] = 'done'
        self.database[self.id]['updated-at'] = self.now
        self.print_task()



    def updated_database(self):
        return self.database
