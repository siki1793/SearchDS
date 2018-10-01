var previousValue = "";

function addRow(table,data){
      // console.log(data);
      var rowCount = table.rows.length;
      var row = table.insertRow(rowCount);
      var nameCell      = row.insertCell(0);
      var charLenCell    = row.insertCell(1);
      nameCell.innerHTML = data;
      charLenCell.innerHTML = data.length;
  
  }

function reqListener(){
      console.log(this.responseText);
      return this.responseText;
}
function getData(value){
      var data ="";
      var tableID = "data";
      var table=document.getElementById(tableID);
      var xhr = new XMLHttpRequest();
      // xhr.addEventListener("load",reqListener)
      xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                  data = this.responseText;
                  console.log(data);
                  var result = JSON.parse(data);
                  result.sort();
                  document.getElementById("resultSet").innerHTML="<strong>Found "+result.length+" Names</strong>";
                  for(var i=0;i<result.length;i++){
                        addRow(table,result[i]);
                  }
                        return data;
           }
        };
      xhr.open("GET", "http://localhost:8888/search/"+value, true);
      xhr.send();
      
}

function autoCompelete(value){
      console.log(value);
      var tableID = "data";
      var table=document.getElementById(tableID);
      table.innerHTML = "";
      var resultSet = document.getElementById("resultSet")
      if(value.length>3){ 
            console.log(getData(value));
            
      }else{
            resultSet.innerHTML="<strong>Input must be greater than 3 letters</strong>";
      }

}

function searchFunction(){
      var value = document.getElementById("searchInput").value;
      if(previousValue!=value && value!=""){
            autoCompelete(value)
      }
      previousValue=value;

}



