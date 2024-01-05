from bottle import request
import common_mysql as common_m
def list_post():
  x="<table border=1><tr><th>POST</th><th>Value</th></tr>"
  r=request.POST
  for key in r:
    x=x+'<tr><td>{}</td><td>{}</td></tr>'.format(key,r[key])
  return x+'</table>';
  
