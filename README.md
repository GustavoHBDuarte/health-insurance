<h1><b><font color="#cc0000"><i>Ranking most promising customers for cross sell using Machine Learning</i></font></b></h1>





<h1>1- Overview, business context and challenges</h1>

<br>
<p><font size="3">Our fictious client is an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.</br>
    
An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.</br>

Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer.</br>

Building a model to rank interested customers in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue.</br> 

The Insurance company surveyed nearly 380,000 customers about their interest in joining a new Vehicle Insurance product last year. All customers showed interest or not in purchasing auto insurance and these responses were saved in a database along with other customer attributes.</br> 

The product team selected 127,000 new customers who did not respond to the survey to participate in a campaign, in which they will be offered the new auto insurance product. The offer will be made by the sales team through phone calls.

</br>



<p><font size="3"><b> The challenge:</b>The sales team has the capacity to make 20,000 calls within the campaign period. Therefore, the main goal of this project is to develop a machine learning model able to rank the most interested customers where the corresponding predictions can be acessed via API requests in Google Sheets.</font></p>

With this solution, the sales team hopes to be able to prioritize the people most interested in the new product and thus optimize the campaign by making contacts only with the customers most likely to make the purchase.


<p><font size="3">For the development of the solution, the following topics will guide us:</font></p>

</br>
<ol>
  <li><font size="3">Finding the main insights about customers interested in vehicle insurance.</font></li>
<br>
  <li><font size="3">What percentage of customers interested in purchasing vehicle insurance will the sales team be able to contact by making 20,000 calls?</font></li>
<br>
  <li><font size="3">What if the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing vehicle insurance will the sales team be able to contact?.</font></li>
<br>  
  <li><font size="3">How many calls does the sales team need to make to contact 80% of customers interested in purchasing vehicle insurance?</font></li>
</ol>
</br>


<p><font size="3"><b>Disclaimer:</b> The business context herein presented is fictitious and was used only for the purpose of the development of this project.</font></p>


<p><font size="3">Datasets used in this project can be downloaded <a href="https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction">here</a>.</font></p>





<h1>2- Assumptions</h1>

<br>
<p><font size="3">For the purpose of the development, model implementation and business we will be assuming the hiring client reaches out potential customers by making random calls.</font></p></br>






<h1>3- Data description</h1>

<br>
  <font size="3">Each row represents a customer and each column contains some attributes that describe that customer, in addition to the survey response, in which they mentioned interest or not in the new insurance product. The dataset used to build the solution has the following attributes:</font></li>
<br>
<br>
<ul>
  <li><font size="3"><b>id - </b>Unique ID for the customer.</font></li><br>
  <li><font size="3"><b>Gender - </b>Gender of the customer.</font></li><br>
  <li><font size="3"><b>Age - </b>Age of the customer.</font></li><br>
  <li><font size="3"><b>Driving_License - </b>0 : Customer does not have DL, 1 : Customer already has DL.</font></li><br>
  <li><font size="3"><b>Region_Code - </b>Unique code for the region of the customer.</font></li><br>
  <li><font size="3"><b>Previously_Insured - </b>1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance.</font></li><br>
  <li><font size="3"><b>Vehicle_Age - </b>Age of the Vehicle.</font></li><br>
  <li><font size="3"><b>Vehicle_Damage - </b>1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.</font></li><br>
  <li><font size="3"><b>Annual_Premium - </b>The amount customer needs to pay as premium in the year.</font></li><br>
  <li><font size="3"><b>PolicySalesChannel - </b>Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.</font></li><br>
    <li><font size="3"><b>Vintage - </b>Number of Days, Customer has been associated with the company.</font></li><br>
  <li><font size="3"><b>Response - </b>1 : Customer is interested, 0 : Customer is not interested.</font></li><br>
</ul>








<h1>4- Solution strategy</h1>

<br>
<ol>
  <li><font size="3"><b>Understanding the business and problems to be solved:</b> already described.</font></li>
<br>
  <li><font size="3"><b>Data colection:</b> downloading the corresponding .csv files from <a href="https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction">Kaggle</a> plattform or in our notebook's resoluting we will be colecting data via SQL queries.</font></li>
<br>
  <li><font size="3"><b>Data cleaning:</b> basic search for missing values, outliers and inconsistencies to make data suitable for further analysis. Adittionally a basic inspection including descriptive statistics (mean, standard deviation, range, skewness and kurtosis) should be also carried out.</font></li>
<br>
  <li><font size="3"><b>Feature engineering:</b> creating new features from the existing ones to assist in both exploratory data analysis (EDA) and machine learning modelling.</font></li>
<br>
  <li><font size="3"><b>Data filtering and selection:</b>  reducing the data based on business assumptions and constraints to make training set as close as possible to data in production.</font></li>
<br>
  <li><font size="3"><b>EDA:</b> exploring data to search for interesting insights and understand the impact of the features on the target variable (response).</font></li>
<br>
  <li><font size="3"><b>Data preparation:</b> splitting the data into train/test sets and applying them scaling, encoding and transformation methods to make data suitable to machine learning.</font></li>
<br>
  <li><font size="3"><b>Feature selection:</b> selecting the most relevant attributes based on EDA results and suitable algorithm to maximize machine learning performance.</font></li>
<br>
  <li><font size="3"><b>Machine learning:</b> evaluating different algorithms and compare their results based on cross-validation. For the sake of this step a good candidate algorithm should perform better than the random baseline estimator.</font></li>
<br>
  <li><font size="3"><b>Hiperparameter fine tuning:</b> randomly test different hyperparameter values in order to find some combination that improves model performance.</font></li>
<br>
  <li><font size="3"><b>Error interpretation:</b> after choosing the best performing model, in the next step model performance needs to be translated to business results.</font></li>
<br>
  <li><font size="3"><b>Model deployment:</b> deploying the machine learning model to cloud environment so predictions can be accessed via API requests in Google Sheets.</font></li>
<br>  
</ol>







<h1>5- Main insights</h1>

<br>
<p><font size="3">- People in the adult group had their vehicle damaged more often. 
    <br>Answer: <b>FALSE</b>. People in the middle age adult group had their vehicle damaged more often.</font></p>

<img src="https://drive.google.com/uc?export=view&id=1XOu2IgYemQ1KRf54It_EfETL9K5pKTlB" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />


<br>
    

<br>    
<br>
<p><font size="3">- People with newer vehicles (vehicle_age less than 1 Year) are more interested in purchasing vehicle insurance. 
    <br>Answer: <b>FALSE</b>. Most of interested people have their car aged between 1-2 year.</font></p>



<img src="https://drive.google.com/uc?export=view&id=1Li5FdwEFPoTE2xhbKTSdzGD_uFt8ytOg" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
    
    
    
<br>
<p><font size="3">- People who have had their vehicle damaged (vehicle_damage = Yes) are more interested in purchasing vehicle insurance. 
    <br>Answer: <b>TRUE</b>.  Most of interested people had their cars damaged before.</font></p>

<img src="https://drive.google.com/uc?export=view&id=1Y2YkSC56o3e8BC1842UvIKTuoliagOhv" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />


    
     
    
    
<br>    
<p><font size="3">Other hypothesis raised, as well as other insights can be checked out in the main notebook.</font></p>     
    
    
    
    
<h1>6- Machine Learning models</h1>

<br>
<p><font size="3">Models evaluated:</font></p>


<ul>
  <li><font size="3">Dummy Random model (baseline)</font></li>
  <li><font size="3">Logistic Regression</font></li>
  <li><font size="3">Balanced Random Forest</font></li>
  <li><font size="3">XGBoost</font></li>
  <li><font size="3">LightGBM</font></li>
  <li><font size="3">Extra Trees</font></li>    
</ul>






<h1>7- Machine Learning performance</h1>
    
    
<br>    
<table border="1">
   <thead>
   <tr>
       <th><font size="3">Model name</font></th>
       <th><font size="3">Precision at k CV</font></th>
       <th><font size="3">Recall at k CV</font></th>
   </tr>
   </thead>
   <tbody>
   <tr>
       <td><font size="3">Random classifier (baseline)</font></td>
       <td><font size="3">0.12 +/-0.01</font></td>
       <td><font size="3">0.04 +/-0.0</font></td>
   </tr>
   <tr>
       <td><font size="3">Logistic Regression</font></td>
       <td><font size="3">0.25 +/-0.13</font></td>
       <td><font size="3">0.08 +/-0.04</font></td>
   </tr>
          <tr>
       <td><font size="3">Random Forest</font></td>
       <td><font size="3">0.29 +/-0.12</font></td>
       <td><font size="3">0.09 +/-0.04</font></td>
   </tr>
          <tr>
       <td><font size="3">XGBoost</font></td>
       <td><font size="3">0.32 +/-0.12</font></td>
       <td><font size="3">0.1 +/-0.04</font></td>
   </tr>
          <tr>
       <td><font size="3">LightGBM</font></td>
       <td><font size="3">0.34 +/-0.11</font></td>
       <td><font size="3">0.11 +/-0.04</font></td>              
   <tr>
       <td><font size="3">Extra Trees</font></td>
       <td><font size="3">0.34 +/-0.1</font></td>
       <td><font size="3">0.11 +/-0.03</font></td>
</table>
    
    
    
<br>
<p><font size="3">K-fold (number of splits=10) cross-validation provided replicates that allowed standard deviation calculation of each metric evaluated (Precision at k, Recall at k). Metrics at k are more reliable to apply as metrics measurement for ranking problems because it tell us how good the model is in ranking customers.</font></p><br>

    
  
    
    

<br>
    
    
    
    

<h1>8- Hyperparameter fine tuning</h1>

<br>
<p><font size="3">Model hyperparameters were adjusted via random search fine tuning in order to improve model performance.The following table shows the metrics for the LightGBM tuned model:</font></p>
<br>

<table border="1">
   <thead>
   <tr>
       <th><font size="3">Model name</font></th>
       <th><font size="3">Precision at k CV</font></th>
   </thead>
   <tbody>
   <tr>
       <td><font size="3">LightGBM</font></td>
       <td><font size="3">0.428 +/-0.005</font></td>
   </tr>         
   </tbody>
</table>

<br>
<p><font size="3">As expected fine tuning did not improve significantly model's performance. The following Cumulative Gain curve show us the benefits of using LightGBM model compared to a random baseline model. Adittionally, lift curve show us how better the machine learning model is in ranking interested customers depending on the percentage of sample compared to baseline model.</font>    
<br>
    
    
    
<img src="https://drive.google.com/uc?export=view&id=1NHJ8D36Nqak4Dd3Y6T5SaDeNqLYYOrUh" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    
     
    
  
<img src="https://drive.google.com/uc?export=view&id=1AQ6Q2sr6vM8RbIMquF0lHc4sX2MiDxUD" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    
     
        


<h1>9- Answering business questions</h1>

    
<br>
<p><font size="3">Question 1: What percentage of customers interested in purchasing auto insurance will the sales team be able to reach by making 20,000 cals?</font></p>    



<p><font size="3">Answer: According to Cumulative Gains curve 20,000 calls corresponds to 16% of our customers base (125766 customers total). The curve shows us that is possible to reach 48% of interested customers (7,398 customers). Lift curve shows us that our machine learning model is almost 3 times better than a baseline/random model at reaching interested customers.</font></p>      
<br>    

    
<ul>
  <li><font size="3">Number of calls: 20000</font></li>
  <li><font size="3">Number of customers: 125766</font></li>
  <li><font size="3">Percentage of sample: 0.16</font></li>
  <li><font size="3">Percentage of interested customers reached: 0.48</font></li>
  <li><font size="3">Total of interested customers in the base: 15414</font></li>
  <li><font size="3">Total of interested customers reached by making 20000 calls: 7398</font></li>    
</ul>    
    
<br>

<img src="https://drive.google.com/uc?export=view&id=1lbC_QT9kc_z1K956j56abZgKn0ZoWFx5" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

    
<br>

<br>

<img src="https://drive.google.com/uc?export=view&id=1uuq--1grsmzj4rpdY5ZOnzulCyKpbm7a" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

    
<br>
<p><font size="3">Question 2: What if the sales team's capacity increases to 40,000 calls, wha percentage of customers interested in purchasing auto insurance will the sales team be able to contact?</font></p>    



<p><font size="3">Answer: According to Cumulative Gains curve 40,000 calls corresponds to 32% of our customers base (125766 customers total). The curve shows us that is possible to reach 82% of interested customers (12,647 customers). Lift curve shows us that our machine learning model is almost 2,7 times better than a baseline/random model at reaching interested customers.</font></p>      
<br>    

    
<ul>
  <li><font size="3">Number of calls: 40000</font></li>
  <li><font size="3">Number of customers: 125766</font></li>
  <li><font size="3">Percentage of sample: 0.32</font></li>
  <li><font size="3">Percentage of interested customers reached: 0.82</font></li>
  <li><font size="3">Total of interested customers in the base: 15414</font></li>
  <li><font size="3">Total of interested customers reached by making 40000 calls: 12647</font></li>    
</ul>    
    
<br>

<img src="https://drive.google.com/uc?export=view&id=12Th7dUcuXTnkp4orq55vynp4VkR29M6u" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

    
<br>

<br>

<img src="https://drive.google.com/uc?export=view&id=1gVUCjhyfZDS4atO2JWtT5QJtE3xszQ0S" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />    
    
    
    
<br>
<p><font size="3">Question 3: How many calls does the sales team need to make to reach 80% of the customers interested in purchasing auto insurance?</font></p>    



<p><font size="3">Answer: 38,480 calls.</font></p>      
<br>    

    
<ul>
  <li><font size="3">Number of calls: 38480</font></li>
  <li><font size="3">Number of customers: 125766</font></li>
  <li><font size="3">Percentage of sample: 0.31</font></li>
  <li><font size="3">Percentage of interested customers reached: 0.80</font></li>
  <li><font size="3">Total of interested customers in the base: 15414</font></li>
  <li><font size="3">Total of interested customers reached by making 38480 calls: 12332</font></li>    
</ul>    
    
<br>

<img src="https://drive.google.com/uc?export=view&id=1_rfH1ZuA-4qO22qXaTVbTL9HQ9SWwAVJ" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

    
<br>

<br>

<img src="https://drive.google.com/uc?export=view&id=1f_JykpyMOgCBo2J1R_3a_RS-IKG6dXob" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />        
    
    
    
<br>
    
    

<h1>10- Model deployment</h1>

<br>

<ul>
  <li><font size="3">Machine learning model was successfully deployed on Heroku cloud. Predictions can be acessed using the following endpoint: <a href="https://health-insurance-gustavo.herokuapp.com/healthinsurance/predict">https://health-insurance-gustavo.herokuapp.com/healthinsurance/predict</a>.</font>
      
<font size="3">In the following image it is possible to see that there is a Google Sheets spreadsheet with a newly created button called "Health Insurance". In this button the user can click on "get predictions" to obtain the probability of each customer to be interested in vehicle insurance (score).</font>
</ul>    
    
<br>

<img src="https://drive.google.com/uc?export=view&id=1-wT69zWEbvs5idXKg-_Qt-GVx-drgv7L" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />        
    
    
    
<br>
  
    
    
    
    

<h1>11- Conclusions</h1>

<br>
<p><font size="3">This project aimed to show that it is possible to, starting from a dataset containing information about customers that might be interested in a new product, train a estimator that is able to rank new customers more likely to be interested in this same product. This represents a valuable resource not only for marketing team, that can reach out customers more assertively compared to randomly call to customers, but also for the company as a whole due to increase of conversion rate since the more interested customers are being contacted. The availability of model predictions in Google Sheets spreadsheets makes is intended to work as a shortcut making the decision making step for non-technical people easier and faster. The integration between the solution building to the final product represents the power of Data Science techniques in solving real world problems.</font></p>
<br>

    
    

