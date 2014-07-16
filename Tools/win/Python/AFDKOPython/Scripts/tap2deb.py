#!/AFDKOPythonBuild/bin/python2.7

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
tap2deb
"""

### Twisted Preamble
# This makes sure that users don't have to set up their environment
# specially in order to run these programs from bin/.
import sys, os, string
if string.find(os.path.abspath(sys.argv[0]), os.sep+'Twisted') != -1:
    sys.path.insert(0, os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir)))
### end of preamble

from twisted.scripts import tap2deb
tap2deb.run()
