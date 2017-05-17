# Table of Contents
1. [Challenge Summary](README.md#challenge-summary)
2. [Details of Implementation](README.md#details-of-implementation)
3. [Description of files](README.md#description-of-files)
4. [Repo directory structure](README.md#repo-directory-structure)
5. [Trouble shooting](README.md#trouble-shooting)


# Challenge Summary

A NASA fan website that generates a large amount of Internet traffic data: this project performs basic analytics on the server log file, provide useful metrics, and implement basic security measures. 

The features are described below: 

### Feature 1: 
Top 10 most active host/IP addresses that have accessed the site.

### Feature 2: 
The 10 resources that consume the maximum bandwidth on the site.

### Feature 3:
List of the top 10 busiest (or most frequently visited) 60-minute periods. 

### Feature 4: 
Detection of patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes. 

### Feature 5 (Additional):
List of top 10 popular resources that are most accessed by different users. Multiple access by the same IP address don't count. 

### Feature 6 (Additional):
Prints rolling number of users for the last 60 seconds at the arrival of every request.


## Details of Implementation

The code does not require any special library or package. All of the modules and source code are added in the `/src` repo. The input file is `log.txt`, which is read line by line. 

This code runs on `python3.0`. It may not run correctly for other earlier versions of python.  

### How to run the code:
#### Step 1: 
Clone this git repository. 
#### Step 2:
Once the download is complete, your local repository will have a folder called `/insight_challenge`. Enter into the this repository. To get a better understanding of the repo structure, please refer to the figure below. 
#### Step 3:
Place the input file `log.txt` in `/log_input` directory. 
#### Step 4:
With `/insight_challenge` as the working directory, following will execute the code:

For Windows:

`insight_challenge~$ run.sh`

For Linux:

`insight_challenge~$ bash run.sh` 

#### Step 5:
The output files will be saved in `/log_output`. To get the additional feature(s), some parts of the file `process_log.py` need to be modified (see below). 

#### Computing additional Features:
In order to calculate the additional features, we need to make minor changes in `process_log.py`. For example, to calculate feature 5, we will need to set the flag `feature_five_flag` to be `TRUE`. Similar action needed for feature 6. 

### Viewing the output:
All outputs are saved in `/log_output`. Several generated `.txt` files correspond to different features that has been calculated.

Feature 1 is saved in `hosts.txt`.

Feature 2 is saved in `resources.txt`.

Feature 3 is saved in `hours.txt`.

Feature 4 is saved in `blocked.txt`.

Feature 5 is saved in `connectedIP.txt`.

Feature 6 is saved in `user.txt`


### Running tests:
There is included a test script, called `run_tests.sh` in the `insight_testsuite` folder. One can run the test from `insight_testsuite` folder:

For Windows:

`insight_testsuite~$ run_tests.sh`

For Linux:

`insight_testsuite~$ bash run_tests.sh`  

## Description of files:

Several source files that can be found in `/src` are described as follows (in alphabetical order):

### blocked.py:
This module saves the hosts with failed attempts under the instance of the class `Fail` and registers them into the `blocked` feature of the `Fail` class if the number of failed attempts from the same host reaches three within a time frame of 20 secs. To remove entries earlier than 20 secs, a MinHeap is used where the heap property is decided by the timestamp. This module is used to calculate feature FOUR.   

### features.py:
The desired features to be calculated are defined here. Each feature is calculated by defining a python function. These python functions take the saved instances (`Host`,`Hour`,`Resource`, etc.) and use a priority queue (MaxHeap) to yeild top ten entries of those instances.

### graph.py:
This module will store the resources accessed by different hosts. It can be used to calculate feature FIVE. Also, this can provide a list of hostnames which may share common interests.  

### heap.py:
A general heap structure has been implemented. Each node in the heap has two values. The heap property is based on the second key. For this challenge, we will
use MaxHeap only. The MinHeap may be used to compute additional features.

### host.py:
This module stores the hostnames(`IP address`) and their count in a python dictionary while the file is being read line by line.
The data is saved under the class `Host`. This class is constructed to calculate feature ONE. 

### hour.py:
All possible timestamps each of one second are stored in a python dictionary. Each timestamp that appears on the dataset falls on all timestamps that are within 60 seconds of its own. The data is saved under class `Hour`. This class is constructed to calculate feature THREE. 

### process_log.py:
This is the main program file. 
	
### resource.py:
The resources accessed by the hosts(`IP address/website`) are saved in a python dictionary. The data is saved under the class `Resource`. This class is used to calculate feature TWO.

### user.py:
This module saves number of users for the last 60 seconds at at the arrival of every timestamp. To implement this, a proirity queue (MinHeap) has been used.

## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── process_log.py
    ├── log_input
    │   └── log.txt
    ├── log_output
    |   └── hosts.txt
    |   └── hours.txt
    |   └── resources.txt
    |   └── blocked.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_features
            |   ├── log_input
            |   │   └── log.txt
            |   |__ log_output
            |   │   └── hosts.txt
            |   │   └── hours.txt
            |   │   └── resources.txt
            |   │   └── blocked.txt
            ├── your-own-test
                ├── log_input
                │   └── your-own-log.txt
                |__ log_output
                    └── hosts.txt
                    └── hours.txt
                    └── resources.txt
                    └── blocked.txt


# Trouble shooting

It is essential that `python3` is installed and loaded in the system.  

#### Case 1:
While executing `run.sh`, you see something like this:

`Traceback (most recent call last):`

`  File "./src/process_log.py", line 31, in <module>`

`    f = open('./log_input/log.txt','r',encoding = "ISO-8859-1")`

 Possible reason: python3 not loaded/installed. 
 
 Action: Open the `run.sh` file. In line line 7, change `python` to `python3`.   

#### Case 2:
While executing `run.sh`, you see something like this:

`Traceback (most recent call last):`

`  File "./src/process_log.py", line 105, in ?`

`    t = datetime.strptime(time.split()[0].strip(), "%d/%b/%Y:%H:%M:%S")`

`AttributeError: type object 'datetime.datetime' has no attribute 'strptime'`

 Possible reason: python3 not loaded/installed. 
 
 Action: Open the `run.sh` file. In line line 7, change `python` to `python3`.   












