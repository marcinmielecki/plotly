<?php
/*===========================================================
plik tnsnames.ora potrzebny do polaczenia 
UMAIN =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = oracle1.pkif.us.edu.pl)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = umain.pkif.us.edu.pl)
    )
  )*/
/*============================================================
Laczenie z baza 
*/

$conn = oci_connect('rt_projekt', 'projekt', '(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = oracle1.pkif.us.edu.pl)(PORT = 1521)))(CONNECT_DATA =(SERVICE_NAME = umain.pkif.us.edu.pl)))'); // polecenie laczenia 
if (!$conn) {
    $e = oci_error();
    trigger_error(htmlentities($e['message'], ENT_QUOTES), E_USER_ERROR);
}

$stid = oci_parse($conn, 'SELECT * FROM TESTOWA');
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>" . ($item !== null ? htmlentities($item, ENT_QUOTES) : "&nbsp;") . "</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

?>
