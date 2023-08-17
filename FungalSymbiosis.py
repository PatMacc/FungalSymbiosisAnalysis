

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


funghi_db = pd.read_csv('analysis_final.csv')

        #Converting data to desired data types 

funghi_db['Harvest.date'] = pd.to_datetime(funghi_db['Harvest.date'])
funghi_db['Planted'] = pd.to_datetime(funghi_db['Planted'])
funghi_db['Number'] = funghi_db['Number'].astype(int)
funghi_db['Tree'] = funghi_db['Tree'].astype(str)


        #Brief EDA of a dataframe structure: column names, null values counts, data types etc.

print(funghi_db.head())
print(funghi_db.info())
print(funghi_db.describe())
print(funghi_db.isna())

sns.histplot(x= "Days in Experiment", data = funghi_db)
plt.show()
sns.histplot(x='Replicate', data = funghi_db)
sns.boxplot(x='Replicate', data = funghi_db)
                #Based on previous plots I've decided to check data for the outlier in a Replicate category

outlier = funghi_db[funghi_db['Replicate'] > 100] 
print(outlier)    #next, I wanted to investigate if high Replicate number is associated with Days in Experiment Number

print(funghi_db['Days in Experiment'].max()) #The highest Days in Experiment value is 202 and Replicate number is 10
print(funghi_db[funghi_db['Days in Experiment'] == 202])

#sns.barplot(x = 'Light', y = 'fungalmass_ug', data = funghi_db, hue = 'Fungi')




funghi_db['Days_Recoded'] = funghi_db['Days in Experiment']

intervals = [
    funghi_db['Days_Recoded'] < 100,
    (funghi_db['Days_Recoded'] >= 120) & (funghi_db['Days_Recoded'] <=150),
    funghi_db['Days_Recoded'] > 180
]
category_names = ['short', 'medium', 'long']
categories = np.select(intervals, category_names, default = 'unknown')

funghi_db['Days_Recoded'] = categories

sns.barplot(x = 'Days_Recoded', y = 'fungalmass_ug', hue = 'Fungi', data = funghi_db)
plt.show()

#Light Intensity and Fungal Growth: Hypothesis: Increased light intensity positively correlates with enhanced fungal growth in ectomycorrhizal symbiosis. This could be due to the potential for increased photosynthesis and subsequent nutrient exchange between the fungus and host plant.
#print(funghi_db['Light'].value_counts())


#Optimal Light Conditions for Symbiotic Benefits: Hypothesis: There exists an optimal range of light conditions that maximizes the benefits of ectomycorrhizal symbiosis in terms of nutrient uptake, growth promotion, and stress resistance for both partners.

#Shade-Tolerant vs. Light-Dependent Species: Hypothesis: Different species of ectomycorrhizal fungi exhibit varying responses to light conditions, with shade-tolerant species thriving under low light and light-dependent species flourishing under high light.
#print(type(funghi_db))


