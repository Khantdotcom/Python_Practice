class InputHandling():
    def __init__(self,database):
        self.database = database
    def valid_command(self):
        user_input = input("").split()
        list_of_command = {
                'add': {'error': "Invalid 'add' command. Expected 3 arguments.", 'length': 3},
                'delete': {'error': "Invalid 'delete' command. Expected 2 arguments.", 'length': 2},
                'list': {'error': "Invalid 'list' command. Expected 2 arguments.", 'length': 2},
                'mark-done': {'error': "Invalid 'mark-done' command. Expected 2 arguments.", 'length': 2},
                'mark-in-progress': {'error': "Invalid 'mark-in-progress' command. Expected 2 arguments.", 'length': 2},
                'update': {'error': "Invalid 'update' command. Expected 3 arguments.", 'length': 3}
        }
        groups = ['done','in-progess','to-do','all']
        '''Valid first command'''
        if not user_input[0] in list_of_command.keys():
            raise Exception(f"Your commands should be: \n1. add\n2. delete\n3.list\n4.update\n5.mark-in-progress\n6.mark-done")
        
        '''length checking'''
        if len(user_input) != list_of_command[user_input[0]]['length']:
            print("length fine")
            raise Exception(f"{list_of_command[user_input[0]]['error']}")
        return user_input