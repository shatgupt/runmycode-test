<?php
echo "Hello World from php!\n";
echo count(array_slice($argv, 1)), " Args: [", implode(', ', array_slice($argv, 1)), "]\n";
?>
