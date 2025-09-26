try:
    with open('task_database.json') as file:
        read_data = file.read()
except FileNotFoundError as err:
    raise Exception(err)  