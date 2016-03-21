#!/usr/bin/python

import os, sys, string

#######################################
# global variables
#######################################
skiperr_flag = False
verbose_flag = False
line_no = 0
err_count = 0

count = 0
sum = 0.0

filename = ""


#######################################
# functions
#######################################
def count4line(line):
	""" Count and sum the floats in single line
	
	Args:
		line: the line
	Returns:
		True/False, will never return False when skiperr_flag is True
	"""
	
	global sum, count, err_count

	line = line.strip()

	if len(line) == 0:		# empty line
		return True

	token = ""
	for token in line.split():
		try:
			num = string.atof(token)
		except ValueError:
			err_count = err_count + 1
			
			errmsg = "Token " + token + " is not a valid float.";
			if verbose_flag:
				print >> sys.stderr, 'There is a error in line', line_no, ':', errmsg
			if not skiperr_flag:
				return False;
			else:
				continue
		
		sum = sum + num
		count = count + 1
		
	return True

def usage(prog_name):
	print prog_name, ' [-s] [-verbose] filename'
	print "-s skip errors"
	print "-verbose show more information of errors"


########################################
# main program
########################################
if (len(sys.argv) <= 1):
	print >> sys.stderr, 'File name is missed.'
	usage(sys.argv[0])
	exit(1)

filename = ""
for i in range(1, len(sys.argv)):
	if (sys.argv[i].startswith('-')):
		if (sys.argv[i] == '-s'):
			skiperr_flag = True
		elif (sys.argv[i] == '-verbose'):
			verbose_flag = True
		else:
			print 'Unknown option:', sys.argv[i]
			usage(sys.argv[0])
			exit(1)
	else:
		if (filename != ""):
			print 'Too many filename in program arguments'
			exit(1)
		filename = sys.argv[i]
if (filename == ""):
	print >> sys.stderr, 'File name is missed.'
	usage(sys.argv[0])
	exit(1)

try:
	fd = open(filename)
except IOError:
	print "Can't open the file, please check the input file or permission."
	exit(1)

line = fd.readline()
while line:
	line_no = line_no + 1
	
	if (count4line(line) == False):
		if (not skiperr_flag):
			fd.close()
			exit(1)
		
	line = fd.readline()

fd.close()

print count, sum, err_count
