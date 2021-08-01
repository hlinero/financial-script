from Column import Column

def calculate_expenses(df):
    expenses_per_month = []

    group_by_month = df.groupby(df[Column.GROUP.value])

    for name, group in group_by_month:
        transactions_to_use_df = group[group[Column.USAGE.value] == True]
        expenses = sum(list(transactions_to_use_df[Column.AMOUNT.value]))

        monthly_stats = {}
        monthly_stats[name] = expenses
        expenses_per_month.append(monthly_stats)
        
    return expenses_per_month