class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, operation, command):
        self.commands[operation] = command

    def execute_command(self, operation, *args):
        command = self.commands.get(operation)
        if command:
            return command.execute(*args)
        return f"Unknown command: {operation}"