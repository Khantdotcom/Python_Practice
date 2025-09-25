class InputHandling(Exception):
    def length_checking(self,input):
        if 4 < len(input) < 2:
            raise InputHandling(f"Your command should be at least 2 arguments and at most 3 arguments")
        return len(input)
    def input(self):
        user_input = input("").strip()
        if self.length_checking(user_input) == 3:
            arg1,arg2,arg3 = user_input
        else:
            arg1,arg2 = user_input
        arg1 = self.valid_command(arg1)
        arg2 = self.valid_second_arg(arg2)

        return arg1,arg2, arg3 if not None

    def valid_command(self,command):
        list_of_command = ['add','update','delete','list','mark-in-progress','mark-done']
        if command not in list_of_command:
            raise InputHandling(f"Your commands should be: \n1. add\n2. delete\n3.list\n4.update\n5.mark-in-progress\n6.mark-done")
        return command
    
    def valid_second_arg(self,arg2):
        groups = ['done','in-progess','to-do']
        if not arg2.is_integer() or arg2 not in groups:
            raise InputHandling(f"Your second argument should be either status or id")
        return arg2
    
