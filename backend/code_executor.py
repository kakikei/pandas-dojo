import sys
import io
import traceback
import pandas as pd
import numpy as np
from backend.problems import get_problem_by_id, get_problem_with_validation
from backend.validations import validate_result

def execute_code(code, problem_id):
    """
    ユーザーのコードを実行し、結果を返す

    Args:
        code: 実行するPythonコード
        problem_id: 問題ID（正誤判定用）

    Returns:
        dict: 実行結果と正誤判定
    """
    # 標準出力をキャプチャ
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    result = {
        'success': False,
        'output': '',
        'error': '',
        'is_correct': False,
        'feedback': ''
    }

    try:
        # 問題情報を取得（検証用に完全な情報を取得）
        problem = get_problem_with_validation(problem_id) if problem_id else None

        # 実行環境を準備
        namespace = {
            'pd': pd,
            'np': np,
            '__builtins__': __builtins__,
        }

        # 問題にデータセットがある場合は読み込む
        if problem and 'dataset' in problem:
            dataset_path = f"backend/datasets/{problem['dataset']}"
            namespace['df'] = pd.read_csv(dataset_path)

        # コードを実行
        exec(code, namespace)

        # 出力を取得
        output = captured_output.getvalue()
        result['output'] = output
        result['success'] = True

        # 正誤判定
        if problem and 'validation' in problem:
            is_correct, feedback = validate_solution(
                namespace,
                problem['validation']
            )
            result['is_correct'] = is_correct
            result['feedback'] = feedback

    except Exception as e:
        result['error'] = traceback.format_exc()

    finally:
        # 標準出力を復元
        sys.stdout = old_stdout

    return result

def validate_solution(namespace, validation):
    """
    ユーザーの解答を検証

    Args:
        namespace: コード実行後の名前空間
        validation: 検証ルール（構造化された形式）

    Returns:
        tuple: (is_correct, feedback)
    """
    try:
        # 期待される変数名
        expected_var = validation.get('variable', 'result')

        # 変数が存在するか確認
        if expected_var not in namespace:
            return False, f"変数 '{expected_var}' が見つかりません。"

        user_result = namespace[expected_var]

        # 新しい検証エンジンを使用
        is_correct = validate_result(validation, user_result)

        if is_correct:
            return True, "正解です！"
        else:
            return False, "期待される結果と異なります。"

    except Exception as e:
        return False, f"検証中にエラーが発生しました: {str(e)}"
