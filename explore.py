import pandas as pd
import numpy as np
import wrangle
import sklearn.preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

import warnings
warnings.filterwarnings("ignore")

def tax_distro(df):
    '''This will graph the tax distubution between counties '''
    plt.figure(figsize=(14,10))
    sns.histplot(data=(df), x='tax_rate', hue='county', bins = 1000)
    plt.xlim(0.75, 3)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.xlabel('Tax Rate Percentage', fontsize = 15)
    plt.ylabel('Frequency', fontsize = 15)
    plt.title('Distributions of Tax Rates by County', x = .24, fontsize = 20)

def distrubutions(train):
    '''checking distributions of our selected features/univariate exploration'''
    for x in train[['bedrooms','bathrooms','sqft','tax_value','has_pool','county', 'year_built']]:
        sns.histplot(train[x], bins = 20, kde = True)
        plt.title(f'Distribution of {x}')
        plt.tight_layout()
        plt.show()

def corr_heatmap(train): 
# Make a heatmap that shows correlation of churn and other variables
    plt.figure(figsize=(8, 12))
    heatmap = sns.heatmap(train.drop(columns=[
                                              'tax_rate']).corr()[['tax_value']].sort_values(by='tax_value',
                                                                                                          ascending=False), vmin=-1, vmax=1, annot=True, cmap='BrBG')
    heatmap.set_title('Features Correlating with Tax Value', fontdict={'fontsize':18}, pad=16);


        
def add_scaled_columns(train, validate, test, scaler, columns_to_scale):
    '''Takes in df and scales the columns inputed and concats them to the dataframe '''    
    # new column names
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    
    # Fit the scaler on the train
    scaler.fit(train[columns_to_scale])
    
    # transform train validate and test
    train = pd.concat([
        train,
        pd.DataFrame(scaler.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    
    
    test = pd.concat([
        test,
        pd.DataFrame(scaler.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    
    return train, validate, test

def lets_explore(train):
    distrubutions(train)
    corr_heatmap(train)
    
def scat_plot(df,x,y):
    plt.figure(figsize = (12,10))
    sns.lmplot(x = (x), y=(y), data = df,line_kws={'color': 'red'})
    plt.title(f'Relationship between {x} and {y}', loc = 'left')
    plt.tight_layout()
    plt.ticklabel_format(style='plain')
    plt.show()
    
def make_metric_df(y, y_pred, model_name, metric_df):
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
                'model': model_name, 
                'RMSE_validate': round(mean_squared_error(
                    y,
                    y_pred) ** .5),
                'r^2_validate': explained_variance_score(
                    y,
                    y_pred)
            }])
        return metric_df
    else:
        return metric_df.append(
            {
                'model': model_name, 
                'RMSE_validate': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_validate': explained_variance_score(
                    y,
                    y_pred)
            }, ignore_index=True)