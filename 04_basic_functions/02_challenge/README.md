# チャレンジ2 (ライブ)

Unicodeはコンピュータ業界の標準の文字コードであり、世界のほとんどの文字体系で使用されるテキストを一貫して表示、操作できるように設計されています。Unicodeはコンピューティングプラットフォーム、アプリケーション、言語に関係なく、各文字にUnicodeコードポイントと呼ばれる固有の番号を割り当てます。

ユーザーが入力として渡したメッセージをエンコードおよびデコードするプログラムを作成してください。次の手順で行います。

- `encode` 関数を作成します。`encode` 関数はリスト内の各文字を反復処理し、その文字のUnicode値に置き換えます。各文字のUnicode値を取得するには、`ord()` 組み込み関数を使用します。

- `decode` 関数を作成します。`decode` 関数は `encode` によって生成されたUnicode番号のシーケンスを反復処理し、文字に変換します。各Unicode番号の文字値を取得するには、`chr()` 組み込み関数を使用します。

`ord` と `chr` の使用方法を調査し、プログラムで空入力のようなエッジケースに対処できるようにしてください。

例
```python
encode("Hello World")  # 72 101 108 108 111 32 119 111 114 108 100
```

```python
decode("72 101 108 108 111 32 119 111 114 108 100")  # Hello World
```