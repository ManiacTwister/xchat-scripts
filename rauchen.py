# -*- coding: utf-8 -*-
# challresp.py
# Copyright (C) 2014 ManiacTwister
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import os
import xchat
import time
from random import choice

__module_name__ = "rauchen"
__module_version__ = "0.1"
__module_description__ = "Rauchen ist doof"

SPREUCHE=[
'Rauchen tötet.',
'Rauchen kann tödlich sein.',
'Rauchen fügt Ihnen und den Menschen in Ihrer Umgebung erheblichen Schaden zu.',
'Raucher sterben früher.',
'Rauchen kann tödlich sein.',
'Rauchen führt zur Verstopfung der Arterien und verursacht Herzinfarkte und Schlaganfälle.',
'Rauchen verursacht tödlichen Lungenkrebs.',
'Rauchen in der Schwangerschaft schadet Ihrem Kind.',
'Schützen Sie Kinder – lassen Sie sie nicht Ihren Tabakrauch einatmen!',
'Ihr Arzt oder Apotheker kann Ihnen dabei helfen, das Rauchen aufzugeben.',
'Rauchen macht sehr schnell abhängig: Fangen Sie gar nicht erst an!',
'Wer das Rauchen aufgibt, verringert das Risiko tödlicher Herz- und Lungenerkrankungen.',
'Rauchen kann zu einem langsamen und schmerzhaften Tod führen.',
'Hier finden Sie Hilfe, wenn Sie das Rauchen aufgeben möchten: Bundeszentrale für gesundheitliche Aufklärung (BZgA) Tel.: 01805-313131, www.rauchfrei-info.de.',
'Rauchen kann zu Durchblutungsstörungen führen und verursacht Impotenz.',
'Rauchen lässt Ihre Haut altern.',
'Rauchen kann die Spermatozoen schädigen und schränkt die Fruchtbarkeit ein.',
'Rauch enthält Benzol, Nitrosamine, Formaldehyd und Blausäure.'
] 

def on_message(word, word_eol, userdata):
  global timer
  words = word[1].split(" ")
  if xchat.get_info('channel').startswith('#chaostal') and 'rauchen' in words:
    timer = xchat.hook_timer(2000, send_raucher_message)


def send_raucher_message(userdata):
	global timer
	xchat.unhook(timer) 
	destination  = xchat.find_context(channel='#chaostal') 
	destination.command('say ' + choice(SPREUCHE))



xchat.hook_print('Channel Message', on_message)
print "%s loaded." % __module_name__
