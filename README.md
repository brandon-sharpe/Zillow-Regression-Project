# Zillow Regression Project
***

## Goals and objectives
    -
## Project Planning

**Goal**:-leave this section with (at least the outline of) a plan for the project documented in your README.md file.

* My initial thought process before anything:
   * *What features logically would drive the value of houses*
       - Size
       - Pool
       - location(well see about incorporating this)
       - fireplace
       - garage size(or if there is a garage)
* Ill scale my data **after** evaluation 
***
## Acquire & Prepare

**Goal**: leave this section with a dataframe ready to prepare.

* Create a wrangle.py file that holds everything inside the prepare and aqcuire stages
    * *This Includes*
        - Brining the data in from sql
        - Taking out null values
        - deciding the features i will bring foward based off the available data
        - Changing any values moving foward
        - making columns readable
        - spliting data into train test and validate
        - creating a function for scaling my data 
        
***
## Data Exploration

**Goal**: Explore the data, come to a greater understanding for feature selection.

* Think about the following in this stage:

    - Run at least 1 t-test and 1 correlation test (but as many as you need!)

    - Visualize all combinations of variables in some way(s).

    - What independent variables are correlated with the dependent?

    - Which independent variables are correlated with other independent variables?
***
## Modeling

Goal: develop a regression model that performs better than a baseline.

Think about the following in this stage:

Extablishing and evaluating a baseline model and showing how the model you end up with performs better.

Documenting various algorithms and/or hyperparameters you tried along with the evaluation code and results in your notebook before settling on the best algorithm.

Evaluating your model using the standard techniques: plotting the residuals, computing the evaluation metrics (SSE, RMSE, and/or MSE), comparing to baseline, plotting 
y
 by 
^
y
.

For some additional options see sklearn's linear models and sklearn's page on supervised learning.

After developing a baseline model, you could do some feature engineering and answer questions like:

Which features should be included in your model?

Are there new features you could create based on existing features that might be helpful?

Are there any features that aren't adding much value?

Here you could also use automated feature selection techniques to determine which features to put into your model.

You should make sure that any transformation that you apply to your training dataframe are reproducible, that is, the same transformations can be applied to your test dataset.