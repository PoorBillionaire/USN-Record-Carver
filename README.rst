USN-Record-Carver
=====================      
Python script to carve NTFS USN records from arbitrary binary data

Description
-------------
The NTFS USN Change journal is a volume-specific log  which records metadata changes to files. It is a treasure trove of information during a forensic investigation. As the change journal reaches its maximum size, clusters of the journal's disk space are marked unallocated by the operating system to be used when needed at a later time. As with many other artifacts, USN change journal records in unallocated space can be extremely valuable. Better yet, due to the compact nature of change journal records, I routinely find millions of records outside of the file system's allocated clusters.

This script will carve NTFS USN journal records from arbitrary binary data, and output to a file in binary format. The investigator can then parse these records with a tool of their own choosing. At this time the script only supports raw/dd input files.

Usage and  Output
--------------------
Simply specify the input and output files:

::

    dev@computer:$ python usncarve.py -f file.raw -o usn.raw

Command-Line Options
-----------------------

::

    usage: usncarve.py [-h] -f FILE -o OUTFILE

    optional arguments:
        -h, --help            show this help message and exit
        -f FILE, --file FILE  Carve USN records from the given file
        -o OUTFILE, --outfile OUTFILE
                            Output to the given file


Installation 
--------------
Using setup.py:

::
    
    python setup.py install
    
Using pip:

::
    
    pip install usncarve

+----------------------------------------------------------------------------------------+
| Travis-CI                                                                              |
+========================================================================================+
|  .. image:: https://travis-ci.org/PoorBillionaire/USN-Record-Carver.svg?branch=master  |
|   :target: https://travis-ci.org/PoorBillionaire/USN-Record-Carver                     |
+----------------------------------------------------------------------------------------+
