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
<table class="table">
   <thead>
      <tr>
         <td><?php echo $lang["Name"];?></td>
         <td><?php echo $lang["name"];?></td>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><?php echo $lang["Sex"];?></td>
         <td><?php echo $lang["gender"];?></td>
      </tr>
      <tr>
         <td><?php echo $lang["Age"];?></td>
         <td><?php echo $lang["age"];?></td>
      </tr>
       <tr>
         <td><?php echo $lang["Major"];?></td>
         <td><?php echo $lang["major"];?></td>
      </tr>
      <tr>
         <td><?php echo $lang["Idol"];?></td>
         <td><?php echo $lang["idol"];?></td>
      </tr>
   </tbody>
</table>
</body>
</html>