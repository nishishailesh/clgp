<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="project_common.css">
<h3>Login</h3>
<form method=post action="check_login" class="bg-light" >
<div class="form-group">
  <label for=login class="text-danger" >Login</label><input id=login type=text name=login class=form-control>
</div>
<div class="form-group">
  <label for=password>Password</label><input id=password type=password name=password class=form-control>
</div>

  <input name=action value=login class="btn btn-primary" type=submit>

</form>
