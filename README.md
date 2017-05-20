# Songz

# Set-up Specifications

This project is set up using AWS RDS for the MySQL Server and MonogoDB for the NoSQL Server. Database management is up to user discretion although during development MySQL Workbench and terminal were used. 

# Instructions and Basic Layout
As of May 19 2017, both AWS and Mongo Servers have been taken down. You may test and modify the code by creating your own AWS and Mongo servers and update the connection endpoints in the project code.

Run "node app.js" in Frontend to run the application

app.js is used to initialize the website and set which functions the getters use.

The routes folder contains .js files which are used to render pages sometimes with information obtained by querying the database.

The views folder contains .jade files used in the render of pages to setup the navbar, the search forms (descritpion, textbox, submission buttoons), and display results in tables.

In general, page1 and page2 refer to the search pages for sql and nosql respectively. page1xyz refers to a particular search within the sql database with an acronym similar to xyz. similarly, page2xyz refers to a particular search within the nosql database with an acronym similar to xyz.

