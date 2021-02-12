# Climate Prop
![header](https://wp-krypton.s3.amazonaws.com/wp-content/uploads/sites/3/2019/11/climate-change-tree.jpg)

## Overview
Twitter: the final frontier. Spend a few hours reading the tweets of the people and you too may deny that human's are intelligent beings. For all it's mess, Twitter is a trove of usable, immediate, actionable data on what people feel strongly about. This project seeks to leverage available data to understand the public conversation on climate change.

## Business Problem
As an environmental advocacy group, having real time information on what people are saying about the climate crisis can be an invaluable tool in making the case to lawmakers, corporations, and, individuals that the will of the people is to take action on climate change. Having a pipeline that can gather tweets on climate change, classify them as believer or denier, then run sentiment analysis on the various groups can empower an organization with this immediate data. 

## Data
For this project data was classified by training a portion of the GW Libraries' "Climate Change Tweets Ids" dataset, which gives the Twitter Ids of nearly 40 million tweets on climate change. The dataset was hydrated using Twarc and the Twitter Developer APIs, split into manageable file sizes then imported in a `for` loop and reconcatenated using the Pandas package.

Tweets were parsed and cleaned...

## Model
Model was trained using a GridSearchCV pipeline using TF-IDF Vectorization and a Random Forest Classifier. Accuracy and F1 scores were both quite high on the training and testing data, meaning both precision and recall are high. When tested on a data from a different dataset, with target variables classified using a different method, the model performed acceptably, though it didn't predict negative cases very well.

![val_mat](/images/val_mat.jpg)

## Conclusion
This was aight but could be better
## Next Steps
Neural network and bring in emissions data
## File Structure:
```
├── README.md                      <- the top-level README for reviewers of this project
├── EDA_notebook.ipynb             <- data cleaning, EDA, feature engineering/selection
├── modeling_notebook.ipynb        <- notebook containing all elements of model
├── data                           <- dataset files
├── summary_presentation.pdf       <- a pdf of the project presentation
└── images                         <- both sourced externally and generated from code
```

## Questions:
Joe Marx—jmarx@hash.fyi
- <a href='https://www.linkedin.com/in/joe-marx-260a64102/'>Joseph Marx</a>


## Sources
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU
