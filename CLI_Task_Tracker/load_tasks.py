import json

class LoadDatabase():
    def entry_point(self):
        try:
            with open(r'/home/unix/Documents/kmitl (copy 1)/academics/python/Real_journey/Python_Practice/CLI_Task_Tracker/task_database.json') as file:
                read_data = file.read()
        except FileNotFoundError as err:
            raise Exception(err)
        if not read_data.strip():
            return {}
        return json.loads(read_data)
    def update(self,updated_dict):
        try:
            with open(r'/home/unix/Documents/kmitl (copy 1)/academics/python/Real_journey/Python_Practice/CLI_Task_Tracker/task_database.json','w') as file:
                file.write(json.dumps(updated_dict))
        except FileNotFoundError as err:
            raise Exception(err)
    