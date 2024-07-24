import pandas as pd
from salesdata.models import SalesData

data_file_path = './xpto_sales_products_mar_may_2024.csv - Página4.csv'
data_table = pd.read_csv(data_file_path, sep=',')

regs = data_table.to_dict('records')
print(data_table)
print(regs)
print(data_table.columns)
SalesData.objects.bulk_create(
    [SalesData(**r)for r in regs]
)
