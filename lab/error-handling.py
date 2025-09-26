number = 0

assert(number < 1 ), "Fuck you"

print(number)

try:
    command, id, description = input("").strip().split(' ')
except ValueError:
    command = 2


print(command)


i,j = " jjlljlj lkjlkj    ".split() 
i

list_of_command = {
            3: ['add', 'update'],
            2: ['delete', 'list', 'mark-in-progress', 'mark-done']
        }
'add' in zip(list_of_command.values())
zip(list_of_command.values())

list_of_command = {
            3: [{
                'add': "add [id] [name if exist else Untitled]"
                }, {'update' : "update [id] [name if you want to change]"}],
            2: [{'delete': "id you want to delete"}, {'list': "type status group"}, {'mark-in-progress', "[id]"}, {'mark-done':'[id]'}]
        }
if not any('add' in sublist for sublist in list_of_command.values()):
    raise Exception(f"Your commands should be: \n1. add\n2. delete\n3.list\n4.update\n5.mark-in-progress\n6.mark-done")

list_of_command.values()

gg = {
 'add': {'error': "Invalid 'add' command. Expected 3 arguments.", 'length': 3},
 'delete': {'error': "Invalid 'delete' command. Expected 2 arguments.", 'length': 2},
 'list': {'error': "Invalid 'list' command. Expected 2 arguments.", 'length': 2},
 'mark-done': {'error': "Invalid 'mark-done' command. Expected 2 arguments.", 'length': 2},
 'mark-in-progress': {'error': "Invalid 'mark-in-progress' command. Expected 2 arguments.", 'length': 2},
 'update': {'error': "Invalid 'update' command. Expected 3 arguments.", 'length': 3}
}

'add' in gg.keys()

user = input('').split()
user