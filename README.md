# grpc-python-example

gPRC の Python 版実装サンプルです

## 開発環境を用意する

* 必要なライブラリをインストールする

```
$ pipenv install
```

* 実際には以下のライブラリがあれば良い
    * grpcio
    * grpcio-tools

## 今あるサンプルを使う

* シェルをひとつ開く
* 次のコマンドを実行してサーバーを起動する

```
$ pwd
/path/to/grpc-python-example

$ python server/server.py
```

* シェルをもうひとつ開く
* 次のコマンドを実行してクライアントの処理を実行する

```
$ pwd
/path/to/grpc-python-example

$ python client/client.py
Greeter client received: Hello, you
```

* あとはご自由に


## protoc でコードを生成する

* proto/helloworld.proto から Python のコードを生成する

```
$ pwd
/path/to/grpc-python-example

$ python -m grpc_tools.protoc \
    -I ./proto \
    --python_out=./pb \
    --grpc_python_out=./pb \
    ./proto/helloworld.proto
```

## 参考

* https://github.com/grpc/grpc
