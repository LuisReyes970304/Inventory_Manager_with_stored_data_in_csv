<h1>InventoryManager with csv database</h1>
<p>This is the version 0.3 of inventory manager it includes now a CRUD system with database in a csv file</p>

<h2>Files</h2>

- <h3>messages.py</h3> <p>This is the simples one, it take care of the styled message printed across the app, like the welcome message, the error messages and so on!<p>

- <h3>validation.py</h3> <p>This file takes care of the validation error and imports the sytled error messages from messages.py to look comfortable to the </p>

- <h3>app_tables.py</h3> <p>This is the file incharged of creating the tables in the console so is possible checking the products information in a very clear way, it has two functions that them are included in the class, it works with *rich* library</p>

- <h3>inventory.py</h3> <p>This is the principal file in the app because it has the two main classes that make the application works, it is based on a class that manage the CRUD system that allows creating, reading, updating and deliting information in the csv file, when there is not csv file, the class create it.
This file works importing the native csv library</p>

- <h3>main.py</h3> <p>The main.py file is the place in which we put all the functions together in a loop and in this way the system runs until the client decide to stop it an get the final receipt with the inventory</p>

h2>Language</h2>
<p>The languange used is Python splited in four files that interact by themselve across the application </p>

![Python](https://skillicons.dev/icons?i=python) 

<h3>Chartflow</h3>

![alt text](<Captura desde 2026-03-25 09-44-50.png>)

<h2>Author</h2>

Luis Reyes Caro  
Software Developer in Training