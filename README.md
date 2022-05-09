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
  <li><font size="3">The reliability of the implemented machine learning model in classifying transactions as legitimate or fraudulent.</font></li>
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
