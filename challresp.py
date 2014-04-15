# -*- coding: utf-8 -*-
# challresp.py
# Copyright (C) 2014 ManiacTwister
# 
# Based on :
# 	challenge-xchat.pl
# 	Copyright (C) 2006 Lee Hardy <lee -at- leeh.co.uk>
# 	Copyright (C) 2006 ircd-ratbox development team

import os
import xchat
from subprocess import Popen, PIPE

__module_name__ = "challresp"
__module_version__ = "0.1"
__module_description__ = "Challenge response plugin for secure oper authentication"

# Define numerics
RPL_RSACHALLENGE2 = 740
RPL_ENDOFRSACHALLENGE2 = 741

respond_path = "/usr/bin/ratbox-respond"
private_key_path = "<PATH TO YOUR PRIVATE KEY>"

challenge = ""
keyphrase = ""

def handle_challenge(word, word_eol, userdata):
	global challenge, keyphrase
	if len(word) < 2:
		print("Usage: /challenge <opername> [keyphrase]")
		return xchat.EAT_ALL;

	challenge = ""

	if len(word) > 2:
		keyphrase = word[2]

	xchat.command("QUOTE CHALLENGE {}".format(word[1]))
    	return xchat.EAT_ALL

def handle_rpl_rsachallenge2(word, word_eol, userdata):
	global challenge

	challenge = word[3][1:]
    	return xchat.EAT_ALL

def handle_rpl_endofrsachallenge2(word, word_eol, userdata):
	global challenge, keyphrase, respond_path, private_key_path

	print("ratbox-challenge: Received challenge, generating response.")

	if not os.access(respond_path, os.X_OK):
		print("ratbox-challenge: Unable to execute respond from " + respond_path + "\n")
		return xchat.EAT_ALL

	if not os.access(private_key_path, os.R_OK):
		print("ratbox-challenge: Unable to open " + private_key_path + "\n")
		return xchat.EAT_ALL

	p = Popen([respond_path, private_key_path], stdin=PIPE, stdout=PIPE, bufsize=1)
	p.stdin.write(keyphrase + "\n")
	p.stdin.write(challenge + "\n")
	output = p.stdout.readline().rstrip()

	if output.startswith("Error:"):
		print("ratbox-challenge: " + output + "\n")
		return xchat.EAT_ALL

	print("ratbox-challenge: Received response, opering..\n")

	keyphrase = None
	challenge = None

	xchat.command("QUOTE CHALLENGE +{}".format(output));

    	return xchat.EAT_ALL

xchat.hook_server("740", handle_rpl_rsachallenge2)
xchat.hook_server("741", handle_rpl_endofrsachallenge2)
xchat.hook_command("CHALLENGE", handle_challenge, priority=xchat.PRI_HIGHEST, help="Usage: /challenge <opername> [keyphrase]")

print "%s loaded." % __module_name__
