<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
%include('post.tpl')
<table class="table table-sm table-striped table-bordered">
  
<tr>
%for i in user_info_columns:
  <td>{{i}}</td>
%end
</tr>
<tr>
%for i in user_info:
  <td>{{i}}</td>
%end
</tr>
</table>
<h3 class="text-success">{{message}}</h3>
<h3 class="text-success">{{token}}</h3>
<form method=post>
<input type=hidden name=token value={{token}}>
<input type=submit name=action value=submit>
</form>
