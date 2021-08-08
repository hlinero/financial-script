from Column import Column

def print_results(df, expenses_per_month, export_configs):
    for expense in expenses_per_month:
        month = list(expense.keys())[0]
        print(expense)

        df_for_month = df[df[Column.GROUP.value] == month]

        if __display_calculation_columns_only(export_configs):
            df_for_month = df_for_month.drop(__columns_to_drop(df_for_month), axis=1)

        sorted_df = df_for_month.sort_values(by=[Column.USAGE.value, Column.DATE.value])
        
        if __display_transactions(export_configs):
            print(sorted_df.to_markdown())

        if __export_to_csv(export_configs):
            sorted_df.to_csv("export_result.csv", index=False)

        print("=============")
        print("=============")

def __display_calculation_columns_only(export_configs):
    return export_configs["display_calculation_columns_only"]

def __columns_to_drop(df):
    columns_to_preserve = [e.value for e in Column]
    
    all_df_columns = list(df.columns)
    return [column_name for column_name in all_df_columns if column_name not in columns_to_preserve]

def __display_transactions(export_configs):
    return export_configs["display_transactions"]

def __export_to_csv(export_configs):
    return export_configs["export_to_file"]