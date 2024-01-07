<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<table class="table table-sm table-striped">
%for i in post:
  <tr><td>{{i}}</td><td>{{post[i]}}</td></tr>
%end
</table>

