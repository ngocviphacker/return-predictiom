import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def run_apriori(df):
    from mlxtend.frequent_patterns import apriori, association_rules
    import pandas as pd

    # tạo basket
    basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)

    # chuyển về 0/1
    basket = basket.apply(lambda x: x > 0)

    # apriori
    frequent = apriori(basket, min_support=0.02, use_colnames=True)

    rules = association_rules(frequent, metric="lift", min_threshold=1)

    print(rules.head())

    return rules  