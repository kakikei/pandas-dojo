// API URL
const API_BASE_URL = 'http://localhost:5001/api';

// グローバル変数
let problems = [];
let currentProblem = null;
let codeEditor = null;

// 初期化
document.addEventListener('DOMContentLoaded', async () => {
    await loadProblems();
    setupEventListeners();
});

// 問題一覧を読み込む
async function loadProblems() {
    try {
        const response = await fetch(`${API_BASE_URL}/problems`);
        problems = await response.json();
        renderProblemList();
    } catch (error) {
        console.error('問題の読み込みに失敗しました:', error);
        alert('問題の読み込みに失敗しました。バックエンドサーバーが起動しているか確認してください。');
    }
}

// 問題一覧を表示
function renderProblemList() {
    const listContainer = document.getElementById('problem-list');
    listContainer.innerHTML = '';

    problems.forEach(problem => {
        const item = document.createElement('div');
        item.className = 'problem-item';
        item.innerHTML = `
            <h3>問題 ${problem.id}</h3>
            <p>${problem.title}</p>
        `;
        item.addEventListener('click', () => selectProblem(problem.id));
        listContainer.appendChild(item);
    });
}

// 問題を選択
async function selectProblem(problemId) {
    try {
        const response = await fetch(`${API_BASE_URL}/problems/${problemId}`);
        currentProblem = await response.json();
        renderProblemDetail();

        // アクティブな問題をハイライト
        document.querySelectorAll('.problem-item').forEach((item, index) => {
            if (index === problemId - 1) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    } catch (error) {
        console.error('問題の読み込みに失敗しました:', error);
    }
}

// 問題の詳細を表示
function renderProblemDetail() {
    const detailContainer = document.getElementById('problem-detail');

    detailContainer.innerHTML = `
        <div class="problem-header">
            <h2>問題 ${currentProblem.id}: ${currentProblem.title}</h2>
            <p class="description">${currentProblem.description}</p>
            ${currentProblem.hint ? `<div class="hint">💡 ヒント: ${currentProblem.hint}</div>` : ''}
        </div>

        <div class="code-editor-container">
            <h3>コードエディター</h3>
            <textarea id="code-editor">${currentProblem.initial_code}</textarea>
        </div>

        <div class="actions">
            <button id="run-btn" class="btn btn-primary">実行</button>
            <button id="reset-btn" class="btn btn-secondary">リセット</button>
        </div>

        <div id="output-container" class="output-container" style="display: none;">
            <h3>実行結果</h3>
            <div id="output" class="output-box"></div>
            <div id="feedback" class="feedback" style="display: none;"></div>
        </div>
    `;

    // CodeMirrorエディターを初期化
    initCodeEditor();

    // イベントリスナーを設定
    document.getElementById('run-btn').addEventListener('click', runCode);
    document.getElementById('reset-btn').addEventListener('click', resetCode);
}

// CodeMirrorエディターを初期化
function initCodeEditor() {
    const textarea = document.getElementById('code-editor');
    codeEditor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: true,
        indentUnit: 4,
        indentWithTabs: false,
        lineWrapping: true,
    });
}

// コードを実行
async function runCode() {
    const code = codeEditor.getValue();
    const runBtn = document.getElementById('run-btn');
    const outputContainer = document.getElementById('output-container');
    const outputBox = document.getElementById('output');
    const feedbackBox = document.getElementById('feedback');

    // ボタンを無効化
    runBtn.disabled = true;
    runBtn.innerHTML = '実行中<span class="loading"></span>';

    // 以前の出力をクリア
    outputBox.className = 'output-box';
    outputBox.textContent = '';
    feedbackBox.style.display = 'none';
    outputContainer.style.display = 'block';

    try {
        const response = await fetch(`${API_BASE_URL}/execute`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                problem_id: currentProblem.id
            })
        });

        const result = await response.json();

        // 結果を表示
        if (result.success) {
            // 正誤判定の結果を表示
            if (result.feedback) {
                feedbackBox.style.display = 'block';
                feedbackBox.className = result.is_correct ? 'feedback correct' : 'feedback incorrect';
                feedbackBox.textContent = result.feedback;
            }

            // 出力がある場合のみ表示
            if (result.output && result.output.trim()) {
                outputBox.className = 'output-box success';
                outputBox.textContent = result.output;
            } else {
                // 出力がない場合は出力ボックスを非表示
                outputContainer.style.display = result.feedback ? 'block' : 'none';
            }
        } else {
            outputBox.className = 'output-box error';
            outputBox.textContent = result.error;
        }
    } catch (error) {
        outputBox.className = 'output-box error';
        outputBox.textContent = 'サーバーへの接続に失敗しました: ' + error.message;
    } finally {
        // ボタンを有効化
        runBtn.disabled = false;
        runBtn.textContent = '実行';
    }
}

// コードをリセット
function resetCode() {
    if (confirm('コードを初期状態に戻しますか？')) {
        codeEditor.setValue(currentProblem.initial_code);
        document.getElementById('output-container').style.display = 'none';
    }
}

// イベントリスナーを設定
function setupEventListeners() {
    // 必要に応じて追加のイベントリスナーを設定
}
