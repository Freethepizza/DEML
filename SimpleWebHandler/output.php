<?php
/*
$file = 'test.deml';
$received = $_POST["deml-code"];
echo $received;
file_put_contents($file, $received);
*/

$received = $_POST["deml-code"];
$file = "a.deml"; 
$handle = fopen($file, 'w');
fwrite($handle, $received); 
fclose($handle); 


echo "<br><br>";
$salida2 = system('python3 deml.py 2>&1', $out);
print($out);
?>
