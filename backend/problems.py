"""
Pandas学習問題の定義
"""

PROBLEMS = [
    {
        'id': 1,
        'title': 'DataFrameの基本操作',
        'description': 'CSVファイルから読み込まれたDataFrame `df` の最初の5行を表示してください。',
        'hint': 'head()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# dfの最初の5行を表示\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: isinstance(x, __import__('pandas').DataFrame) and len(x) == 5
        }
    },
    {
        'id': 2,
        'title': '列の選択',
        'description': 'DataFrame `df` から "Product" 列を選択して、変数 `result` に代入してください。',
        'hint': 'df["列名"] または df.列名 で列を選択できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Product列を選択\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 3,
        'title': 'データのフィルタリング',
        'description': 'DataFrame `df` から Sales が 1000 以上の行だけを抽出して、変数 `result` に代入してください。',
        'hint': 'df[df["列名"] > 値] のように条件を指定します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesが1000以上の行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: isinstance(x, __import__('pandas').DataFrame) and all(x['Sales'] >= 1000)
        }
    },
    {
        'id': 4,
        'title': '集計関数の使用',
        'description': 'DataFrame `df` の Sales 列の平均値を計算して、変数 `result` に代入してください。',
        'hint': 'mean()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Sales列の平均値を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 5,
        'title': 'グループ化と集計',
        'description': 'DataFrame `df` を Product 列でグループ化し、各グループの Sales の合計を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とsum()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productでグループ化してSalesの合計を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 6,
        'title': '新しい列の追加',
        'description': 'DataFrame `df` に、Sales に1.1を掛けた値を持つ "Sales_with_tax" という新しい列を追加してください。結果を `result` に代入してください。',
        'hint': 'df["新しい列名"] = 計算式 で列を追加できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Sales_with_tax列を追加（Sales * 1.1）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Sales_with_tax' in x.columns
        }
    },
    {
        'id': 7,
        'title': 'ソート',
        'description': 'DataFrame `df` を Sales 列で降順にソートして、変数 `result` に代入してください。',
        'hint': 'sort_values()メソッドを使用します。ascending=Falseで降順になります。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesで降順ソート\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: list(x['Sales']) == sorted(x['Sales'], reverse=True)
        }
    },
    {
        'id': 8,
        'title': '欠損値の処理',
        'description': 'DataFrame `df` の欠損値（NaN）を 0 で埋めて、変数 `result` に代入してください。',
        'hint': 'fillna()メソッドを使用します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# 欠損値を0で埋める\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: not x.isnull().any().any()
        }
    },
    # 列の操作（基礎）
    {
        'id': 9,
        'title': '複数列の選択',
        'description': 'DataFrame `df` から "Product" と "Sales" 列を選択して、変数 `result` に代入してください。',
        'hint': 'df[["列名1", "列名2"]] の形式で複数列を選択できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductとSales列を選択\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: list(x.columns) == ['Product', 'Sales']
        }
    },
    {
        'id': 10,
        'title': '列の削除',
        'description': 'DataFrame `df` から "Quantity" 列を削除して、変数 `result` に代入してください。',
        'hint': 'drop()メソッドを使用します。axis=1を指定すると列を削除できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Quantity列を削除\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Quantity' not in x.columns
        }
    },
    {
        'id': 11,
        'title': '列名の変更',
        'description': 'DataFrame `df` の "Sales" 列の名前を "Revenue" に変更して、変数 `result` に代入してください。',
        'hint': 'rename()メソッドを使用します。columns={"旧名": "新名"}の形式で指定します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Sales列の名前をRevenueに変更\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Revenue' in x.columns and 'Sales' not in x.columns
        }
    },
    {
        'id': 12,
        'title': 'DataFrameの形状確認',
        'description': 'DataFrame `df` の行数と列数をタプルとして取得し、変数 `result` に代入してください。',
        'hint': 'shape属性を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# DataFrameの形状を取得\nresult = ',
        'validation': {
            'variable': 'result',
            'check_function': lambda x: isinstance(x, tuple) and len(x) == 2
        }
    },
    {
        'id': 13,
        'title': '末尾のデータ表示',
        'description': 'DataFrame `df` の最後の3行を表示して、変数 `result` に代入してください。',
        'hint': 'tail()メソッドに引数を指定します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# 最後の3行を表示\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: len(x) == 3
        }
    },
    # フィルタリング（中級）
    {
        'id': 14,
        'title': '複数条件のフィルタリング（AND）',
        'description': 'DataFrame `df` から Sales が 1000 以上で、かつ Region が "East" の行を抽出して、変数 `result` に代入してください。',
        'hint': '条件を&で結合します。各条件は()で囲む必要があります。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesが1000以上かつRegionがEastの行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Sales'] >= 1000) and all(x['Region'] == 'East')
        }
    },
    {
        'id': 15,
        'title': '複数条件のフィルタリング（OR）',
        'description': 'DataFrame `df` から Product が "Apple" または "Orange" の行を抽出して、変数 `result` に代入してください。',
        'hint': '条件を|で結合するか、isin()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductがAppleまたはOrangeの行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Product'].isin(['Apple', 'Orange']))
        }
    },
    {
        'id': 16,
        'title': '文字列を含む行の抽出',
        'description': 'DataFrame `df` から Region 列に "orth" が含まれる行を抽出して、変数 `result` に代入してください。',
        'hint': 'str.contains()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Regionに"orth"が含まれる行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Region'].str.contains('orth'))
        }
    },
    {
        'id': 17,
        'title': '範囲指定フィルタリング',
        'description': 'DataFrame `df` から Sales が 1000 以上 1500 以下の行を抽出して、変数 `result` に代入してください。',
        'hint': 'between()メソッドを使用するか、複数条件を&で結合します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesが1000以上1500以下の行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all((x['Sales'] >= 1000) & (x['Sales'] <= 1500))
        }
    },
    {
        'id': 18,
        'title': '最大値を持つ行の抽出',
        'description': 'DataFrame `df` から Sales が最大の行を抽出して、変数 `result` に代入してください。',
        'hint': 'idxmax()メソッドで最大値のインデックスを取得し、loc[]で行を抽出します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesが最大の行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'check_function': lambda x: isinstance(x, __import__('pandas').Series) or isinstance(x, __import__('pandas').DataFrame)
        }
    },
    # 集計（中級）
    {
        'id': 19,
        'title': '複数列の集計',
        'description': 'DataFrame `df` の Sales 列と Quantity 列の合計をそれぞれ計算して、変数 `result` に代入してください。',
        'hint': 'sum()メソッドを複数列に対して適用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# SalesとQuantityの合計を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 20,
        'title': '中央値の計算',
        'description': 'DataFrame `df` の Sales 列の中央値を計算して、変数 `result` に代入してください。',
        'hint': 'median()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Sales列の中央値を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 21,
        'title': '標準偏差の計算',
        'description': 'DataFrame `df` の Sales 列の標準偏差を計算して、変数 `result` に代入してください。',
        'hint': 'std()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Sales列の標準偏差を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 22,
        'title': 'ユニーク値の取得',
        'description': 'DataFrame `df` の Product 列のユニークな値を取得して、変数 `result` に代入してください。',
        'hint': 'unique()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Product列のユニーク値を取得\nresult = ',
        'validation': {
            'variable': 'result',
            'check_function': lambda x: len(x) == 3 and 'Apple' in x
        }
    },
    {
        'id': 23,
        'title': '値のカウント',
        'description': 'DataFrame `df` の Region 列の各値の出現回数をカウントして、変数 `result` に代入してください。',
        'hint': 'value_counts()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Region列の値をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    # グループ化（中級）
    {
        'id': 24,
        'title': 'グループごとの平均',
        'description': 'DataFrame `df` を Product 列でグループ化し、各グループの Sales の平均を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmean()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの平均Salesを計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 25,
        'title': 'グループごとの最大値',
        'description': 'DataFrame `df` を Region 列でグループ化し、各グループの Sales の最大値を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmax()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Regionごとの最大Salesを計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 26,
        'title': 'グループごとのカウント',
        'description': 'DataFrame `df` を Product 列でグループ化し、各グループの行数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とcount()またはsize()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの行数をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 27,
        'title': '複数列でのグループ化',
        'description': 'DataFrame `df` を Product と Region 列でグループ化し、各グループの Sales の合計を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()に列名のリストを渡します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductとRegionでグループ化してSalesの合計を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 28,
        'title': '集約関数の適用',
        'description': 'DataFrame `df` を Product 列でグループ化し、Sales の合計と平均を同時に計算して、変数 `result` に代入してください。',
        'hint': 'agg()メソッドに関数のリストを渡します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの合計と平均を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    # データ変換
    {
        'id': 29,
        'title': '列の演算',
        'description': 'DataFrame `df` に、Sales を Quantity で割った値を持つ "UnitPrice" という新しい列を追加してください。結果を `result` に代入してください。',
        'hint': 'df["新列名"] = df["列1"] / df["列2"] の形式で計算できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# UnitPrice列を追加（Sales / Quantity）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'UnitPrice' in x.columns
        }
    },
    {
        'id': 30,
        'title': 'apply関数の使用',
        'description': 'DataFrame `df` の Sales 列の各値を2倍にして、新しい列 "DoubleSales" として追加してください。結果を `result` に代入してください。',
        'hint': 'apply()メソッドやラムダ関数を使用するか、単純に*2でも可能です。',
        'dataset': 'sales_data.csv',
        'initial_code': '# DoubleSales列を追加（Sales * 2）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'DoubleSales' in x.columns
        }
    },
    {
        'id': 31,
        'title': '文字列操作（大文字変換）',
        'description': 'DataFrame `df` の Product 列のすべての値を大文字に変換して、変数 `result` に代入してください。',
        'hint': 'str.upper()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Product列を大文字に変換\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
            'check_function': lambda x: all(x.str.isupper())
        }
    },
    {
        'id': 32,
        'title': '条件に基づく値の変更',
        'description': 'DataFrame `df` の Sales が 1000 以上の行に "High"、それ以外に "Low" を設定する "Category" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'np.where()を使用するか、条件分岐でマスクを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Category列を追加（Salesが1000以上ならHigh、それ以外はLow）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Category' in x.columns
        }
    },
    {
        'id': 33,
        'title': 'インデックスのリセット',
        'description': 'DataFrame `df` のインデックスをリセットして、変数 `result` に代入してください。',
        'hint': 'reset_index()メソッドを使用します。drop=Trueで元のインデックスを削除できます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# インデックスをリセット\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    # 欠損値処理（中級）
    {
        'id': 34,
        'title': '欠損値の確認',
        'description': 'DataFrame `df` の各列の欠損値の数をカウントして、変数 `result` に代入してください。',
        'hint': 'isnull().sum()を使用します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# 各列の欠損値をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 35,
        'title': '欠損値を含む行の削除',
        'description': 'DataFrame `df` から欠損値を含む行をすべて削除して、変数 `result` に代入してください。',
        'hint': 'dropna()メソッドを使用します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# 欠損値を含む行を削除\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: not x.isnull().any().any()
        }
    },
    {
        'id': 36,
        'title': '欠損値を平均値で埋める',
        'description': 'DataFrame `df` の Sales 列の欠損値を、その列の平均値で埋めて、変数 `result` に代入してください。',
        'hint': 'fillna()メソッドに平均値を渡します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# Sales列の欠損値を平均値で埋める\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 37,
        'title': '前方補完',
        'description': 'DataFrame `df` の欠損値を前の行の値で埋めて（前方補完）、変数 `result` に代入してください。',
        'hint': 'fillna()メソッドにmethod="ffill"を指定します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# 欠損値を前方補完\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 38,
        'title': '特定列の欠損値のみ削除',
        'description': 'DataFrame `df` から Sales 列に欠損値がある行のみを削除して、変数 `result` に代入してください。',
        'hint': 'dropna()メソッドにsubset引数で列を指定します。',
        'dataset': 'sales_data_with_nan.csv',
        'initial_code': '# Sales列が欠損している行を削除\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    # ソートとランキング
    {
        'id': 39,
        'title': '複数列でのソート',
        'description': 'DataFrame `df` を Product で昇順、Sales で降順にソートして、変数 `result` に代入してください。',
        'hint': 'sort_values()に複数の列名とascendingのリストを渡します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductとSalesでソート\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 40,
        'title': 'インデックスでのソート',
        'description': 'DataFrame `df` をインデックスで降順にソートして、変数 `result` に代入してください。',
        'hint': 'sort_index()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# インデックスで降順ソート\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 41,
        'title': 'ランキングの追加',
        'description': 'DataFrame `df` に、Sales 列の値に基づくランキングを "Rank" 列として追加してください。結果を `result` に代入してください。',
        'hint': 'rank()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Rank列を追加（Salesのランキング）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Rank' in x.columns
        }
    },
    {
        'id': 42,
        'title': '上位N件の抽出',
        'description': 'DataFrame `df` から Sales が上位3件の行を抽出して、変数 `result` に代入してください。',
        'hint': 'nlargest()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesの上位3件を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: len(x) == 3
        }
    },
    {
        'id': 43,
        'title': '下位N件の抽出',
        'description': 'DataFrame `df` から Sales が下位2件の行を抽出して、変数 `result` に代入してください。',
        'hint': 'nsmallest()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesの下位2件を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: len(x) == 2
        }
    },
    # 従業員データを使った問題
    {
        'id': 44,
        'title': '部門ごとの平均給与',
        'description': 'DataFrame `df` を Department 列でグループ化し、各部門の平均給与（Salary）を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmean()を組み合わせます。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 部門ごとの平均給与を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 45,
        'title': '高給与従業員の抽出',
        'description': 'DataFrame `df` から Salary が 80000 以上の従業員を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 給与が80000以上の従業員を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Salary'] >= 80000)
        }
    },
    {
        'id': 46,
        'title': '年齢別ソート',
        'description': 'DataFrame `df` を Age 列で降順にソートして、変数 `result` に代入してください。',
        'hint': 'sort_values()メソッドでascending=Falseを指定します。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 年齢で降順ソート\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 47,
        'title': '部門ごとの従業員数',
        'description': 'DataFrame `df` を Department 列でグループ化し、各部門の従業員数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とsize()を組み合わせます。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 部門ごとの従業員数をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 48,
        'title': '勤続年数の長い従業員',
        'description': 'DataFrame `df` から YearsOfService が 10 以上の従業員の Name を取得して、変数 `result` に代入してください。',
        'hint': 'フィルタリング後に特定の列を選択します。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 勤続10年以上の従業員名を取得\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 49,
        'title': 'パフォーマンス評価A',
        'description': 'DataFrame `df` から Performance が "A" の従業員を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'employee_data.csv',
        'initial_code': '# パフォーマンスがAの従業員を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Performance'] == 'A')
        }
    },
    {
        'id': 50,
        'title': '部門別最高給与',
        'description': 'DataFrame `df` を Department 列でグループ化し、各部門の最高給与を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmax()を組み合わせます。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 部門別最高給与を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 51,
        'title': '年齢の平均値',
        'description': 'DataFrame `df` の Age 列の平均値を計算して、変数 `result` に代入してください。',
        'hint': 'mean()メソッドを使用します。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 年齢の平均値を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    # 学生成績データを使った問題
    {
        'id': 52,
        'title': '合計点の計算',
        'description': 'DataFrame `df` に、各学生の Math、English、Science、History の合計点を "Total" 列として追加してください。結果を `result` に代入してください。',
        'hint': 'sum(axis=1)で行ごとの合計を計算できます。',
        'dataset': 'student_scores.csv',
        'initial_code': '# Total列を追加（4科目の合計）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Total' in x.columns
        }
    },
    {
        'id': 53,
        'title': '平均点の計算',
        'description': 'DataFrame `df` に、各学生の Math、English、Science、History の平均点を "Average" 列として追加してください。結果を `result` に代入してください。',
        'hint': 'mean(axis=1)で行ごとの平均を計算できます。',
        'dataset': 'student_scores.csv',
        'initial_code': '# Average列を追加（4科目の平均）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Average' in x.columns
        }
    },
    {
        'id': 54,
        'title': '数学の最高得点',
        'description': 'DataFrame `df` の Math 列の最高得点を計算して、変数 `result` に代入してください。',
        'hint': 'max()メソッドを使用します。',
        'dataset': 'student_scores.csv',
        'initial_code': '# 数学の最高得点を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 55,
        'title': 'クラスごとの平均点',
        'description': 'DataFrame `df` を Class 列でグループ化し、各クラスの Math の平均点を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmean()を組み合わせます。',
        'dataset': 'student_scores.csv',
        'initial_code': '# クラスごとの数学平均点を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 56,
        'title': '高得点学生の抽出',
        'description': 'DataFrame `df` から Math が 90 以上の学生を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'student_scores.csv',
        'initial_code': '# 数学が90点以上の学生を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Math'] >= 90)
        }
    },
    {
        'id': 57,
        'title': '全科目の平均点',
        'description': 'DataFrame `df` の Math、English、Science、History の全体平均点を計算して、変数 `result` に代入してください。',
        'hint': '複数列を選択してmean()を適用します。',
        'dataset': 'student_scores.csv',
        'initial_code': '# 全科目の平均点を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 58,
        'title': '特定学生の抽出',
        'description': 'DataFrame `df` から Name が "Taro" の学生の情報を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'student_scores.csv',
        'initial_code': '# Taroの情報を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 59,
        'title': '科目ごとの最高得点学生',
        'description': 'DataFrame `df` から Math の得点が最も高い学生の Name を取得して、変数 `result` に代入してください。',
        'hint': 'idxmax()でインデックスを取得し、loc[]で名前を取得します。',
        'dataset': 'student_scores.csv',
        'initial_code': '# 数学の得点が最も高い学生名を取得\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    # 在庫管理データを使った問題
    {
        'id': 60,
        'title': 'カテゴリごとの在庫数',
        'description': 'DataFrame `df` を Category 列でグループ化し、各カテゴリの Stock の合計を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とsum()を組み合わせます。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# カテゴリごとの在庫合計を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 61,
        'title': '高額商品の抽出',
        'description': 'DataFrame `df` から Price が 10000 以上の商品を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# 価格が10000以上の商品を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Price'] >= 10000)
        }
    },
    {
        'id': 62,
        'title': '在庫金額の計算',
        'description': 'DataFrame `df` に、Price と Stock を掛けた値を持つ "TotalValue" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'df["新列"] = df["列1"] * df["列2"] の形式で計算します。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# TotalValue列を追加（Price * Stock）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'TotalValue' in x.columns
        }
    },
    {
        'id': 63,
        'title': 'サプライヤーごとの商品数',
        'description': 'DataFrame `df` を Supplier 列でグループ化し、各サプライヤーの商品数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とsize()を組み合わせます。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# サプライヤーごとの商品数をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 64,
        'title': '在庫不足商品の抽出',
        'description': 'DataFrame `df` から Stock が 50 以下の商品を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# 在庫が50以下の商品を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Stock'] <= 50)
        }
    },
    {
        'id': 65,
        'title': 'カテゴリごとの平均価格',
        'description': 'DataFrame `df` を Category 列でグループ化し、各カテゴリの平均価格を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmean()を組み合わせます。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# カテゴリごとの平均価格を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 66,
        'title': '特定カテゴリの商品抽出',
        'description': 'DataFrame `df` から Category が "Electronics" の商品を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# Electronicsカテゴリの商品を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Category'] == 'Electronics')
        }
    },
    {
        'id': 67,
        'title': '最も在庫が多い商品',
        'description': 'DataFrame `df` から Stock が最も多い商品の ItemName を取得して、変数 `result` に代入してください。',
        'hint': 'idxmax()でインデックスを取得し、loc[]で商品名を取得します。',
        'dataset': 'store_inventory.csv',
        'initial_code': '# 最も在庫が多い商品名を取得\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    # 天気データを使った問題
    {
        'id': 68,
        'title': '都市ごとの平均気温',
        'description': 'DataFrame `df` を City 列でグループ化し、各都市の平均気温（Temperature）を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とmean()を組み合わせます。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 都市ごとの平均気温を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 69,
        'title': '降水量がある日の抽出',
        'description': 'DataFrame `df` から Precipitation が 0 より大きい日を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 降水量がある日を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Precipitation'] > 0)
        }
    },
    {
        'id': 70,
        'title': '最高気温の日',
        'description': 'DataFrame `df` から Temperature が最高の日の City と Date を取得して、変数 `result` に代入してください。',
        'hint': 'idxmax()でインデックスを取得し、loc[]で行を取得します。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 最高気温の日の情報を取得\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 71,
        'title': '都市ごとの総降水量',
        'description': 'DataFrame `df` を City 列でグループ化し、各都市の総降水量を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とsum()を組み合わせます。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 都市ごとの総降水量を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 72,
        'title': '湿度の高い日',
        'description': 'DataFrame `df` から Humidity が 70 以上の日を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 湿度が70以上の日を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Humidity'] >= 70)
        }
    },
    {
        'id': 73,
        'title': '東京の天気データ',
        'description': 'DataFrame `df` から City が "Tokyo" のデータを抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 東京の天気データを抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['City'] == 'Tokyo')
        }
    },
    {
        'id': 74,
        'title': '風速の平均',
        'description': 'DataFrame `df` の WindSpeed 列の平均値を計算して、変数 `result` に代入してください。',
        'hint': 'mean()メソッドを使用します。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 風速の平均を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 75,
        'title': '気温の分散',
        'description': 'DataFrame `df` の Temperature 列の分散を計算して、変数 `result` に代入してください。',
        'hint': 'var()メソッドを使用します。',
        'dataset': 'weather_data.csv',
        'initial_code': '# 気温の分散を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    # 複雑な販売データを使った問題
    {
        'id': 76,
        'title': '割引後の価格計算',
        'description': 'DataFrame `df` に、Price に (1 - Discount) を掛けた値を持つ "FinalPrice" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'df["新列"] = df["列1"] * (1 - df["列2"]) の形式で計算します。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# FinalPrice列を追加（割引後価格）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'FinalPrice' in x.columns
        }
    },
    {
        'id': 77,
        'title': '売上金額の計算',
        'description': 'DataFrame `df` に、FinalPrice（割引後価格）に Quantity を掛けた "Revenue" 列を追加してください。結果を `result` に代入してください。',
        'hint': '先にFinalPriceを計算してから、それにQuantityを掛けます。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# Revenue列を追加（売上金額）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Revenue' in x.columns
        }
    },
    {
        'id': 78,
        'title': 'カテゴリごとの売上合計',
        'description': 'DataFrame `df` から、Price * Quantity で売上を計算し、Category ごとの合計を求めて、変数 `result` に代入してください。',
        'hint': '売上列を作成してからgroupby()とsum()を使用します。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# カテゴリごとの売上合計を計算\n',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 79,
        'title': '地域ごとの注文数',
        'description': 'DataFrame `df` を Region 列でグループ化し、各地域の注文数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とsize()を組み合わせます。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# 地域ごとの注文数をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 80,
        'title': '高額注文の抽出',
        'description': 'DataFrame `df` から Price * Quantity が 100000 以上の注文を抽出して、変数 `result` に代入してください。',
        'hint': '計算列を作成するか、条件式内で直接計算します。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# 売上が100000以上の注文を抽出\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 81,
        'title': '割引率の高い注文',
        'description': 'DataFrame `df` から Discount が 0.1 以上の注文を抽出して、変数 `result` に代入してください。',
        'hint': '条件式でフィルタリングします。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# 割引率が10%以上の注文を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: all(x['Discount'] >= 0.1)
        }
    },
    {
        'id': 82,
        'title': '顧客ごとの注文回数',
        'description': 'DataFrame `df` を CustomerID 列でグループ化し、各顧客の注文回数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とsize()を組み合わせます。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# 顧客ごとの注文回数をカウント\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 83,
        'title': '日付でのフィルタリング',
        'description': 'DataFrame `df` から Date が "2024-01-20" 以降の注文を抽出して、変数 `result` に代入してください。',
        'hint': '文字列として比較するか、pd.to_datetime()で日付型に変換します。',
        'dataset': 'complex_sales.csv',
        'initial_code': '# 2024-01-20以降の注文を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    # 高度な操作
    {
        'id': 84,
        'title': 'ピボットテーブルの作成',
        'description': 'DataFrame `df` から、Product を行、Region を列とし、Sales の合計値を表示するピボットテーブルを作成して、変数 `result` に代入してください。',
        'hint': 'pivot_table()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ピボットテーブルを作成\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 85,
        'title': 'クロス集計',
        'description': 'DataFrame `df` の Product と Region のクロス集計を行い、出現回数を表示して、変数 `result` に代入してください。',
        'hint': 'pd.crosstab()を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# クロス集計を実行\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 86,
        'title': '累積合計の計算',
        'description': 'DataFrame `df` の Sales 列の累積合計を計算して、変数 `result` に代入してください。',
        'hint': 'cumsum()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesの累積合計を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 87,
        'title': 'パーセンタイルの計算',
        'description': 'DataFrame `df` の Sales 列の75パーセンタイル値を計算して、変数 `result` に代入してください。',
        'hint': 'quantile()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# 75パーセンタイルを計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 88,
        'title': '移動平均の計算',
        'description': 'DataFrame `df` の Sales 列の3期間移動平均を計算して、変数 `result` に代入してください。',
        'hint': 'rolling()メソッドとmean()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# 3期間移動平均を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 89,
        'title': '条件付き集計',
        'description': 'DataFrame `df` から、Sales が 1000 以上の行のみを対象に、Product ごとの Quantity の合計を計算して、変数 `result` に代入してください。',
        'hint': 'フィルタリング後にgroupby()とsum()を適用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesが1000以上の行でProductごとのQuantity合計を計算\n',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 90,
        'title': '複数の集約関数',
        'description': 'DataFrame `df` を Product 列でグループ化し、Sales の合計、平均、最大値を同時に計算して、変数 `result` に代入してください。',
        'hint': 'agg()メソッドに["sum", "mean", "max"]を渡します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの複数統計量を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 91,
        'title': 'ビニング（ビン分割）',
        'description': 'DataFrame `df` の Sales 列を3つの区間に分割し、"Low"、"Medium"、"High" のラベルを付けた "SalesCategory" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'pd.cut()を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# SalesCategory列を追加（3区間に分割）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'SalesCategory' in x.columns
        }
    },
    {
        'id': 92,
        'title': '重複行の確認',
        'description': 'DataFrame `df` に重複行があるかどうかを確認し、重複行を抽出して、変数 `result` に代入してください。',
        'hint': 'duplicated()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# 重複行を抽出\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 93,
        'title': '特定列での重複削除',
        'description': 'DataFrame `df` から Product 列が重複する行を削除し、最初の行のみを残して、変数 `result` に代入してください。',
        'hint': 'drop_duplicates()メソッドにsubset引数を指定します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Product列で重複を削除\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 94,
        'title': '条件に基づく複数値の設定',
        'description': 'DataFrame `df` に、Sales が 1500 以上なら "A"、1000 以上 1500 未満なら "B"、それ以外なら "C" を設定する "Grade" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'np.select()またはpd.cut()を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Grade列を追加（条件分岐）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Grade' in x.columns
        }
    },
    {
        'id': 95,
        'title': '相関係数の計算',
        'description': 'DataFrame `df` の Sales 列と Quantity 列の相関係数を計算して、変数 `result` に代入してください。',
        'hint': 'corr()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# SalesとQuantityの相関係数を計算\nresult = ',
        'validation': {
            'variable': 'result',
        }
    },
    {
        'id': 96,
        'title': 'カテゴリデータのエンコーディング',
        'description': 'DataFrame `df` の Region 列をカテゴリコード（数値）に変換して、"RegionCode" 列として追加してください。結果を `result` に代入してください。',
        'hint': 'astype("category").cat.codesを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# RegionCode列を追加（カテゴリコード）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'RegionCode' in x.columns
        }
    },
    {
        'id': 97,
        'title': 'グループごとのランキング',
        'description': 'DataFrame `df` に、Product ごとの Sales のランキングを "ProductRank" 列として追加してください。結果を `result` に代入してください。',
        'hint': 'groupby()とrank()を組み合わせます。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductRank列を追加（Productごとのランキング）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'ProductRank' in x.columns
        }
    },
    {
        'id': 98,
        'title': 'グループ内での正規化',
        'description': 'DataFrame `df` に、Product ごとの Sales を 0-1 の範囲に正規化した "NormalizedSales" 列を追加してください。結果を `result` に代入してください。',
        'hint': 'groupby()とtransform()を使用し、(x - x.min()) / (x.max() - x.min())で正規化します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# NormalizedSales列を追加（Productごとに正規化）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'NormalizedSales' in x.columns
        }
    },
    {
        'id': 99,
        'title': 'カスタム集約関数の適用',
        'description': 'DataFrame `df` を Product 列でグループ化し、各グループの Sales の範囲（最大値 - 最小値）を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とagg()で lambda x: x.max() - x.min() を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの販売額の範囲を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 100,
        'title': 'マルチインデックスの作成',
        'description': 'DataFrame `df` を Product と Region 列でグループ化し、Sales の合計を計算して、マルチインデックスの結果を `result` に代入してください。',
        'hint': 'groupby()で複数列を指定し、as_index=Trueのままにします。',
        'dataset': 'sales_data.csv',
        'initial_code': '# マルチインデックスで集計\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 101,
        'title': 'グループごとの最頻値',
        'description': 'DataFrame `df` を Department 列でグループ化し、各部門で最も多い Performance 評価を取得して、変数 `result` に代入してください。',
        'hint': 'groupby()とagg()で lambda x: x.mode()[0] を使用します。',
        'dataset': 'employee_data.csv',
        'initial_code': '# 部門ごとの最頻Performance評価を取得\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 102,
        'title': '変化率の計算',
        'description': 'DataFrame `df` の Sales 列の前行からの変化率（パーセント）を計算して、変数 `result` に代入してください。',
        'hint': 'pct_change()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Salesの変化率を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 103,
        'title': '外れ値の検出',
        'description': 'DataFrame `df` の Sales 列で、平均値 ± 2標準偏差の範囲外にある値（外れ値）を持つ行を抽出して、変数 `result` に代入してください。',
        'hint': '平均と標準偏差を計算し、条件式で範囲外の値をフィルタリングします。',
        'dataset': 'sales_data.csv',
        'initial_code': '# 外れ値を持つ行を抽出\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 104,
        'title': '列の型変換',
        'description': 'DataFrame `df` の Quantity 列を float 型に変換して、変数 `result` に代入してください。',
        'hint': 'astype()メソッドを使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Quantity列をfloat型に変換\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 105,
        'title': '文字列の分割',
        'description': 'DataFrame `df` の Name 列を使用して、最初の文字だけを抽出し "Initial" 列として追加してください（employee_data使用）。結果を `result` に代入してください。',
        'hint': 'str[0]またはstr.slice()を使用します。',
        'dataset': 'employee_data.csv',
        'initial_code': '# Initial列を追加（名前の頭文字）\n',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
            'check_function': lambda x: 'Initial' in x.columns
        }
    },
    {
        'id': 106,
        'title': 'DataFrameのマージ準備',
        'description': 'DataFrame `df` から Product と Region 列のユニークな組み合わせを取得して、変数 `result` に代入してください。',
        'hint': 'drop_duplicates()を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# ProductとRegionのユニークな組み合わせを取得\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'DataFrame',
        }
    },
    {
        'id': 107,
        'title': '条件付きカウント',
        'description': 'DataFrame `df` を Product 列でグループ化し、各グループで Sales が 1000 以上の行数をカウントして、変数 `result` に代入してください。',
        'hint': 'groupby()とapply()でフィルタリングとカウントを行います。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとに1000以上のSalesの数をカウント\n',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
    {
        'id': 108,
        'title': '最小値と最大値の差',
        'description': 'DataFrame `df` の各 Product について、Sales の最大値と最小値の差を計算して、変数 `result` に代入してください。',
        'hint': 'groupby()とagg()で lambda x: x.max() - x.min() を使用します。',
        'dataset': 'sales_data.csv',
        'initial_code': '# Productごとの最大値と最小値の差を計算\nresult = ',
        'validation': {
            'variable': 'result',
            'type': 'Series',
        }
    },
]

def get_all_problems():
    """全ての問題を返す（検証関数は除外）"""
    return [
        {
            'id': p['id'],
            'title': p['title'],
            'description': p['description'],
            'hint': p.get('hint', ''),
            'dataset': p.get('dataset', ''),
            'initial_code': p.get('initial_code', '')
        }
        for p in PROBLEMS
    ]

def get_problem_by_id(problem_id):
    """IDで問題を取得"""
    for problem in PROBLEMS:
        if problem['id'] == problem_id:
            return problem
    return None
