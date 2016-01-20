# infpro-9

THIS IS MADLOG README.

CONFIGURATION:

1. First you need working python3 environment. I RECOMMEND version 3.4.
2. Then:
  2.1. Get Oracle Instant client from this site:

http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html

  2.2. You need these components: Client Package - Basic, SQL*Plus, SDK and probably ODBC.
  
  2.3. Put these in ONE folder (will make configuration easier).
  
  2.4. Prepare tnsnames.ora file (recommended in Instant Client directory). Example below.
  
  2.5. You must set up global environment variables in system in order to make Oracle Instant working.
  
  2.6. Set these variables (process is different on each operating system):
  
    a) ORACLE_HOME - pointing to the directory with Instant Client
    
    b) TNS_ADMING - pointing to the directory with tnsnames.ora file.
    
    
TNSNAMES.ORA EXAMPLE:
UMAIN =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = oracle1.pkif.us.edu.pl)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = umain.pkif.us.edu.pl)
    )
  )

USAGE:

1. Put main.py in folder containing TXXX_(...).txt files.
2. Run main.py located in /madlog/ directory in your prefered Python IDE.
