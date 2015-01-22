##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.9                                  #
##############################################
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics as smgraphics
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np
from scipy import stats
import math

df = pd.read_csv("cleaned_data_population.csv")

#conver to log
df['policy_index'] = np.log1p(df['policy_index'])
df['persons_prosecuted'] = np.log1p(df['persons_prosecuted'])
df['child_victims'] = np.log1p(df['child_victims'])
df['gdp'] = np.log1p(df['gdp'])
df['females_education'] = np.log1p(df['females_education'])
df['life_expectancy'] = np.log1p(df['life_expectancy'])
df['unemployment'] = np.log1p(df['unemployment'])

#declare variable
y = df[['Adult_victims']]
x=  df[["life_expectancy","policy_index","females_education"]]
X = sm.add_constant(x)
x2=  df[["policy_index","females_education","life_expectancy","unemployment"]]
X2 = sm.add_constant(x2)


# Model preparation
w = len(df['country'])
mod_wls = sm.WLS(y, X2, weights=1./w)
res_wls = mod_wls.fit()
print(res_wls.summary())


#new dataset
df_new = pd.read_csv("new.csv")
df_new = df_new.replace(np.nan,0)
df_new.rename(columns={'persons prosecuted': 'persons_prosecuted', 
                   'policy index': 'policy_index',
                   'child victims':'child_victims',
                   'Adult victims':'Adult_victims',
                   'life expectancy':'life_expectancy',
                   '% females in primary education':'females_education'}, inplace=True)


#adding new data
sLength2 = len(df_new['country'])
df_new['unemployment'] = pd.Series(np.random.randn(sLength2), index=df_new.index)
x_new= df_new[["policy_index","females_education","life_expectancy","unemployment"]]
y_new = df_new[['Adult_victims']]
X_new = sm.add_constant(x_new)

#figure prep
plt.figure()
plt.xlabel('all predictors')
plt.ylabel('Adult_victim')

# 3-rd order polynomial with new data
plt.plot(X_new, res_wls.predict(X_new), 'ro', label='Poly n=3 $R^2$=%.2f' % res_wls.rsquared, 
         alpha=0.9)

#saving new predicted values to csv
df_new['Adult_victims']=res_wls.predict(X_new)
df_new['Adult_victims'] = df_new['Adult_victims'].astype(int)
df_new.to_csv('predicted_glm_2.csv')

plt.savefig('figure_9new.png')
plt.show()


