from handle_input import InputHandling
from load_tasks import LoadDatabase
from engine import DatabaseFunction

database = LoadDatabase()
read_data = database.entry_point()

input = InputHandling(read_data)

cleaned_input = input.valid_command()

engine = DatabaseFunction(read_data,cleaned_input)

engine.match_command()

update_database = engine.updated_database()

database.update(update_database)

