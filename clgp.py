#!/usr/bin/python3
#sys.path is appended by wsgi.py
from bottle import route, template, static_file,request
import sys, logging, bcrypt
import config
logging.basicConfig(filename=config.log_filename,level=logging.DEBUG,force=True)  
logging.debug(sys.path) #appended by wsgi.py, used to find config

import common_defination as common_d
import common_mysql as common_m

import importlib
import secrets

#for handler in logging.root.handlers[:]:
#  logging.root.removeHandler(handler)

sys.path.append(config.mysql_secret_file_location)
astm_var = importlib.import_module(config.mysql_secret_module, package=None)


#import astm_var_clg as astm_var
m=common_m.my_sql()
m.get_link(astm_var.my_host,astm_var.my_user,astm_var.my_pass,astm_var.my_db)

@route('/bootstrap/css/bootstrap.min.css')
def server_static():
  return static_file('bootstrap.min.css', root=config.project_dir+'/bootstrap/css')

@route('/project_common.css')
def server_static():
  return static_file('project_common.css', root=config.project_dir)

@route('/')
def get_tat():
  return template("login.tpl")
    
@route('/login')
def get_tat():
  return template("login.tpl")

@route('/check_login',method='POST')
def chk():
  cur=m.run_query('select * from user where user=%s',(request.POST.login,))
  user_info=m.get_single_row(cur)
  logging.debug('user data:{}'.format(user_info))

  '''
  Python: bcrypt.hashpw(b'mypassword',bcrypt.gensalt(rounds= 4,prefix = b'2b')
  PHP:    password_hash('mypassword',PASSWORD_BCRYPT);

  Python:bcrypt.checkpw(b'text',b'bcrypted password')
  PHP: password_verify('text,'bcrypted password')
  '''
  #try is required to cache NoneType exception when supplied hash is not bcrypt
  try:
    if(bcrypt.checkpw(request.POST.password.encode(),user_info[2].encode())):
      message='password success'
      token=secrets.token_hex(15)
      hashed_token=bcrypt.hashpw(token.encode(),bcrypt.gensalt(rounds= 4,prefix = b'2b'))
      '''
      save token in mysql with timestamp
      supply hashed_token to all forms
      
      
      
      '''
      
      #now modify password data display
      mypost=request.POST
      mypost['password']="****"   #dictionary is mutable
      user_info=list(user_info) #tuple(immutable) to list, to change password field
      user_info[2]='***'
      user_info_columns=m.get_column_names(cur)
      return template(
                      'login_success.tpl',
                      post=mypost,
                      user_info=user_info,
                      user_info_columns=m.get_column_names(cur),
                      message=message,
                      token=token)
    else:
      message='password fail'
      return template('login_fail.tpl',message=message)
  except Exception as ex:
    logging.debug('{}'.format(ex))
    message='password can not be checked:{}'.format(ex)
    return template('login_fail.tpl',message=message)

#TEMPLATE_PATH = ['./', './views/']
