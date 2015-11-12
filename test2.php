<html>
<head>
<title>test</title>
</head>

<body>
	<?php
		//połączenie z bazą 
		$Connection = ocilogon("rt_projekt","projekt");
		//zapytanie
		$Query = "SELECt *FROM USERTABLES";
		
		//interpetacja zapytania
		$Statement = ociparse($Connection,$Query);
	
		//zamkniecie polaczenia
		ocilogoff($Connection);
	?>
	
</body>

</html>
