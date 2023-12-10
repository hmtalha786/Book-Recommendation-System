# CUSTOMER SEGMENTATION

### USE CASE

##### Use Case Summary
- Objective Statement:
  * Get a business insight about how many products are sold every month.
  * Get a business insight into how many customers spend their money every month.
  * To reduce risk in deciding where, when, how, and to whom a product, service, or brand will be marketed.
  * To increase marketing efficiency by directing effort specifically toward the designated segment in a manner consistent with that segment’s characteristics.

- Challenges:
  * Large size of data, can not maintain my Excel spreadsheet.
  * Need several coordination from each department.
  * Demography data have a lot of missing values and typos.

- Methodology / Analytic Technique:
  * Descriptive analysis
  * Graph analysis
  * Segment Analysis

- Business Benefit:
  * Helping the Business Development Team to create product differentiation based on the characteristics of each customer.
  * Know how to treat customers with specific criteria.

- Expected Outcome:
  * Know how many products are sold every month.
  * Know how many customers spend their money every month.
  * Customer segmentation analysis.
  * Recommendation based on customer segmentation.
  
### BUSINESS UNDERSTANDING

- Retail is the process of selling consumer goods or services to customers through multiple channels of distribution to earn a profit.- This case has some business questions using the data:
- How many products sold every month?
- How many customers spend their money every month?
- How about Customer segmentation analysis?
- How about recommendations based on customer segmentation?

### DATA UNDERSTANDING

- Data of Retail Transaction from 01 December 2010 to 09 December 2011
- Source Data: Online retail dataset by UCI Machine Learning Library. 
https://archive.ics.uci.edu/ml/datasets/Online+Retail
- The dataset has 8 columns and 541909 rows.
- Data Dictionary:
- Invoice No: Invoice number uniquely assigned to each transaction. 
- StockCode: Product (item) code.
- Description: Product (item) name.
- Quantity: The quantities of each product (item) per transaction. 
- InvoiceDate: The day and time when each transaction was generated.
- UnitPrice: Product price per unit in sterling.
- CustomerID: Customer number uniquely assigned to each customer.
- Country: The name of the country where each customer resides.

### DATA PREPARATION 

- Code Used:
- Python Version: 3.7.6
- Packages: Pandas, Numpy, Matplotlib, Seaborn, Sklearn, and Feature Engine 

### DATA CLEANING 

- There are about 25% of Null CustomerID in the data. We need to remove them as there is no way we can get the number of CustomerID.
- There are few records with UnitPrice<0 and Quantity<0. We need to remove them from the analysis. This could represent cancelled or returned orders.
- There is more than 90% of 'United Kingdom' customers, therefore we will restrict the data to only United Kingdom customers.

### EXPLORATORY DATA ANALYSIS

- How many products sold every month ???
![count 1](https://user-images.githubusercontent.com/75175081/127734116-ed109eb3-686d-435d-96fd-d29255377ea6.png)
The product sold in November had the highest quantity that has around 13,41% of products sold from all transactions in 1 year. Therefore the business team can increase sales in this month such as promoting new products to customers in this month.

- How many customers spend their money every month ???
![revenue 1](https://user-images.githubusercontent.com/75175081/127734242-42991f19-1ef5-4af5-b623-fdaf7c6cc122.png)
Revenue in November has the highest amount has  13,41% revenue from total revenue over 1 year. Therefore the business team can replicate the success of sales strategies in November to be implemented in other months

### RFM ANALYSIS

- Recency Frequency Monetary (RFM)
- RFM analysis allows you to segment customers by the frequency and value of purchases and identify those customers who spend the most money.
- Recency — how long it’s been since a customer bought something from us.
- Frequency — how often a customer buys from us.
- Monetary value — the total value of purchases a customer has made.

### MODELING DATA : RFM QUANTILES

- Now we split the metrics into segments using quantiles.
- We will assign a score from 1 to 4 to each Recency, Frequency and Monetary respectively.
- 1 is the highest value, and 4 is the lowest value.
- A final RFM score (Overall Value) is calculated simply by combining individual RFM score numbers.

![image](https://user-images.githubusercontent.com/75175081/127734694-d312d392-7994-4f7d-adfe-e55d01fdc5f4.png)

![image](https://user-images.githubusercontent.com/75175081/127737315-58d588ee-371b-4a8b-8c9f-d2e4d696939f.png)

### MODELING DATA : K-MEANS CLUSTERING
- K-Means clustering algorithm is an unsupervised machine learning algorithm that uses multiple iterations to segment the unlabeled data points into K different clusters in a way such that each data point belongs to only a single group that has similar properties.
- K-means gives the best result under the following conditions:
- Data distribution is not skewed.
- Data is standardised.
- The data is highly skewed, therefore I will perform log transformations to reduce the skewness of each variable and I standardise the data.
- Finding the optimal number of clusters

![finding k](https://user-images.githubusercontent.com/75175081/127736473-c222dcb1-6bcb-4746-bb11-b38b37f49eba.png)

# EVALUATING MODEL : K-MEANS CLUSTERING

- Davies Bouldin Score is a metric for evaluating clustering algorithms. 
- The smaller the Davies Bouldin Score is The more optimal the cluster.
![image](https://user-images.githubusercontent.com/75175081/127736802-fd0e6465-1c20-4e8a-8a35-a3fc2f85280a.png)

K-Means 4 clusters have the lowest Davies Bouldin Score than other clusters. Therefore the optimum cluster is 4. 

### INTERPRETATION OF THE CLUSTERS FORMED USING K-MEANS

- "Cluster 0" has 29% customers. It belongs to the “Loyal Customer" segment as they Haven’t purchased for some time, but used to purchase frequently (F=2) and spent a lot. 
- "Cluster 1" has 20% customers. It can be interpreted as “Almost Lost". They purchased recently (R=2). However, they do not purchase frequently and do not spend a lot. 
- "Cluster 2“ has 30% customers. It can be interpreted as "Lost Cheap Customers". Their last purchase was long ago (R=4), purchased very few (F=4) and spent little (M=4).
- "Cluster 3“has 21% customers. It belongs to the "Best Customers" segment which we saw earlier as they purchase recently (R=1), are frequent buyers (F=1), and spend the most (M=1).
![kmeans 2](https://user-images.githubusercontent.com/75175081/127737861-0f62e50f-359b-4a74-9aa1-b59198d68570.png)

### RECOMMENDATION

- Recommendation for the “Best Customers" segment: Focus on increasing customer purchases therefore it is necessary to form a cross/Up Selling Strategy.
- Recommendation for the “Loyal Customers" segment: The business team must optimize the budget campaign and the time campaign for this customer segment to maintain their loyalty and increase their value.
- Recommendation for “Almost Lost" segment: This customer segment is very at risk for churn, so focus on activating customers and making repurchases by forming a Reactivation Strategy, Retention Strategy.
- Recommendation for “Lost Cheap Customers" segment: This customer segment has churned, so the focus of the campaign is to reactivate the customer by forming a Reactivation strategy.
