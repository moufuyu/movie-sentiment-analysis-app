# 概要
入力された映画のレビューが"positive"かnegativeかを判定し、分類器の性能を向上させるアプリケーション。  
IMDMの映画レビューデータセットのレビューをトークンにし、ロジスティック回帰分類器を学習している(学習した分類器とNLTKライブラリのストップワードは、pickleにdumpし、app.py内でで読み出す)。  
フレームワークとしてFlaskを用い、入力されたレビューの保持にはSQLite3を使用している。  

# 実行方法  
python app.pyでプログラムを実行し、http://127.0.0.1:5000 にアクセスする。
# 実行画面

・テキストフィールドに映画の感想を入力する。  

<img width="960" alt="sentiment-result1" src="https://user-images.githubusercontent.com/62968285/148700905-763fbb1d-2b52-4566-ba47-179d8274fdbe.png">
  
・入力された映画の感想を"positive"か"negative"であるかをその確率とともに提示する。ユーザはその判定が正しいかどうかをボタンで選び、分類器の性能の向上につなげる。  

<img width="960" alt="result2" src="https://user-images.githubusercontent.com/62968285/148700909-ece1c7b4-ad61-409e-9547-91965883aadb.png">
  
・"thank you" メッセージを表示する。"Submit another review"ボタンを押すと、最初のページに戻る。  

<img width="960" alt="sentiment-result3" src="https://user-images.githubusercontent.com/62968285/148700914-b1a47d8e-7d0a-4a36-af96-1d14770ad56e.png">  

# 参考文献  
[第3版]Python機械学習プログラミング 達人データサイエンティストによる理論と実践 (impress top gear)   
(https://www.amazon.co.jp/%E7%AC%AC3%E7%89%88-Python%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E9%81%94%E4%BA%BA%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88%E3%81%AB%E3%82%88%E3%82%8B%E7%90%86%E8%AB%96%E3%81%A8%E5%AE%9F%E8%B7%B5-impress-gear/dp/4295010073)


