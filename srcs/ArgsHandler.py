import sys
from dataclasses import dataclass, field

@dataclass
class OptionObject:
	fullname: str
	description: str = field(default='')
	name: str = field(default=None)
	expected_type: str = field(default=bool)

@dataclass
class ArgsObject:
	name: str
	description: str = field(default='')

class ArgsHandler:
	"""Argv class parser.
	Init with a description, a list of ArgsObject and a list of OptionObject.
	You can also add an extended help message.

	ArgsObject are the arguments that the program will take.
	
	OptionObject are the options that the program will take.
	"""
	def __init__(self, description: str, all_args: list, all_option: list, extended_help: str = ''):
		self.description = description
		self.extended_help = extended_help
		self.all_option = all_option
		self.all_args = all_args

	def parse_args(self) -> dict:
		"""Read on sys.argv and return a dict with the arguments and options parsed with the expected type. If an error is found, raise a ValueError."""
		args = {}
		last_option = None
		args_index = 0
		for value in sys.argv[1:]:
			if value.startswith('--'):
				value = value[2:]
				if value in [opt.fullname for opt in self.all_option]:
					last_option = self.all_option[[opt.fullname for opt in self.all_option].index(value)]
					if last_option.expected_type is bool:
						args[last_option.fullname] = True
				else:
					raise ValueError(f"Unknown option: {value}")
			elif value.startswith('-'):
				value = value[1:]
				if value in [opt.name for opt in self.all_option]:
					last_option = self.all_option[[opt.name for opt in self.all_option].index(value)]
					if last_option.expected_type is bool:
						args[last_option.fullname] = True
				else:
					raise ValueError(f"Unknown option: {value}")
			else:
				if last_option == None:
					if args_index < len(self.all_args):
						args[self.all_args[args_index].name] = value
						args_index += 1
					else:
						raise ValueError(f"Too many arguments.")
				else:
					if last_option.expected_type == int:
						args[last_option.fullname] = int(value)
					elif last_option.expected_type == float:
						args[last_option.fullname] = float(value)
					elif last_option.expected_type == str:
						args[last_option.fullname] = value
					elif last_option.expected_type == list:
						if last_option.fullname not in args:
							args[last_option.fullname] = []
						args[last_option.fullname].append(value)
					else:
						raise ValueError(f"Unknown type: {last_option.expected_type}")
		if args_index < len(self.all_args):
			raise ValueError(f"Too few arguments.")				

		return args

	def full_help(self) -> str:
		"""Return the full_help message."""
		usage = f"Usage: python3 {sys.argv[0]} " + " ".join([f"{arg.name}" for arg in self.all_args]) + " [OPTIONS]"
		options = f"Options:\n" + "\n".join([f"  {f'-{opt.name}, ' if opt.name != None else '   '} --{opt.fullname}  {opt.description}" for opt in self.all_option])
		args = f"Arguments:\n" + "\n".join([f"  {arg.name}  {arg.description}" for arg in self.all_args])
		return(f"""\
{usage}

{self.description}

{args}

{options}

{self.extended_help}""")
	
	def light_help(self) -> str:
		"""Return the light_help message."""
		usage = f"Usage: python3 {sys.argv[0]} " + " ".join([f"{arg.name}" for arg in self.all_args]) + " [OPTIONS]"
		options = f"Options:\n  " + ", ".join(filter(lambda x: x != '' ,[f"{f'-{opt.name}' if opt.name != None else ''}" for opt in self.all_option]))
		return(f"""\
{usage}

{options}""")

	def __repr__(self) -> str:
		"""Description of the ArgsHandler."""
		return self.light_help()

	def __str__(self) -> str:
		"""Description of the ArgsHandler."""
		return self.full_help()