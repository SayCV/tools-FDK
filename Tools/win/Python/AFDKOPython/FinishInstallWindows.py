##***********************************************************************#
#*                                                                     *#
#* Copyright 2008, 2009 Adobe Systems Incorporated.                          *#
#* All rights reserved.                                                *#
#*                                                                     *#
#* Patents Pending                                                     *#
#*                                                                     *#
#* NOTICE: All information contained herein is the property of Adobe   *#
#* Systems Incorporated. Many of the intellectual and technical        *#
#* concepts contained herein are proprietary to Adobe, are protected   *#
#* as trade secrets, and are made available only to Adobe licensees    *#
#* for their internal use. Any reproduction or dissemination of this   *#
#* software is strictly forbidden unless prior written permission is   *#
#* obtained from Adobe.                                                *#
#*                                                                     *#
#* PostScript and Display PostScript are trademarks of Adobe Systems   *#
#* Incorporated or its subsidiaries and may be registered in certain   *#
#* jurisdictions.                                                      *#
#*                                                                     *#
#***********************************************************************#
"""
FinishInstallWindows.py v1.0 June 3 2011
"""

import sys
import os
kAFDKOPythonName = "AFKDOPython27"

import _winreg

def isNotAFDKOPythyonDir(dirPath):
	# Check if this path contains AFKDOPython27
	if kAFDKOPythonName in dirPath:
		print "Removing previous path from the path environment variable '%s'." % (dirPath)
		return 0
	else:
		return 1
	
def removeOldFDKDirectories(path):
	dirList = path.split(";")
	dirList = filter(isNotAFDKOPythyonDir, dirList)
	path = ";".join(dirList)
	return path
	
def getRegistryValue(registry, key, name):
	kHandle = _winreg.OpenKey(registry, key)
	value = _winreg.QueryValueEx(kHandle, name)[0]
	_winreg.CloseKey(kHandle)
	return value

def setRegistryValue(registry, key, name, value, valueType=_winreg.REG_SZ):
	kHandle = _winreg.OpenKey(registry, key, 0, _winreg.KEY_WRITE)
	_winreg.SetValueEx(kHandle, name, 0, valueType, value)
	_winreg.CloseKey(kHandle)

def main():
	fdkPythonPath = os.path.abspath(os.path.dirname(__file__))

	try:
		registry = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
		key = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
		path = getRegistryValue(registry, key, "Path")
		path = removeOldFDKDirectories(path)
		path += ";" + fdkPythonPath
		print "Adding the AFDKO Python command home dir '%s' to the system environment variable PATH." % (fdkPythonPath)
		setRegistryValue(registry, key, "Path", path, _winreg.REG_EXPAND_SZ)
		print "Success."
		print "You now need to log off or restart; the AFDKO Python command '%s' will then work in a new command window." % (kAFDKOPythonName)
	except:
		print "Error", repr(sys.exc_info()[1])
		if "Access" in repr(sys.exc_info()[1]):
			print "You need system admin privileges to run this script."
		else:
			print "You will have to manually add the path to the AFDKO Python command home directory to the system environment variable PATH."
		print "Quitting. Failed to add the AFDKO Python command home directory to the system environment variable PATH."
	return
	



if __name__=='__main__':
	main()
