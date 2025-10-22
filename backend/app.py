from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import io
import traceback
from code_executor import execute_code
from problems import get_all_problems, get_problem_by_id

app = Flask(__name__)
CORS(app)

@app.route('/api/problems', methods=['GET'])
def get_problems():
    """全ての問題を取得"""
    problems = get_all_problems()
    return jsonify(problems)

@app.route('/api/problems/<int:problem_id>', methods=['GET'])
def get_problem(problem_id):
    """特定の問題を取得"""
    problem = get_problem_by_id(problem_id)
    if problem:
        return jsonify(problem)
    return jsonify({'error': 'Problem not found'}), 404

@app.route('/api/execute', methods=['POST'])
def execute():
    """コードを実行して結果を返す"""
    data = request.json
    code = data.get('code', '')
    problem_id = data.get('problem_id')

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    result = execute_code(code, problem_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
