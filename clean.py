from dateutil import parser
from Column import Column

def clean(df, date_column_name, amount_column_name, transaction_name_column):
    df.drop(columns=['index',], inplace = True)

    __set_amount_column_name(df, amount_column_name)
    __set_date_column_name(df, date_column_name)
    __set_transaction_name_column_name(df, transaction_name_column)

    __format_date(df)
    __format_amount(df)

def __set_amount_column_name(df, amount_column_name):
    df.rename(columns = {amount_column_name: Column.AMOUNT.value}, inplace = True)

def __set_date_column_name(df, date_column_name):
    df.rename(columns = {date_column_name: Column.DATE.value}, inplace = True)

def __set_transaction_name_column_name(df, transaction_name_column):
    df.rename(columns = {transaction_name_column: Column.NAME.value}, inplace = True)

def __format_date(df):
    format = "%Y-%m-%d"
    new_date_column = []
    
    for index, row in df.iterrows():
        original_date = parser.parse(row[Column.DATE.value])
        new_date_column.append(original_date.strftime(format))
    
    df.drop(columns=[Column.DATE.value], inplace = True)

    assert len(new_date_column) == len(df)
    df.insert(0, Column.DATE.value,  new_date_column)
            
def __format_amount(df):
    new_amount_column = []

    for index, row in df.iterrows():
        new_amount_column.append(float(row[Column.AMOUNT.value].replace(",", "").replace(" ", "")))

    df.drop(columns=[Column.AMOUNT.value], inplace = True)

    assert len(new_amount_column) == len(df)
    df.insert(0, Column.AMOUNT.value,  new_amount_column)
    