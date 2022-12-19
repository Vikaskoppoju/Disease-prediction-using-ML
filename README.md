# Disease_prediction-using-ML 
A more accurate diagnosis than the traditional method can be achieved by creating a medical diagnosis system based on the Random Forest machine learning algorithm for disease prediction. By creating a classification system with the help of the machine learning algorithm Random Forest, doctors would be far more able to anticipate and identify diseases at an early stage, greatly facilitating the resolution of health-related concerns. The primary objective of our project is to identify the disease term using the user's or patient's symptom data. This project suggests an automated disease prediction system that depends on user input to reduce the time and cost necessary for the first phase of diagnosing symptoms. After receiving user input, the system generates a list of likely ailments
## PROPOSED SYSTEM 
By using the user's symptoms, the model (GUI) forecasts the disease he is likely to have. The interface answers right away and accurately and quickly. 
- The user must enter information like his name. 
- The user must enter at least 2 symptoms that they are now experiencing. 
## RANDOM FOREST ALGORITHM 
Popular machine learning algorithm Random Forest is a part of the supervised learning methodology. It can be applied to ML issues involving both classification 
and regression. It is built on the idea of ensemble learning, which is a method of integrating various classifiers to address difficult issues and enhance model performance. Random Forest, as the name implies, is a classifier that uses a number of decision trees on different subsets of the provided dataset and averages them to 
increase the dataset's predictive accuracy. As opposed to depending on a single decision tree, the random forest uses forecasts from all of the trees to predict the 
ultimate result based on the votes of the majority of predictions. An increase in accuracy and a solution to the overfitting issue are provided by the larger number of 
trees in the forest. 
* First, a random sample of n records from a data collection with k records is selected for the Random Forest model. Each sample's own decision tree is built in 
second step. The third step is when each decision tree produces an output. 
* The final output is evaluated based on the majority vote or the average for classification and regression, respectively. 
## DESIGN AND WORK FLOW: 
![WhatsApp Image 2022-12-19 at 13 52 57](https://user-images.githubusercontent.com/98159254/208402269-6b160c88-1160-4126-9bb2-112ae841f7d5.jpg)
## Software Requirements
- python-above 3
#### Packages
You can download all required packages by executing the below commands in manage.py location in project
* pip install -r req.txt
> The above command recursively download all required packages to your system.
## FrontEnd Design:
#### Home Page
![image](https://user-images.githubusercontent.com/98159254/208404321-aea44def-0a10-4a21-b54e-ad9c103e270d.png)
#### This page takes Inputs from user
![image](https://user-images.githubusercontent.com/98159254/208404391-1b9e6bdd-a878-4287-855d-135692f48e6f.png)
#### Result Page
![image](https://user-images.githubusercontent.com/98159254/208404525-7a8b7d86-bcf5-4c63-95a1-c20341468038.png)
#### The User can  download the result as PDF format
![image](https://user-images.githubusercontent.com/98159254/208404704-1c80d34e-0982-4c94-9fb8-6856c1a29185.png)
