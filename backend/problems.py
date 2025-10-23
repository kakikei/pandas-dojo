"""
Pandas学習問題の定義

問題定義と検証ルールはproblems.jsonから読み込む
"""
import json
import os

# 現在のファイルのディレクトリを取得
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_JSON_PATH = os.path.join(CURRENT_DIR, 'problems.json')

# JSONファイルから問題定義を読み込む
def load_problems():
    """JSONファイルから問題を読み込む"""
    with open(PROBLEMS_JSON_PATH, 'r', encoding='utf-8') as f:
        problems_data = json.load(f)
    return problems_data

# 問題リストを読み込む
PROBLEMS = load_problems()


def get_all_problems():
    """全ての問題を返す（検証ルールは除外）"""
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
    """IDで問題を取得（検証ルールは除外）"""
    for problem in PROBLEMS:
        if problem['id'] == problem_id:
            return {
                'id': problem['id'],
                'title': problem['title'],
                'description': problem['description'],
                'hint': problem.get('hint', ''),
                'dataset': problem.get('dataset', ''),
                'initial_code': problem.get('initial_code', '')
            }
    return None


def get_problem_with_validation(problem_id):
    """IDで問題を取得（検証ルールを含む - 内部使用のみ）"""
    for problem in PROBLEMS:
        if problem['id'] == problem_id:
            return problem
    return None
