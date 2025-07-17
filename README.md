
# Customer Segmentation and Churn Analysis Assignment

## Problem Description

In this assignment, you will perform a basic customer segmentation using RFM (Recency, Frequency, Monetary) analysis and calculate churn rate. These are key metrics for understanding customer behavior and business health.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find two function definitions: `perform_rfm_analysis(df)` and `calculate_churn_rate(df)`.
3.  Your task is to implement these functions:
    *   `perform_rfm_analysis`: Calculate Recency, Frequency, and Monetary values for each customer in the input DataFrame `df`. Assume `df` has columns like 'CustomerID', 'OrderDate', and 'Sales'. Recency is days since last purchase, Frequency is total orders, Monetary is total sales.
    *   `calculate_churn_rate`: Calculate the churn rate from a DataFrame `df` that has a 'Churn' column (1 for churned, 0 for not churned).

## Further Exploration (Optional)

*   How can you segment customers into different RFM groups (e.g., 'Loyal Customers', 'At-Risk Customers')?
*   Explore other methods for churn prediction, such as using machine learning models.
*   How can you visualize the RFM segments?
