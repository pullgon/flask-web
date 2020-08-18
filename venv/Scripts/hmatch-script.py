#!D:\dev\pycharm\flask_web\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'request==1.0.117','console_scripts','hmatch'
__requires__ = 'request==1.0.117'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('request==1.0.117', 'console_scripts', 'hmatch')()
    )
