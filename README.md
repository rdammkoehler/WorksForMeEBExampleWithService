# Example Service Use

1) Run the service

```bash
	python n/s/s.py start
```

2) Run the Pinger

```bash
	python n/s/pinger.py
```

3) Look at the log files

* Each process has a log file
* MyService logs to the myservice.log file, nothing really interesting here
* Ponger, a process startded by MyService, logs to ponger.log.
	* After step one this will just tell you that the ponger is waiting
	* After step two you will see the receipt of the ping
* Pinger, a process started by you in step 2, logs to pinger.log.
	* Not too exciting, you will see the logging of Pinger sending its ping

Works for me, how about you?	 
