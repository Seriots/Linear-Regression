from ArgsHandler import ArgsHandler, OptionObject, ArgsObject

args_handler = ArgsHandler('This program generate some random things for you', [
	ArgsObject('arg1', 'First argument.'),
	ArgsObject('arg2', 'Second argument.'),
	ArgsObject('arg3', 'Third argument.'),
], [
	OptionObject('help', 'Show this help message.', 'h'),
	OptionObject('version', 'Show the version of the program.', 'v'),
	OptionObject('file', 'File to be processed.', 'f'),
	OptionObject('debug', 'Run the program in debug mode.', 'd'),
	OptionObject('yolooaud', 'Run the program in debug mode.'),
], """The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
Also the TIME_STYLE environment variable sets the default style to use.

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.""")

print(args_handler)