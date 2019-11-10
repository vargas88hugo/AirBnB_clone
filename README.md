## AirBnB clone - The console

<p align="center"><img width="250" src="https://i.ibb.co/fk6gjPW/airbnb.png" alt="printf logo"></a></p>

## Description

This repository contains the console of AirBnB clone, which is a command interpreter to manipulate data without a visual interface, like in a Shell. This project is a project requested by [Holberton School](https://www.holbertonschool.com/)


## Prerequisites 📋

All our files are interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3):

### On any terminal:

Mode Interactive

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$</code></pre>

Mode Non-Interactive

<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$</code></pre>


### Options :mag_right:

The following commands are available in the console, the main class is BaseModel:
<ul>
  <li>
    <b>create:</b> Creates a new instance of the class. Ex: <code>$ create BaseModel</code>
  </li>
  <li>
    <b>show:</b> Prints the string representation of an instance based on the class name and id. Ex: <code>$ show BaseModel 1234-1234-1234</code>
  </li>
  <li>
    <b>destroy:</b> Deletes an instance based on the class name and id. Ex: <code>$ destroy BaseModel 1234-1234-1234</code>
  </li>
  <li>
    <b>all:</b> Prints all string representation of all instances based or not on the class name. Ex: <code>$ all BaseModel</code> or <code>$ all</code>
  </li>
  <li>
    <b>update:</b> Updates an instance based on the class name and id by adding or updating attribute. Ex: <code>update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</code> 
  </li>
</ul>

### Example :mag_right:

Testing on interactive mode:
<code><pre>(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) </code></pre>


## Running the tests ⚙️
All our tests are executed by using this command in the root directory of the project: <code>python3 -m unittest discover tests</code>


## Authors :copyright:

* **Hugo Emilio Vargas Celis** - [Github](https://github.com/vargas88hugo)

* **Edgar Carlos Mauricio Quintero Romero** - [Github](https://github.com/alzheimeer)

