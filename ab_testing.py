#############################
# imports and display settings
#############################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 10)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

#############################
# Data Preparation & Analysis
#############################

# uploading dataset
df = pd.read_excel("datasets/ab_testing.xlsx", sheet_name=["Control Group", "Test Group"])

df_control = df["Control Group"]
df_test = df["Test Group"]

# analysis of control_group data
df_control.head()
df_control.describe().T
df_control.isnull().sum()
df_control.shape
df_control.info()

# analysis of test_group
df_test.head()
df_test.describe().T
df_test.isnull().sum()
df_test.shape
df_test.info()

# Concat control and test group datasets
df_control["group"] = "control"
df_test["group"] = "test"
df_ab = pd.concat([df_control, df_test], ignore_index=True)
df_ab.head()
df_ab.shape


#######################
# A/B Testing
#######################
"""
AB Testing Hypothesis:

- H0 : M1 = M2
    H0 claims that there is no statistically significant difference between purchase averages.

- H1 : M1 != M2
    H1 claims that there is statistically significant difference between purchase averages.

"""

# average purchase for control and test groups
df_ab.groupby("group").agg({"Purchase": "mean"})

"""
Normality Assumption
- H0 : M1 = M2
    H0 claims that the assumption of normal distribuion is verified.

- H1 : M1 != M2
    H1 claims that the assumption of normal distribution is not verified.

* p-value < 0.05 : H0 is rejected.
* p-value > 0.05 : H0 cannot be rejected.
"""

# normality assumption for control group
test_stat, pvalue = shapiro(df_ab.loc[df_ab["group"] == "control", "Purchase"])
print("test stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

# p-value = 0.5891
# p-value > 0.05 : H0 cannot be rejected
# assumption of normal distribution is verified

# normality assumption for control group
test_stat, pvalue = shapiro(df_ab.loc[df_ab["group"] == "test", "Purchase"])
print("test stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

# p-value = 0.1541
# p-value > 0.05 : H0 cannot be rejected
# assumption of normal distribution is verified


"""
Homogeneity of Variance
- H0 : M1 = M2
    Variances are homogeneous.

- H1 : M1 != M2
    Variances are not homogeneous.

* p-value < 0.05 : H0 is rejected
* p-value > 0.05 : H0 cannot be rejected.
"""

# homogeneity of variance
test_stat, pvalue = levene(df_ab.loc[df_ab["group"] == "control", "Purchase"],
                           df_ab.loc[df_ab["group"] == "test", "Purchase"])
print("test stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

# p-value = 0.1083
# p-value > 0.05 : H0 cannot be rejected
# assumption of variance homogeneity is verified

"""
Implementation of Hypotheses
Two-sample t-test if assumptions are verified (parametric)
Mannwhitneyu test if assumptions are not verified (non-parametric)
Note: in this case assumptions are verified so two sample t-test will be used but i will also use 
mannwhitneyu to be an example.
"""

# assumptions are verified : t-test
test_stat, pvalue = ttest_ind(df_ab.loc[df_ab["group"] == "control", "Purchase"],
                              df_ab.loc[df_ab["group"] == "test", "Purchase"],
                              equal_var=True)
print("test stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

# p-value = 0.3493
# p-value > 0.05 : H0 cannot be rejected
# there is no statistically significant difference between purchase averages.


# EXTRA
# let's assume assumptions are not verified and use the Mannwhitneyu test to se how it is using
test_stat, pvalue = mannwhitneyu(df_ab.loc[df_ab["group"] == "control", "Purchase"],
                                 df_ab.loc[df_ab["group"] == "test", "Purchase"])
print("test stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
