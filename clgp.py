#!/usr/bin/python3
from bottle import route, template, static_file,request
import sys, logging, bcrypt
import common_defination as common_d
import common_mysql as common_m

for handler in logging.root.handlers[:]:
  logging.root.removeHandler(handler)
    
logging.basicConfig(filename='/root/projects/clgp/error.log',level=logging.DEBUG,force=True)  

sys.path.append('/var/gmcs_config')
import astm_var_clg as astm_var
m=common_m.my_sql()
m.get_link(astm_var.my_host,astm_var.my_user,astm_var.my_pass,astm_var.my_db)

@route('/bootstrap/css/bootstrap.min.css')
def server_static():
  return static_file('bootstrap.min.css', root='/root/projects/clgp/bootstrap/css')

@route('/project_common.css')
def server_static():
  return static_file('project_common.css', root='/root/projects/clgp')
  
@route('/login')
def get_tat():
  return template("login.tpl")

@route('/check_login',method='POST')
def chk():
  cur=m.run_query('select * from user where user=%s',(request.POST.login,))
  user_info=m.get_single_row(cur)
  logging.debug('user data:{}'.format(user_info))


  '''
  Python: bcrypt.hashpw(b'mypassword',bcrypt.gensalt(rounds= 1,prefix = b'2b')
  PHP:    password_hash('mypassword',PASSWORD_BCRYPT);

  Python:bcrypt.checkpw(b'text',b'bcrypted password')
  PHP: password_verify('text,'bcrypted password')
  '''
  #try is required to cache NoneType exception when supplied hash is not bcrypt
  try:
    if(bcrypt.checkpw(request.POST.password.encode(),user_info[2].encode())):
      message='password success'
    else:
      message='password fail'
  except Exception as ex:
    logging.debug('{}'.format(ex))
    message='password can not be checked'
    
  #now modify password data display
  mypost=request.POST
  mypost['password']="****"
  if(user_info!=None):
    user_info=list(user_info) #tuple to list, to change password field
    user_info[2]='***'
  else:
    user_info=()
  user_info_columns=m.get_column_names(cur)
    
  return template(
                    'check_login.tpl',
                    post=mypost,
                    user_info=user_info,
                    user_info_columns=m.get_column_names(cur),
                    message=message)

#TEMPLATE_PATH = ['./', './views/']
