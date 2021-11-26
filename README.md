# SideProject03-RESTAPI
個人獨立小型專案<br>
使用 <a href="https://www.postman.com/">Postman</a></br>
網址: <a href="https://arcane-mesa-97312.herokuapp.com/">https://arcane-mesa-97312.herokuapp.com/</a> <br>

<img src='https://github.com/r97221004/SideProject03-RESTAPI/blob/master/img/Introduction.PNG'></img>

# 介紹
這是我的第三個個人獨立小型專案，模擬簡單的民宿訂房系統, 寫個 Rest API 接口。目前用到的技術:
<ul>
  <li>程式語言: Python、SQL</li>
  <li>框架: Flask</li>
  <li>資料庫: MySQL</li>
  <li>主要套件: Flask-SQLAlchemy、Flask-RESTful、Flask-JWT</li>
  <li>部屬: Heroku</li>
</ul>
主要的實現:
<ul>
  <li>權限細分</li>
  <li>民宿的評論</li>
  <li>民宿的預定與取消</li>
  <li>民宿管理員房間的風格規劃與房間管理</li>
  <li>單元測試</li>
  <li>pep8 檢測</li>
</ul>

# 資料庫的關係圖
<img src='https://github.com/r97221004/SideProject03-RESTAPI/blob/master/img/ER.PNG'></img>

# 啟動
使用 git clone 將程式碼下載到你的電腦且進入 SideProject01-PersonalWeb
```
$ git clone git@github.com:r97221004/SideProject03-RESTAPI.git
$ cd SideProject03-RESTAPI
```
建立且激活虛擬環境
```
python -m venv venv
source ./venv/Scripts/activate
```
下載依賴套件
```
pip install -r requirements.txt
```
在本地端的 Mysql 建立一個名稱為 demo 的資料庫, 修改 DATABASE_URI
```
'mysql+pymysql://你的帳號:你的密碼@localhost:3306/demo'
```
建立資料庫資料表
```
flask db init
flask db migrate
flask db upgrade
```
建立管理員帳號密碼，帳號密碼自己決定
```
flask admin
```
啟動
```
flask run
```
# 參考資源
<ul>
  <li>Flask REST APIs入門與實戰, Peng Xiao </li>
  <li>REST APIs with Flask and Python, Jose</li>
  <li>Flask 入門教程, 李輝</li>
  <li>Flask Web 開發實戰, 李輝</li>
</ul>


