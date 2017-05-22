<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Untitled Document</title>
</head>

<body>
<form method="post" action="">
<pre>
	Employee Id	<input type="text" name="txt1" />
	<input type="submit" name="sub1" value="View" />
</pre>
</form>

<?php
$a=$_POST['txt1'];
if(isset($_POST['sub1']))
{
mysql_connect("localhost","root","root") or die(mysql_error());
mysql_select_db("kumar") or die(mysql_error());
$result=mysql_query("SELECT * from employee WHERE employeeid='$a'");
while($row=mysql_fetch_array($result))
{
$b=$row[0];
$c=$row[1];
$d=$row[2];
$e=$row[3];
$f=$row[4];
$g=$row[5];
$h=$row[6];
$i=$row[7];
$j=$row[8];
}

echo("<table border=5 cellpaddimg=5>
<tr><td>Employee ID </td> <td>$b</td></tr>

<tr><td>Employee Name </td> <td>$c</td></tr>

<tr><td>Date of Birth</td> <td>$d</td></tr>

<tr><td>Date of Joining</td> <td>$e</td></tr>

<tr><td>Designation</td> <td>$f</td></tr>

<tr><td>Address</td> <td>$g</td></tr>

<tr><td>Phone No</td> <td>$h</td></tr>

<tr><td>Blood Group</td> <td>$i</td></tr>

<tr><td>Basic Pay</td> <td>$j</td></tr>
</table>");
}

?>	
</body>
</html>
