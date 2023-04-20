import io
import pandas as pd
import requests


# 全都道府県の市区町村csvデータをDLして、一つのcsvに結合する
def create_geolocation_csv():
    # URL一覧
    urls = []

    # DLしてきたCSVのリスト
    data_list = []

    # 47都道府県のcsvデータのURLを生成してリストに追加
    for n in range(47):
        n = n + 1
        if n < 10:
            url = f'https://www.stat.go.jp/data/mesh/csv/0{n}.csv'
            urls.append(url)
        else:
            url = f'https://www.stat.go.jp/data/mesh/csv/{n}.csv'
            urls.append(url)

    # URLからデータをDLしてリストに追加
    for url in urls:
        print(url)
        res = requests.get(url)
        data_list.append(pd.read_csv(io.BytesIO(res.content), encoding="cp932", dtype=object))

    # 複数のリストを行方向に結合
    # 結合したcsvをカレントディレクトリに保存する
    df = pd.concat(data_list, axis=0, sort=True)
    df = df.drop('備考', axis=1)
    df = df.rename(columns={'都道府県市区町村コード': 'city_code', '市区町村名': 'city_name', '基準メッシュ・コード': 'mesh_code'})
    df.to_csv("./geolocation_data.csv", index=False, encoding="utf-8")


if __name__ == '__main__':
    print("--START--")
    try:
        create_geolocation_csv()
    except Exception as e:
        print(e)
    finally:
        print("--DONE--")
