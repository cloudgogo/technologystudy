# 下载pip及切换源
1. 查找ubuntu下的Python3
```sh
whereis python3
```
2. 修改python默认指向
```sh
sudo mv /usr/bin/python /usr/bin/python.bak
sudo ln -s /usr/bin/python3 /usr/bin/python
```
3. 检查Python版本
```sh
python -V
```
4. 下载pip3
```sh
sudo apt-get install python3-pip
```
5. 输入命令查看pip3的版本，如果正常显示说明安装成功
```sh
pip3 -V
```
6. 升级pip3
```sh
sudo pip3 install --upgrade pip
```
7. 卸载pip3
```sh
sudo apt-get remove python3-pip
```
8. 调整源   
    编辑文本,若目录不存在就添加
    ```sh
    vim ~/.pip/pip.conf
    ```
    编辑内容
    > 说明:url为源地址,若源地址不为https协议地址,则需添加下面那段用于信任
    ```txt
    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple
    [install]
    trusted-host = mirrors.aliyun.com
    ```