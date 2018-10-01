from flask import Flask, request, render_template
from instantSearch import InstantSearch
import json

filename = 'data.csv'
iSearch = InstantSearch()

app = Flask(__name__)

# indexting this route to index page
@app.route('/')
def index():
      return render_template('index.html')

@app.route('/search/<string:name>')
def autoSearch(name):
      log= open("result.log","w+")
      result = iSearch.autoCompelete(name)
      for r in result:
            log.write(r+"\n")
      # print(result)
      log.close()
      return json.dumps(result),200

if __name__=="__main__":
      print("server started")
      iSearch.loadData(filename)
      app.run(debug=True,port=8888)