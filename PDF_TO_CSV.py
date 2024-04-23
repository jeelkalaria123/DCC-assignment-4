import fitz
import csv
import pandas as pd
def pdf_to_csv(pdf_file, csv_file):
  document = fitz.open(pdf_file)
  data=[]
  for pg in document:
    Table=pg.find_tables()
    if Table.tables:
      TABLES=Table[0].extract()
    data.extend(TABLES[1:])
  heading = [i.replace('\n',' ') for i in TABLES [0]]
  ds=pd.DataFrame (data, column=heading)
  ds ["Denominations"]=ds["Denominations"].apply(lambda x:x.replace(",",""))
  ds.to_csv(csv_file,index=False)
pdf_to_csv(r"C:\Users\jeelk\Downloads\TABLE 1.pdf", r'EB_Redemption_Details.csv')
pdf_to_csv(r"C:\Users\jeelk\Downloads\TABLE 2.pdf", r'EB_Purchase_Details.csv')