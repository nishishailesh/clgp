#!/usr/bin/python3
import os, sys
os.chdir(os.path.dirname(__file__)) #for template relative path bottle.py: TEMPLATE_PATH = ['./', './views/']
sys.path.append('/root/projects/clgp')  #to import bottle and clgp
import bottle #used by last line
import clgp   #entry point used by following line
application = bottle.default_app()
