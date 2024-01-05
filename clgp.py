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
  data=m.get_single_row(cur)
  logging.debug('user data:{}'.format(data))
  if(bcrypt.checkpw(request.POST.password.encode(),data[2].encode())):
    message='password success'
  else:
    message='password fail'    
  return template('check_login.tpl',post_table=common_d.list_post(),login_user='{}'.format(data),message=message)

#TEMPLATE_PATH = ['./', './views/']
