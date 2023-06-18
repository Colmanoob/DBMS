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
  
## Data Visualization

The visualization behavior depends on the type of data source you are using. The application automatically detects the data type and adjusts the visualization accordingly.

### MySQL Data Visualization

To visualize data from MySQL, follow these steps:

1. Generate a JSON object representing the MySQL table data. The structure should be as follows:

```json
{
  "type": "mysql",
  "table": {
    "name": "employees",
    "columns": ["id", "name", "age"],
    "rows": [
      [1, "John Doe", 30],
      [2, "Jane Smith", 25],
      [3, "Alice Johnson", 35]
    ]
  }
}
```
- Set "type" to "mysql" to indicate the data source as MySQL.
- Provide the "name" of the table.
- Specify the "columns" as an array of column names.
- Populate the "rows" with arrays representing the data for each row.
2. Upload the generated JSON object to the visualization tool.

### MongoDB Data Visualization

To visualize data from MongoDB, follow these steps:

1. Generate a JSON object representing the MongoDB collection data. The structure should be as follows:

```json
{
  "type": "mongodb",
  "collection": {
    "name": "users",
    "documents": [
      {
        "_id": "1",
        "name": "John Doe",
        "age": 30
      },
      {
        "_id": "2",
        "name": "Jane Smith",
        "age": 25
      },
      {
        "_id": "3",
        "name": "Alice Johnson",
        "age": 35
      }
    ]
  }
}
```
- Set "type" to "mongodb" to indicate the data source as MongoDB.
- Provide the "name" of the collection.
- Populate the "documents" with objects representing the data for each document. Ensure each document has an "_id" field.
2. Upload the generated JSON object to the visualization tool.
 
## Customization

You can customize the visualization appearance and behavior by modifying the code in the project files. The relevant files can be found in the `vsrc` directory.