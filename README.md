# 概要
入力された映画のレビューが"positive"かnegativeかを判定し、分類器の性能を向上させるアプリケーション。  
IMDMの映画レビューデータセットのレビューをトークンにし、ロジスティック回帰分類器を学習している。フレームワークとしてFlaskを用い、入力されたレビューの保持にはSQLite3を使用している。  

# 実行方法  
python app.pyでプログラムを実行し、http:127.0.0.1:5000 にアクセスする。
# 実行画面

・テキストフィールドに映画の感想を入力する。  

<img width="960" alt="sentiment-result1" src="https://user-images.githubusercontent.com/62968285/148700905-763fbb1d-2b52-4566-ba47-179d8274fdbe.png">
  
・入力された映画の感想を"positive"か"negative"であるかをその確率とともに提示する。ユーザはその判定が正しいかどうかをボタンで選び、分類器の性能の向上につなげる。  

<img width="960" alt="result2" src="https://user-images.githubusercontent.com/62968285/148700909-ece1c7b4-ad61-409e-9547-91965883aadb.png">
  
・"thank you" メッセージを表示する。"Submit another review"ボタンを押すと、最初のページに戻る。  

<img width="960" alt="sentiment-result3" src="https://user-images.githubusercontent.com/62968285/148700914-b1a47d8e-7d0a-4a36-af96-1d14770ad56e.png">

