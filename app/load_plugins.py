import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    """A class to manage the application, including loading commands and executing user inputs."""

    def __init__(self):
        """Initialize the command handler."""
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all plugins and register them with the command handler."""
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        pass  # Ignore non-command classes

    def start(self):
        """Start the application and process user commands."""
        self.load_plugins()
        while True:
            user_input = input("Enter a command (or 'exit' to quit): ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                break

            parts = user_input.split(" ", 1)  # Allows subcommands like 'history view'
            command_name = parts[0]
            command_args = parts[1] if len(parts) > 1 else None

            result = self.command_handler.execute_command(command_name, command_args)
            if result is None:
                print(f"No such command: {user_input}")
            else:
                print(result)