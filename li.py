#!/usr/bin/python3
import os
import config
print(config.project_dir)
loginnn="""
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<form method=post action="check_login" class="bg-light">
<div class="form-group">
  <label for=login class="text-danger" >Login</label><input id=login type=text name=login>
</div>
<div class="form-group">
  <label for=password>Password</label><input id=password type=password name=password>
</div>
<div class="form-group">
  <input name=action value=login type=submit>
</div>
</form>
"""
print(loginnn)

b="""
asdasda
asdasda
asdasdas
asdasdsa
"""
print(b)

print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
