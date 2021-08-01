# How to Run

## 1. Create a `config.yaml` file
The file must look as follows

```yaml
export:
  display_transactions: True
  display_calculation_columns_only: True
  export_to_file: False

files_with_transactions:
  - "october.csv"
  - "december.csv"

column_names:
  amount_column: NAME OF AMOUNT COLUMN
  date_column: NAME OF DATE COLUMNS
  transaction_name_column: TRANSACTION NAME COLUMN

transaction_names_to_ignore:
  - Example Transaction name 1
  - Example Transaction name 2

transaction_positions_to_ignore: [ ]
```

- `files_with_transactions`: Provide one or more `CSV` files with the transactions you want to analyse.

- `amount_column`: Specify the name of the column in your `CSV` file that has the transaction amounts.

- `date_column`: Specify the name of the column in your `CSV` file that has the date of the transactions.

- `transaction_name_column`: Specify the name of the column in your `csv` file that has the description or name of each transaction.

- `transaction_names_to_ignore`: The transactions with the names specified here will be ignored from the calculation.

- `transaction_positions_to_ignore`: The transactions with the positions specified here will be ignored from the calculation. Values must be separated by commas.

## 2. Download Dependencies
Run the command `pip install -r requirements.txt` to download all necessary dependencies

## 3. Run the code
Open a terminal window and run the command `python main.py`. The results will appear in the window as follows:

![Screenshoot](/screenshot.png)

# Interpreting Output
- The first column is the position of the transactions, if you wish to ignore a transaction based on position, put the position you want to ignore under the property `transaction_positions_to_ignore` from the `config.yaml` file.

- The column `GROUP` demonstrates a shorter  version of the date which only contains the year and month.

- The column `USE IN ANALYSIS` column shows if the transaction was used in the calculation or not.

- The value `{'2018-02' : 9213.0}` indicates the result for the month. A negative result indicates the amount of money spent, while a positive result indicates the amount of money earned.

- If you wish to only see the result for the month without showing the transactions, then change the property `display_transactions` to `False` in the `config.yaml` file.

- If you wish to see all the columns from your CSV file and not only the simplified version, as shown in the picture, change the property `display_calculation_columns_only` to `False`.