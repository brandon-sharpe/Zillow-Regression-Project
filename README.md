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
        - creating a function for scaling my data (I use anything with a zscore less than 3 and throw out the rest. This keeps 97% of my data) 
        
***
## Data Exploration

**Goal**: Explore the data, come to a greater understanding for feature selection.

* Think about the following in this stage:

    - I've found that there is not enough data in fireplace or air conditioning to use them as features 

    - I like SQFT, Bathrooms, Bedrooms, Pool and year built as features. 

***
## Modeling

Goal: develop a regression model that performs better than a baseline.

2nd Degree polynomial was by far the best perfoming model. Given more time I would love to further feture engineer to make this a more reliable model.
   * RSME of 310069
   * $R^2$ of .36
   * Beats baseline RSME of 378,000
   
*** 
## Data Dictionary

| Feature           | Datatype                | Definition   |
|:------------------|:------------------------|:-------------|
| sqft              | 15189 non-null: int64   |Calculated Square footage of residence |
| bathrooms         | 15189 non-null: float64 |Number of bathrooms in residence   |
| bedrooms          | 15189 non-null: int64   |Number of Bedrooms in residence |
| has_pool          | 15189 non-null: int64   |Does the Residence have a pool: 0= no, 1=yes|
| tax_value         | 15189 non-null: int64   |The estimated value of the home|
| year_built        | 15189 non-null: float64 |The year the home was built |
| tax_amount        | 15189 non-null: float64 |The amount of taxes payed the previous year (2016) |
| fips              | 15189 non-null: object  |County code resident resides within: 6037 = LA, 6059 = Orange, 6111 = Ventura|
| county            | 15189 non-null: object  |County the resident resides|
| tax_rate          | 15189 non-null: float64 |The tax rate the resident was charged at|
| sqft_scaled       | 15189 non-null: float64 |sqft scaled using minmax scaler|
| bedrooms_scaled   | 15189 non-null: float64 |number of bedrooms scaled using minmax scaler |
| bathrooms_scaled  | 15189 non-null: float64 |number of bathrooms scaled using minmax scaler |
| year_built_scaled | 15189 non-null: float64 |year the house was built scaled using minmax scaler|

***
## Given more time 

I'd love to explore the effect of lat and lon on the Data
Eclore seperating the data set into larger and smaller priced houses and create a different model for each. 