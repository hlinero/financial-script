import config
import file_handler
from import_transactions import import_transactions
from clean import clean
from classify import classify
from analysis import calculate_expenses
from export import print_results

def exec():
    if not file_handler.is_config_file_present():
        print("'config.yaml' is not present")
        return

    files_with_transactions = config.files_with_transactions()
    for file_path in files_with_transactions:
        if not file_handler.is_file(file_path):
            print(f"The file '{file_path}' does not exist.")
            exit()

    data_df = import_transactions(files_with_transactions)

    date_column_name = config.date_column_name()
    amount_column_name = config.amount_column_name()
    transaction_column_name = config.transaction_name_column_name()
    clean(data_df, date_column_name, amount_column_name, transaction_column_name)

    transaction_name_to_ignore = config.transaction_names_to_ignore()
    transaction_positions_to_ignore = config.transaction_positions_to_ignore()
    classify(data_df, transaction_name_to_ignore, transaction_positions_to_ignore)

    expenses_per_month = calculate_expenses(data_df)

    export_config = config.export_configurations()
    print_results(data_df, expenses_per_month, export_config)

if __name__ == '__main__':
    exec()