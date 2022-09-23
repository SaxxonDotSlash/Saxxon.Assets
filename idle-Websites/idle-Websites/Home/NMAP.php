<?php
$ip_addr = $_POST["ip-addr"]
$ports = $_POST["port-range"]
exec ('nmap' + $ip_addr)
?>