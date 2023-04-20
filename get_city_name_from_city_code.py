import sys
import pandas as pd

# 市区町村コード
city_code = sys.argv[1]


def read_csv():
    df = pd.read_csv('geolocation_data.csv', encoding='utf-8', dtype=str)
    city_code = df.query("city_code == @city_code").head(1)['city_name'].iloc[-1]

    return city_code



if __name__ == '__main__':
    print("--START--")
    try:
        print(read_csv())
    except Exception as e:
        print(e)
    finally:
        print("--DONE--")
