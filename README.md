# A/B Testing: Two-Sample t-Test:

![Ekran görüntüsü 2022-11-17 014844](https://user-images.githubusercontent.com/81737980/202545951-c01bc7c1-f637-4153-85f3-a2e7ecdd8d56.jpg)


Two-Sample t-test is used when it is desired to make a comparison between the mean of two groups. A/B Testing should always be based on a hypothesis. When selecting a problem, it is important to prioritize the problems and possible ideas of the service (product) to be tested.

While you are establishing the hypotheses, it will be very helpful if you follow these steps:

    1 - Set up hypotheses

    2 - Check assumptions

      2.1 - Normality Assumption
  
      2.2 - Variance homogenity
  
    3 - Carry out hypotheses

      3.1 - if the assumptions are verified, two sample t-test (parametric test)
  
      3.2 - if the assumptions are not verified, mannwhitneyu test, (non-parametric test)

    4 - Comment on results based o p-value

#### You can reach the detailed explanation of the project from the link below:
    https://medium.com/@zbeyza/a-b-testing-c2bdb065fb39

# About Data Set:
Facebook recently introduced a new bid type “Average Bidding” as an alternative to the current bidding called “Maximum Bidding. One of our customers, xxx.com, has decided to test this new feature and wants to do an A/B test to see if average bidding converts more than maximum bidding. A/B testing has been going on for 1 month and xxx.com is now waiting for you to analyze the results of this A/B test. The ultimate measure of success for xxx.com is Purchase. Therefore, the focus should be on the Purchase metric for statistical testing. There are two separate data sets, the control and test groups. Maximum Bidding was applied to the control group and Average Bidding was applied to the test group.

# Varibales:
- Impression: ad views
- Click: number of clicks on the ad viewed
- Purchase: the number of products purchased after the ads clicked
- Earning: Profit after the purchased products
