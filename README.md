# grpc-python-example

* 必要なライブラリをインストールする


```
$ pipenv install
```

* 実際には以下のライブラリがあれば良い
    * grpcio
    * grpcio-tools

## 今あるサンプルを使う

* シェルをひとつ開く

```
$ pwd
/path/to/grpc-python-example

$ python src/server/server.py
```

* シェルをもうひとつ開く

```
$ pwd
/path/to/grpc-python-example

$ python src/client/client.py
Greeter client received: Hello, you
```

* あとはご自由に

## 参考

* https://github.com/grpc/grpc
