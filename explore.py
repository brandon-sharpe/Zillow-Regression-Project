import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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