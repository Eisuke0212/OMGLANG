import streamlit as st
import sys
import io

# ページ全体のタイトル
st.title("OMG LANG Web Studio")
st.write("日本語で書いたコードをブラウザでそのまま実行できる、あなただけの言語環境です！")

# 1. 翻訳して実行し、出力結果（printなど）を文字としてキャプチャする関数
def 実行して結果を取得する(日本語コードの文字列):
    # あなたの言語の変換ルール
    pythonコード = 日本語コードの文字列.replace("表示", "print")
    pythonコード = pythonコード.replace("もし", "if")
    pythonコード = pythonコード.replace("ならば", ":")
    pythonコード = pythonコード.replace("繰り返す", "while True:")
    pythonコード = pythonコード.replace("終了", "break")
    pythonコード = pythonコード.replace("関数", "def")
    pythonコード = pythonコード.replace("戻り値", "return")
    pythonコード = pythonコード.replace("インポート", "import")
    pythonコード = pythonコード.replace("クラス", "class")
    pythonコード = pythonコード.replace("開始クラス", "(")
    pythonコード = pythonコード.replace("終了クラス", ")")
    pythonコード = pythonコード.replace("開始関数", "(")
    pythonコード = pythonコード.replace("終了関数", ")")
    pythonコード = pythonコード.replace("開始ブロック", ":")
    pythonコード = pythonコード.replace("終了ブロック", "")
    pythonコード = pythonコード.replace("真", "True")
    pythonコード = pythonコード.replace("偽", "False")
    pythonコード = pythonコード.replace("なし", "None")
    pythonコード = pythonコード.replace("リスト", "list")
    pythonコード = pythonコード.replace("辞書", "dict")
    pythonコード = pythonコード.replace("タプル", "tuple")
    pythonコード = pythonコード.replace("セット", "set")
    pythonコード = pythonコード.replace("文字列", "str")
    pythonコード = pythonコード.replace("整数", "int")
    pythonコード = pythonコード.replace("浮動小数点", "float")
    pythonコード = pythonコード.replace("ブール", "bool")
    pythonコード = pythonコード.replace("入力", "input")
    pythonコード = pythonコード.replace("長さ", "len")
    pythonコード = pythonコード.replace("範囲", "range")
    pythonコード = pythonコード.replace("例外", "Exception")
    pythonコード = pythonコード.replace("エラー", "Error")
    pythonコード = pythonコード.replace("ファイル", "file")
    pythonコード = pythonコード.replace("開く", "open")
    pythonコード = pythonコード.replace("閉じる", "close")
    pythonコード = pythonコード.replace("読み込む", "read")
    pythonコード = pythonコード.replace("書き込む", "write")
    pythonコード = pythonコード.replace("追加", "append")
    pythonコード = pythonコード.replace("削除", "remove")
    pythonコード = pythonコード.replace("存在する", "exists")
    pythonコード = pythonコード.replace("コピー", "copy")
    pythonコード = pythonコード.replace("移動", "move")
    pythonコード = pythonコード.replace("日付", "datetime") 
    pythonコード = pythonコード.replace("時間", "time")
    pythonコード = pythonコード.replace("モジュール", "module")
    pythonコード = pythonコード.replace("パッケージ", "package")
    pythonコード = pythonコード.replace("ライブラリ", "library")
    pythonコード = pythonコード.replace("バージョン", "version")
    pythonコード = pythonコード.replace("設定", "config")
    pythonコード = pythonコード.replace("環境", "environment")
    pythonコード = pythonコード.replace("変数", "variable")
    pythonコード = pythonコード.replace("定数", "constant")
    pythonコード = pythonコード.replace("関数名", "function_name")
    pythonコード = pythonコード.replace("クラス名", "class_name")
    pythonコード = pythonコード.replace("メソッド", "method")
    pythonコード = pythonコード.replace("属性", "attribute")
    pythonコード = pythonコード.replace("引数", "argument")
    pythonコード = pythonコード.replace("戻り値", "return_value")
    pythonコード = pythonコード.replace("例外処理", "try_except")
    pythonコード = pythonコード.replace("条件分岐", "if_else")
    pythonコード = pythonコード.replace("ループ", "loop")
    pythonコード = pythonコード.replace("リスト内包表記", "list_comprehension")
    pythonコード = pythonコード.replace("辞書内包表記", "dict_comprehension")
    pythonコード = pythonコード.replace("タプル内包表記", "tuple_comprehension")
    pythonコード = pythonコード.replace("セット内包表記", "set_comprehension")
    pythonコード = pythonコード.replace("ラムダ", "lambda")
    pythonコード = pythonコード.replace("デコレーター", "decorator")
    pythonコード = pythonコード.replace("ジェネレーター", "generator")
    pythonコード = pythonコード.replace("イテレーター", "iterator")
    pythonコード = pythonコード.replace("コンテキストマネージャー", "context_manager")
    pythonコード = pythonコード.replace("非同期", "async")
    pythonコード = pythonコード.replace("待機", "await")
    pythonコード = pythonコード.replace("スレッド", "thread")

    # printなどの出力を画面に表示するために、一時的に出力先を横取りする仕組み
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(pythonコード)
        結果 = new_stdout.getvalue()
    except Exception as エラー:
        結果 = f"【エラー】書き方を確認してね:\n{エラー}"
    finally:
        sys.stdout = old_stdout  # 元に戻す

    return 結果

# 2. 画面のデザイン（レイアウト）
st.subheader(" コード入力エリア")
default_code = """# ここにOMG LANGのコードを書こう！
スコア = 整数(85)

表示("あなたのテストの点数は...")
表示(スコア)
表示("点です！")

もし スコア >= 80 ならば
    表示("おめでとう！よくできました！")
"""

# コードを入力する大きなテキストボックス
ユーザーの入力コード = st.text_area("コードエディタ", default_code, height=200)

# 実行ボタン
if st.button("実行する"):
    if ユーザーの入力コード.strip() == "":
        st.warning("コードが空だよ！何か書いてね。")
    else:
        st.subheader("実行結果")
        # 実行して結果を取得
        出力結果 = 実行して結果を取得する(ユーザーの入力コード)
        # 画面に結果を綺麗に表示
        st.code(出力結果, language="text")