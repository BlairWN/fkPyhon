<?php
require "init.php";
include "page1.php";
?>
<html>
<head>
	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>

<style type="text/css">
  div{
width:auto;
margin:auto;
padding:20px;
}
h1
{
	margin: auto;
    width: 30%;
    padding: 10px;
}
</style>
<title>
<?php echo $lang["page"];?>
</title>
<h1><span>
<?php
echo $lang["motto"];
?></span></h1>
</head>
<body>
  <div>
<p>
<?php
echo $lang["pag1"];
?>
</p>
</div>
<div>
<p>
 <?php
echo $lang["pag2"];
?> 
</p>
</div>

<p>
<?php
echo $lang["pag3"];
?></p>
</div>
</body>
</html>