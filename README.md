# DiskStats

This is a simple Python script on Linux which is used to traverse the directories and files, determine the size of the directories, and generate a disk usage statistics report in CSV format. Module ```sys.argv``` is used to access the terminal command line. 

### Script Execution
To run the script, follow the steps below: 

* Set up virtual environment 
```bash
~$ virtualenv env
```
* Activate virtual environment
```bash
~$ source env/bin/activate 
```
* Install dependencies
```bash
~$ pip install -r requirements.txt
```
* Run script
```bash
~$ ./disk_report.py /TARGET_DIRECTORY/
```
