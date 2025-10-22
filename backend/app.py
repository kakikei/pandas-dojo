from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.code_executor import execute_code
from backend.problems import get_all_problems, get_problem_by_id

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health_check():
    """ヘルスチェックエンドポイント"""
    return jsonify({
        'status': 'ok',
        'message': 'Pandas Dojo API is running',
        'endpoints': {
            'problems': '/api/problems',
            'problem_detail': '/api/problems/<id>',
            'execute': '/api/execute'
        }
    })

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
    app.run(debug=True, host='0.0.0.0', port=5001)
