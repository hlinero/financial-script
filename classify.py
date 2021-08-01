from Column import Column

def classify(df, transactions_names_to_ignore, transaction_positions_to_ignore):
    __assign_usage_classification(df, transactions_names_to_ignore, transaction_positions_to_ignore)
    __assign_date_classification(df)

def __assign_usage_classification(df, transactions_names_to_ignore, transaction_positions_to_ignore):
    usage_column = []

    for index, row in df.iterrows():
        result = row[Column.NAME.value] not in transactions_names_to_ignore and index not in transaction_positions_to_ignore
        usage_column.append(result)

    assert len(usage_column) == len(df)

    df.insert(0, Column.USAGE.value,  usage_column)

def __assign_date_classification(df):
    group_column = []

    for index, row in df.iterrows():
        date = row[Column.DATE.value]
        group = __generate_group(date)
        
        group_column.append(group)

    assert len(group_column) == len(df)

    df.insert(0, Column.GROUP.value,  group_column)

def __generate_group(date):
    date_by_parts = date.split("-")
    
    # Groups are in the format YYYY-MM
    return "{}-{}".format(date_by_parts[0], date_by_parts[1]) 