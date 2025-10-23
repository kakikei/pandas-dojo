"""
検証エンジン
構造化された検証ルールを解釈して実行
"""
import pandas as pd
import numpy as np


def run_validation_check(check, result):
    """
    単一の検証チェックを実行

    Args:
        check: 検証チェック定義（辞書）
        result: 検証対象の値

    Returns:
        bool: 検証結果（True=成功、False=失敗）
    """
    check_type = check['type']

    # 型チェック
    if check_type == 'type_check':
        expected_type = check['expected_type']
        type_map = {
            'DataFrame': pd.DataFrame,
            'Series': pd.Series,
            'tuple': tuple,
            'list': list,
            'dict': dict,
            'int': (int, np.integer),
            'float': (float, np.floating),
            'str': str
        }
        expected_class = type_map.get(expected_type)
        if expected_class is None:
            return False
        return isinstance(result, expected_class)

    # 複数型のいずれかチェック
    elif check_type == 'type_check_or':
        expected_types = check['expected_types']
        type_map = {
            'DataFrame': pd.DataFrame,
            'Series': pd.Series,
            'tuple': tuple,
            'list': list
        }
        for expected_type in expected_types:
            expected_class = type_map.get(expected_type)
            if expected_class and isinstance(result, expected_class):
                return True
        return False

    # 長さチェック
    elif check_type == 'length_equals':
        try:
            return len(result) == check['value']
        except:
            return False

    # 列の存在チェック
    elif check_type == 'column_exists':
        if not isinstance(result, pd.DataFrame):
            return False
        return check['column'] in result.columns

    # 列の非存在チェック
    elif check_type == 'column_not_exists':
        if not isinstance(result, pd.DataFrame):
            return False
        return check['column'] not in result.columns

    # 列名リストの一致チェック
    elif check_type == 'columns_equal':
        if not isinstance(result, pd.DataFrame):
            return False
        return list(result.columns) == check['columns']

    # 欠損値なしチェック
    elif check_type == 'no_nulls':
        if isinstance(result, pd.DataFrame):
            return not result.isnull().any().any()
        elif isinstance(result, pd.Series):
            return not result.isnull().any()
        return False

    # 列の全ての値が >= valueチェック
    elif check_type == 'column_all_gte':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        return all(result[column] >= check['value'])

    # 列の全ての値が > valueチェック
    elif check_type == 'column_all_gt':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        return all(result[column] > check['value'])

    # 列の全ての値が <= valueチェック
    elif check_type == 'column_all_lte':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        return all(result[column] <= check['value'])

    # 列の全ての値が == valueチェック
    elif check_type == 'column_all_eq':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        return all(result[column] == check['value'])

    # 列の全ての値が指定リストに含まれるチェック
    elif check_type == 'column_all_in':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        return all(result[column].isin(check['values']))

    # 列の全ての値が文字列を含むチェック
    elif check_type == 'column_str_contains':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        try:
            return all(result[column].str.contains(check['substring']))
        except:
            return False

    # 列の全ての値が範囲内チェック
    elif check_type == 'column_all_between':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        min_val = check['min']
        max_val = check['max']
        return all((result[column] >= min_val) & (result[column] <= max_val))

    # 列がソート済みチェック
    elif check_type == 'column_sorted':
        if not isinstance(result, pd.DataFrame):
            return False
        column = check['column']
        if column not in result.columns:
            return False
        ascending = check.get('ascending', True)
        sorted_values = sorted(result[column], reverse=not ascending)
        return list(result[column]) == sorted_values

    # Seriesの全ての値が大文字チェック
    elif check_type == 'str_all_upper':
        if not isinstance(result, pd.Series):
            return False
        try:
            return all(result.str.isupper())
        except:
            return False

    # 配列に値が含まれるチェック
    elif check_type == 'array_contains':
        try:
            if isinstance(result, (pd.Series, pd.DataFrame)):
                return check['value'] in result.values
            else:
                return check['value'] in result
        except:
            return False

    # 未知のチェックタイプ
    else:
        print(f"Warning: Unknown check type '{check_type}'")
        return True  # 未知のチェックは無視


def validate_result(validation_rules, result):
    """
    検証ルールに基づいて結果を検証

    Args:
        validation_rules: 検証ルール辞書（variable, checks）
        result: 検証対象の値

    Returns:
        bool: 検証結果（True=成功、False=失敗）
    """
    if not validation_rules:
        return True

    checks = validation_rules.get('checks', [])

    # 全てのチェックを実行
    for check in checks:
        if not run_validation_check(check, result):
            return False

    return True
