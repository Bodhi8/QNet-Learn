/usr/bin/env python

# License: 3-clause BSD

import sys
import os
import platform
import shutil
from distutils.command.clean import clean as Clean
from pkg_resources import parse_version
import traceback
try:
    import builtins
except ImportError:
   
import __builtin__ as builtins
