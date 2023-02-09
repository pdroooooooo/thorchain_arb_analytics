# import os
import pdb
import pandas as pd
# import mysql.connector
# from dotenv import load_dotenv, find_dotenv

columns = ["date", "time", "level", "dex", "pool_asset", "cex", "cex_asset", "price_diff", "dex_price", "cex_price"]
df = pd.DataFrame(columns=columns)

# Constructs or re-builds a DF from the to_db.log file (i.e. raw data)
def build_table(file_loc = "../../data/to_db.log"):
    with open(file_loc, 'r') as log:
        lines = log.readlines()
    for line in lines:
        line = line.strip()
        date, time, _, level, _, dex, pool_asset, _, cex, cex_asset, _, price_diff, _, dex_price, cex_price, _ = line.split(" ")
        lista = [date, time, level, dex, pool_asset, cex, cex_asset, price_diff, dex_price, cex_price]
        df.loc[len(df)] = lista
    return df

# Export DF to MYSQL # Not used anymore
# def export_table():
#     load_dotenv(find_dotenv())
#     db = mysql.connector.connect(
#             host="127.0.0.1",
#             user=os.getenv("MYSQL_USER"),
#             password = os.getenv("MYSQL_PWD")
#             )

#     cursor = db.cursor(buffered=True)
#     cursor.execute("SHOW DATABASES")



if __name__ == "__main__":
    pdb.set_trace()