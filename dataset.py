import random
import pandas as pd
from datetime import datetime, timedelta

# Function to generate random sales data
def generate_sales_data(num_rows=100):
    # Define possible values for each column
    regions = ['North', 'South', 'East', 'West']
    product_ids = [f'P{str(i).zfill(4)}' for i in range(1, 21)]  # 20 unique products

    # Start date for sales data generation
    start_date = datetime(2023, 1, 1)
    
    # Create an empty list to store the rows of the dataset
    data = []

    for _ in range(num_rows):
        # Randomly generate data for each column
        date = start_date + timedelta(days=random.randint(0, 365))  # Random date within 2023
        sales_amount = round(random.uniform(10, 500), 2)  # Random sales amount between 10 and 500
        units_sold = random.randint(1, 20)  # Random number of units sold (1 to 20)
        product_id = random.choice(product_ids)  # Random product ID from list
        region = random.choice(regions)  # Random region from list

        # Append the generated row to the data list
        data.append([date.strftime('%Y-%m-%d'), sales_amount, units_sold, product_id, region])
    
    return data

# Generate 100 rows of sales data
sales_data = generate_sales_data()

# Create a DataFrame using the generated data
df = pd.DataFrame(sales_data, columns=['Date', 'Sales_Amount', 'Units_Sold', 'Product_ID', 'Region'])

# Save the DataFrame to a CSV file
df.to_csv('sales_data.csv', index=False)

print("Sales data CSV file has been generated and saved as 'sales_data.csv'.")