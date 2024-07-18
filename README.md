Basic aplication using Sanic framework:

**Installation requiremnets:**
pip install requirments.txt

**Running apllication:**
python app.py

Note: Have created a simple postgresql server, so u can use the table in it. Have given the Database URL in the code

**Description:**

Created the application to do basic Crud operation for sales per location data using get,post delete methods.
After running the application we can access the following url,

get: http://localhost:8000/sales
Here we can fetch the sales table details from the Database

get with filter: (http://localhost:8000/sales?location=America)
Here we can fetch the sales table details of particular filter (columns of the DB) from the Database

post: (http://localhost:8000/sales)   ---->> curl -X POST "http://localhost:8000/sales" -H "Content-Type: application/json" -d '{"location": "NewYork", "amount": 100.0}'
Here we can create the sales table details for the database

delete: (http://localhost:8000/sales/1)
Here we can delete the sales table details(with id) from the Database
