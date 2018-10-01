# Simple Search for a Names CSV

* A Fast Search Data Structure
* An API which responds to a search query searches the source file [`data.csv`](https://drive.google.com/open?id=1zDicarnkZj17R9QVydo6agpb5LE5XaLC) contains > 300k names.


Install flask:

```
pip install flask
```

### Starting the Server
* In command line Locate to current working directory 
* Use the following command to start the server
```
python server.py
```

### Accessing API
* use the following urls for accesing the url

      http://localhost:8888/search/{{name}} 


### InstantSearch Data Structure  
* Actual Data Structure is implemented in fastDataStructure.py
* server api interact with instantsearch.py for accesing the Data structure 

