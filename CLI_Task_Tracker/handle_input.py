class InputHandling():
    def __init__(self,database):
        self.database = database
    def valid_command(self,length):
        user_input = input("").split()
        list_of_command = {
                'add': {'error': "Invalid 'add' command. Expected 3 arguments.", 'length': 3},
                'delete': {'error': "Invalid 'delete' command. Expected 2 arguments.", 'length': 2},
                'list': {'error': "Invalid 'list' command. Expected 2 arguments.", 'length': 2},
                'mark-done': {'error': "Invalid 'mark-done' command. Expected 2 arguments.", 'length': 2},
                'mark-in-progress': {'error': "Invalid 'mark-in-progress' command. Expected 2 arguments.", 'length': 2},
                'update': {'error': "Invalid 'update' command. Expected 3 arguments.", 'length': 3}
        }
        groups = ['done','in-progess','to-do']
        '''Valid first command'''
        if not input[0] in list_of_command.keys():
            raise Exception(f"Your commands should be: \n1. add\n2. delete\n3.list\n4.update\n5.mark-in-progress\n6.mark-done")
        
        '''length checking'''
        if len(input) != list_of_command[input[0]]['length']:
            raise Exception(f"{list_of_command[input[0]]['error']}")
        if not input[2] in self.database.keys() or input[1] not in groups:
            raise Exception(f"Your second argument should be either status or id")
        return input
    
"""To return valid args that will perform database functions or else display errors"""

"""    def input(self):
        user_input = input("").strip()
        if self.length_checking(user_input) == 3:
            arg1,arg2,arg3 = user_input
        else:
            arg1,arg2 = user_input
        arg1 = self.valid_command(arg1)
        arg2 = self.valid_second_arg(arg2)"""