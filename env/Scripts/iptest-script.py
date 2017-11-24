#!D:/Anaconda2/envs/ece180final\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==5.4.1','console_scripts','iptest'
__requires__ = 'ipython==5.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ipython==5.4.1', 'console_scripts', 'iptest')()
    )
