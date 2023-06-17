# Installation and Configuration of Apache Drill
1. The installation is mainly refer to the following website:
	a. https://www.tutorialspoint.com/apache_drill/apache_drill_installation.htm
	b. The quickest way is install the embedded mode as we did in the final demo.
2. After the installation, we have to configure storage metric in order to connect Apache Drill to MySQL and MongoDB installed on the local machine.
	a. Start the embedded mode Apache Drill shell with the command of "bin/drill-embedded" in Apache Drill's directory.
	b. Connect to http://localhost:8047/storage (default port, might be different if the port is used).
	c. Create a new storage plugin for MySQL.
		- Ref Website: https://medium.com/lumiq-tech/apache-drill-exploring-connecting-to-rdbms-via-jdbc-c014538007fc
	d. Enable storage plugin for MongoDB.
		- Ref Website: https://drill.apache.org/docs/mongodb-storage-plugin/
3. Then, we may start to drill. Query may be done in several ways
	a. In Drill Shell (where we type "bin/drill-embedded")
		- Directly Type in the query command in the shell.
	b. Through 3rd party programming language. For eg, python.
		- The code submmitted is done through this way.

# Installation of PyDrill:
- This is a python library which enable us to connect to Apache Drill from python.
- The installation is rather simple which may be done using 'pip'.
	- For e.g., pip install pydrill.# DBMS
