#!/usr/bin/python

import sys, re
from geoip import geolite2

version="0.1"
input=""

def usage():
	print "-------------------------------------------------------"
	print "IP Geoloc v%s - Hugo RIFFLET - @l3m0ntr33" % (version)
	print "-------------------------------------------------------"
	print "Description: take standard input, search for the 1st IP found and use geolite2 to output the found IP and geolocation data."
	print ""

def getparam():
	global input
	for param in sys.argv:
		input = input + param


######### START ##############
if (len(sys.argv) == 2) and ((sys.argv[1]=="-help") or (sys.argv[1]=="-h")) :
	usage()
	sys.exit(1)

while(1):
	try:
		input = raw_input()
	except:
		break
	
	match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',input)
	
	if match is not None:
		ip = match.group(1)
		print "IP: %s - " % ip,

		try:
			geoloc = geolite2.lookup(ip)
			if geoloc is not None:
				if geoloc.country is not None:
					print "Country: %s - " % geoloc.country,
				else:
					print "Country: x - ",
				if geoloc.continent is not None:
					print "Continent: %s - " % geoloc.continent,
				else:
					print "Continent: x - ",
				if geoloc.timezone is not None:
					print "Timezone: %s " % geoloc.timezone,
				else:
					print "Timezone: x ",
				print ""
			else:
				print "Country: x - Continent: x - Timezone: x"
		except:
			print "ERROR"
	else:
		print "No IP found."
