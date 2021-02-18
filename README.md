# Climate Prop
![header](https://wp-krypton.s3.amazonaws.com/wp-content/uploads/sites/3/2019/11/climate-change-tree.jpg)

# Overview
Twitter: not the final frontier, but one of the loudest frontiers. Twitter is a platform that allows users to share thoughts, ideas, resources, and news. With over 300 million active users, and billions of queries per day, Twitter is a trove of usable, immediate, actionable data on what people feel strongly about. This project seeks to leverage available data to understand the public conversation on climate change. 

# Task Definition
As an environmental advocacy group, having real time information on what people are saying about the climate crisis can be an invaluable tool in making the case to lawmakers, corporations, and, individuals that the will of the people is to take action on climate change. Having a pipeline that can gather tweets on climate change, classify them as believer or denier, then run sentiment analysis on the various groups can empower an organization with this immediate data. 

# Data
For this project data was classified by training a portion of the GW Libraries' "Climate Change Tweets Ids" dataset, which gives the Twitter Ids of nearly 40 million tweets on climate change. The dataset was hydrated using Twarc and the Twitter Developer APIs, split into manageable file sizes then imported in a `for` loop and reconcatenated using the Pandas package. Target variable was created by coercing embedded hashtag data from the API response. 

<img src="https://github.com/JoeBrowz/climate_prop/blob/main/images/wc_bel.jpg?raw=true" width="40%" class="center"> <img src="https://github.com/JoeBrowz/climate_prop/blob/main/images/wc_den.jpg?raw=true" width="40%" class="center">

Data was cleaned using Regular Expression and the nltk package, assisted by domain knowlege and findings from exploratory data analysis, stop words were determined, tweets were lemmatized, and prepped for modeling. 

<img src="https://github.com/JoeBrowz/climate_prop/blob/main/images/class.jpg?raw=true" width="30%">

# Model
Data was trained using several GridSearchCV models using TF-IDF Vectorization and Logistic Regression, Gradient Boosted Trees (based on LightGBM technique), and Random Forest Classifiers. Accuracy and F1 scores were both quite high on the training and testing data, meaning both precision and recall are high. When tested on a data from a different dataset, with target variables classified using a different method, the model performed acceptably, though it didn't predict negative cases very well.

![val_mat](/images/val_mat.jpg)

# Conclusion
Using TF-IDF has shortcomings that can't be fully dealt with using linear and ensemble modeling. The dramatic class imbalance fogs the ability to discern what is holding the model back: modeling techniques, the data itself, or the mathematical realities a class imbalance causes. However, putting aside the shortcomings, the model does have excellent metrics, achieving over 90% accuracy and F1 scoring on all of the best parameter models for each classifier type.
## Next Steps
A likely cure for the shortcomings of the modeling methods used thus far would be implementation of a recursive neural network built with transfer learning. Better handling class imbalance and allowing contextual memory would likely improve performance on the predicting minority class cases. Implementation of this in addition to feature engineering using other tweet metadata, utlizing a larger share of the dataset, more robust sentiment analysis, and importing and analyzing CO2 emissions data in relation to the climate conversation on twitter is all on the to-do list for this project's next steps.
## File Structure:
```
├── README.md                      <- the top-level README for reviewers of this project
├── data_wrangle.ipynb             <- data collection, organization and concatenating
├── EDA_notebook.ipynb             <- data cleaning, EDA, light visualization
├── modeling_notebook.ipynb        <- notebook containing all elements of model
├── data                           <- dataset files not hosted on github due to size constraints 
├── summary_presentation.pdf       <- a pdf of the project presentation
└── images                         <- generated from code for use in readme and presentation slides
```

## For Inquiries:
Joe Marx—jmarx@hash.fyi
- <a href='https://www.linkedin.com/in/joe-marx-260a64102/'>LinkedIn</a>


## Sources
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU

https://www.kaggle.com/edqian/twitter-climate-change-sentiment-dataset
