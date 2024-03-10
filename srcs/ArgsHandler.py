import sys
from dataclasses import dataclass, field

@dataclass
class OptionObject:
	fullname: str
	description: str = field(default='')
	name: str = field(default=None)

@dataclass
class ArgsObject:
	name: str
	description: str = field(default='')

class ArgsHandler:
	def __init__(self, description: str, all_args: list, all_option: list, extended_help: str = ''):
		self.description = description
		self.extended_help = extended_help
		self.all_option = all_option
		self.all_args = all_args

	def parse_args(self) -> dict:
		"""Parse the arguments and return a dictionary with the parsed values."""

	def help(self) -> str:
		"""Return the help message."""
		usage = f"Usage: python3 {sys.argv[0]} " + " ".join([f"{arg.name}" for arg in self.all_args]) + " [options]"
		options = f"Options:\n" + "\n".join([f"  {'-' + opt.name + ',' if opt.name != None else '   '} --{opt.fullname}  {opt.description}" for opt in self.all_option])
		return(f"""\
{usage}
{self.description}

{options}

{self.extended_help}""")

	def __repr__(self) -> str:
		"""Description of the ArgsHandler."""
		return self.help()

	def __str__(self) -> str:
		"""Description of the ArgsHandler."""
		return self.help()