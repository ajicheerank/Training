<?php

$username = "sa_aji";

$password = "password123";

$hostname = "aji-db-instance.cm6vdj3ydhy2.us-east-1.rds.amazonaws.com";

$dbname = "mysql_db_test";



//connection to the database

$dbhandle = mysql_connect($hostname, $username, $password) or die("Unable to connect to MySQL");

echo "Connected to MySQL using username - $username, password - $password, host - $hostname<br>";

$selected = mysql_select_db("$dbname",$dbhandle)   or die("Unable to connect to MySQL DB - check the database name and try again.");

?>