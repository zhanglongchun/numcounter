## All the ways plan to test the numcounter:

### Functional testing:
1. Wrong arguments
	- No arguments
	- Too many arguments: -s filename filename filename
	- Wrong arguments: -t filename, -a filename
	- Order of arguments: -s filename, filename -s 
	- Too long filename(probably dealed by OS shell):
2.	Wrong file
	- Filename is not a valid path
	- File is not exist
	- File permission is wrong
3.	File contents
	- Empty file
	- Multi-blank lines (at first, middle, end of the file)
	- Different line ends: \r\n, \n
	- Long line: huge size single line
4.	Line formats
	- One space separator
	- Two or more successive separators
	- Head separator
	- Tail separator
	- Long token
5.	Number formats
	- Wrong number: character is not digital, point, e/E, +-
	- Wrong float format: 1.1, .1, 0.1, 1.10,e+10, E+10, e-10, E-10, e1.1, E1.1

### None functional testing:
1.	Performance testing (clear the OS cache buffer before each testing)
	- Big file (1M, 100M, 1T)
