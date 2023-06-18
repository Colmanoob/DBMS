import matplotlib.pyplot as plt
import json
import PythonInterface  # Assuming pythoninterface.py returns mySQL_Result and mongo_Result
with open(r'C:\Users\colma\Downloads\DBMS\db_tables_columns.json', 'r') as file:
    json_data = json.load(file)
# Retrieve JSON data from pythoninterface.py
mySQL_Result, mongo_Result = json_data,json_data#PythonInterface.QueryToMySQL_MongoDB(Inputted_SQL_query = r"SELECT * FROM HWs.student WHERE 學號='B07202043'")

# Visualizing JSON Objects from MySQL (SQL)
def visualize_mysql_data(json_objects):
    # Process and visualize the JSON data
    # Example: Creating a bar chart
    data = []
    labels = []
    for obj in json_objects:
        data.append(obj['value'])
        labels.append(obj['label'])

    plt.bar(labels, data)
    plt.xlabel("Labels")
    plt.ylabel("Values")
    plt.title("Visualization of JSON Objects from MySQL")
    plt.show()

# Visualizing JSON Objects from MongoDB (NoSQL)
def visualize_mongodb_data(json_objects):
    # Process and visualize the JSON data
    # Example: Creating a pie chart
    data = {}
    for obj in json_objects:
        label = obj['label']
        if label in data:
            data[label] += 1
        else:
            data[label] = 1

    labels = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Visualization of JSON Objects from MongoDB")
    plt.show()

# Call the visualization functions with the retrieved JSON data
visualize_mysql_data(mySQL_Result)
visualize_mongodb_data(mongo_Result)
