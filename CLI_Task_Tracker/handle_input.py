class InputHandling():
    def __init__(self,database):
        self.database = database
        self.user_input = input("").split()
    def valid_command(self):
        list_of_command = {
                'add': {'error': "Invalid 'add' command. Expected 3 arguments.", 'length': 3},
                'delete': {'error': "Invalid 'delete' command. Expected 2 arguments.", 'length': 2},
                'list': {'error': "Invalid 'list' command. Expected 2 arguments.", 'length': 2},
                'mark-done': {'error': "Invalid 'mark-done' command. Expected 2 arguments.", 'length': 2},
                'mark-in-progress': {'error': "Invalid 'mark-in-progress' command. Expected 2 arguments.", 'length': 2},
                'update': {'error': "Invalid 'update' command. Expected 3 arguments.", 'length': 3},
                'to-do' : {'error': "Invalid 'to-do' command. Expected 2 arguments.", 'length': 2},
                'x' : {'error': "Invalid 'exit' command. Expected 1 arguments", 'length' : 1}
        }
        groups = ['done','in-progess','to-do','all']
        '''Valid first command'''
        if not self.user_input[0] in list_of_command.keys():
            raise Exception(f"Your commands should be: \n1. add\n2. delete\n3.list\n4.update\n5.mark-in-progress\n6.mark-done")
        
        '''length checking'''
        if len(self.user_input) != list_of_command[self.user_input[0]]['length']:
            print("length fine")
            raise Exception(f"{list_of_command[self.user_input[0]]['error']}")
        return self.user_input
    def go_on(self):
        return self.user_input == 'x'