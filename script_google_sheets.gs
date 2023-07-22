// Setting button
function onOpen(){
  var ui = SpreadsheetApp.getUi(); // acessing spreadsheet
  ui.createMenu('Health Insurance') // creating the button
    .addItem('Get predictions', 'Predict_all') // adding functionalities to button, function 'Predict_all' makes API request
    .addToUi() 
}


//host_production = 'health-insurance-app-ba5j.onrender.com'
host_production = 'health-insurance-app-ba5j.onrender.com'


// Api call function

function Api_call(data, endpoint){
  var url = 'https://' + host_production + endpoint
  var payload = JSON.stringify(data)
  
  var options = {'method': 'POST', 'contentType':'application/json', 'payload':payload};

  // request
  var response = UrlFetchApp.fetch(url,options);

  // get response
  var rc = response.getResponseCode();
  var responseText = response.getContentText();

  
  if (rc !== 200){
    Logger.log('Response (%s) %s', rc, responseText);    
  }
  else{
    prediction = JSON.parse(responseText);

    return prediction
  }

  return None

}




// 'Predict all' function

function Predict_all(){
  var ss = SpreadsheetApp.getActiveSpreadsheet(); // getting acess to current active spreadsheet
  var last_column = ss.getLastColumn(); // geting the last column of the spreadsheet
  var column_title = ss.getRange('A1:K'+ last_column).getValues()[0]; // colecting spreadsheet headers and putting them in a list
  var last_row = ss.getLastRow(); // geting the last row of the spreadsheet

  var data = ss.getRange('A2'+ ':' + 'K' + last_row).getValues(); // range of values to iter

  // initialize an empty array
  var json_send_final = []

  

  // iter over all rows
  for (row in data){
    var json_row = new Object();

    // iter over all columns
    for(var j=0; j <column_title.length; j++){
      json_row[column_title[j]] = data[row][j];
    };


    // Setting json to send
    var json_to_send = new Object();
    json_to_send['id'] = json_row['id']
    json_to_send['Gender'] = json_row['Gender']
    json_to_send['Age'] = json_row['Age']
    json_to_send['Driving_License'] = json_row['Driving_License']
    json_to_send['Region_Code'] = json_row['Region_Code']
    json_to_send['Previously_Insured'] = json_row['Previously_Insured']
    json_to_send['Vehicle_Age'] = json_row['Vehicle_Age']
    json_to_send['Vehicle_Damage'] = json_row['Vehicle_Damage']
    json_to_send['Annual_Premium'] = json_row['Annual_Premium']
    json_to_send['Policy_Sales_Channel'] = json_row['Policy_Sales_Channel']
    json_to_send['Vintage'] = json_row['Vintage']


    // append multiple values to the array
    json_send_final.push(json_to_send);


  }





// Making API request to get predictions
pred = Api_call(json_send_final, '/healthinsurance/predict')


// Sending data back to Google Sheets

// For loop to iter through the json returned by API request to retrieve Rank information for each row
row_number = 2
for (var i=0; i < pred.length; i++) {
  
   Logger.log(pred[i]['Rank'])
   var actual_pred = pred[i]['Rank']
   // Sending data back to Google Sheets
   ss.getRange('L'+row_number).setValue(actual_pred)
   row_number++   

}

  
} 


