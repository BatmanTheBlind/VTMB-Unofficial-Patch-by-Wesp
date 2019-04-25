#!BPY

"""
Name: 'Save Current Theme...'
Blender: 240
Group: 'Export'
Tooltip: 'Save current theme as a BPython script'
"""

__author__ = "Willian P. Germano"
__url__ = ("blender", "elysiun")
__version__ = "2.41 2006/01/16"

__bpydoc__ = """\
This script saves the current Theme in Blender as a Blender Python script.

Usage:

Use Blender's Theme tab in the User Preferences window to create and name your
theme, then run this script from the File->Export menu to save it.

It is saved as a bpython script, meaning that you can simply run it to change
the current theme.  By default it is currently saved under the
"Misc" group, available only from the Scripts window "Scripts->Misc" menu.

To appear in the menu, a theme saved with this script must be put in your
Blender's scripts dir, that's what happens by default when you save one by
yourself.  If you don't know where this dir is, running

import Blender<br>print Blender.Get("scriptsdir")

on the Text Editor window (use menu or ALT+P to run it) will write the path on
the console.

Remember to edit your exported theme's source file to put your name and
some information on it before sharing it with others.
"""

# $Id: save_theme.py,v 1.10 2006/01/29 19:17:53 ianwill Exp $
#
# --------------------------------------------------------------------------
# Copyright (C) 2004: Willian P. Germano, wgermano _at_ ig com br
# --------------------------------------------------------------------------
# The scripts generated by this script are put under Public Domain by
# default, but you are free to edit the ones you generate with this script
# and change their license to another one of your choice.
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2005: Willian P. Germano, wgermano _at_ ig.com.br
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

import Blender
from Blender.Window import Theme, FileSelector

theme = Theme.Get()[0] # get current theme

# default filename: theme's name + '_theme.py' in user's scripts dir:
default_fname = Blender.Get("scriptsdir")
default_fname = Blender.sys.join(default_fname, theme.name + '_theme.py')
default_fname = default_fname.replace(' ','_')

def write_theme(filename):
	"Write the current theme as a bpython script"

	if not filename.endswith('.py'): filename += '.py'

	fout = file(filename, "w")

	fout.write("""#!BPY

# \"\"\"
# Name: '%s'
# Blender: 241
# Group: 'Themes'
# Tooltip: 'Change current theme'
# \"\"\"

__%s__ = "????"
__%s__ = "2.41"
__%s__ = ["blender"]
__%s__ = \"\"\"\\
You can edit this section to write something about your script that can
be read then with the Scripts Help Browser script in Blender.

Remember to also set author, version and possibly url(s) above.  You can also
define an __email__ tag, check some bundled script's source for examples.
\"\"\"

# This script was automatically generated by the save_theme.py bpython script.
# By default, these generated scripts are released as Public Domain, but you
# are free to change the license of the scripts you generate with
# save_theme.py before releasing them.

import Blender
from Blender.Window import Theme

theme = Theme.New('%s')
""" % (theme.name, "author", "version", "url", "bpydoc", theme.name))

	for tsp in theme.get(): # 
		command = "\n%s = theme.get('%s')" % (tsp, tsp)
		fout.write(command + "\n")
		exec(command)
		exec("vars = dir(%s)" % tsp)
		vars.remove('theme')

		for var in vars:
			v = "%s.%s" % (tsp, var)
			exec("value = %s" % v)
			fout.write("%s = %s\n" % (v, value))

	fout.write('\nBlender.Redraw(-1)')
	fout.close()
	try:
		Blender.UpdateMenus()
	except:
		Blender.Draw.PupMenu("Warning - check console!%t|Menus could not be automatically updated")

FileSelector(write_theme, "Save Current Theme", default_fname)
