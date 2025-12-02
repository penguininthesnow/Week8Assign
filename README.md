# Week8Assign
第一階段研究專案(week8)

## Task1 - HTML <script> Attributes  
There are 2 attributes, defer and async , that we can use in <script> tag to change the script loading and executing behavior.
Q1-1: What happens if we add a "defer" attribute to a <script>tag? <br>
A1-1: Deferred(延遲的)，defer會告訴瀏覽器，不用等腳本下載與執行，可以繼續完成HTML的解析和DOM的建構; 也就是說在建構的同時，會在背景中載入腳本，因此他不會擋住畫面的渲染。倘若今天腳本在HTML解析完成前就先下載好，那他也會等到HTML解析完成後才會執行，也就是說如果有腳本需要等HTML解析完，DOM完整建立才能載入，那麼會需要選defer。 另一個情境是: 如果今天同時帶有多個defer屬性，瀏覽器會同步下載，只是會依照在HTML中的順序執行，確保在執行時是我們要的順序，有時是某一腳本A依賴某一腳本B時，要確保A是在B之前執行，這實業會選用defer。

Q1-2: What happens if we add a "async" attribute to a <script>tag? <br>
A1-2: 全名-asynchrnous，意即非同步，換句話說解析HTML與腳本載入，是非同步進行的。因此歲然同樣會告訴瀏覽器不用等腳本下載與執行，可以繼續完成HTML的解析和DOM的建構，但跟defer不一樣在於，async腳本載入與HTML解析，兩者屬性是彼此獨立的，因此只要下載完成就會馬上執行，而不是像defer那樣要等HTML解析完才執行，有點自己做自己的事情的感覺...
再來是，除了腳本載入與解析是彼此獨立之外，帶有async屬性的腳本跟其他腳本也是彼此獨立的，哪個先下載完成就那個先執行，雖然下載時不會暫停HTML解析的動作，但如果是在執行時腳本就會跟著暫停解析了，所以通常會用在腳本之間比較沒有依賴關係的，例如Google Analytics

Q1-3: When to use these 2 attributes? Could you give us code examples to illustrate the use cases for these 2 attributes? <br>
A1-3: 先講歷史沿革部分，在以前defer、async還沒出來的年代，當瀏覽器在解析HTML時，只要遇到<script>標籤就會走以下程序，1.停止解析 2.對src發起請求 3.等待 4.執行回應腳本或是請求失敗Exception 5.繼續向下解析，也就是說當遇到<script>標籤時，就會先停下手邊建構DOM的工作，開始載入<script>腳本資源，並執行下載好的腳本，直到下載完並執行完畢，才會繼續DOM的建構。
而這樣就會有兩難局面，就是說如果今天我們把 <script> 標籤順序擺比較上面，則可能導致如果腳本較肥大，要載入比較久的時間，進而導致畫面比較晚才被渲染出來，這也是為什麼許多人傾向把<script>標籤放在最下面，然而如果這麼做則會導致當畫面渲染完之後，還要等script裡的內容載入與執行完，這會讓畫面是呈現渲染出來得樣子，但是沒辦法有功能，因此有了async與defer的誕生。這兩個屬性都是在跟瀏覽器說，不用等腳本載入，繼續建構DOM，這樣不只讓兩邊同步進行，也能讓使用者使用體驗更好。<br>
A1-3-2: 用week7做示範 

## Task2 - CSS Selector Naming 
OOCSS, SMACSS, and BEM are 3 common naming guidelines for CSS Selector. These guidelines help us write more readable CSS code.
Q2-1: Introduce the concepts of OOCSS, SMACSS, and BEM naming guidelines. <br>
A2-1: <strong>OOCSS:</strong>全名為Object Oriented CSS，類似積木的概念，我們要將CSS寫成一個個可以獨立拆開的積木(耦合:兩個模組間的相依性，業就是要寫出低耦合的CSS，方便未來的擴展彈性)，而其中最主要的代表框架就是Bootstrap，其中主要概念就是1.結構與樣式分離:獨立出結構和樣式後，我們就可以重複套用在其他按鈕上，不需要在其他不同按鈕上又寫不一樣的code
```/* 原本寫法是 */
.btn-login{
  padding:20px;
  border-radius:5px solid;
  background-color:blue;
}
/*獨立出結構*/
.btn{
  padding:20px;
  border-radius:5px solid;
}
/*獨立出樣式*/
.btn-primary{
  background-color:blue;
}
```
2.容器與內容分離:就是在沒一個容器裡抽出一樣得樣式，然後統一寫在一個css裡面
```/* 原本寫法: */
header{
  max-width: 1500px;
  margin:20px 40px;
  background-color: #aaa;
  ...
}
footer{
  max-width: 1500px;
  margin:20px 40px;
  background-color: #bbb;
}
/*以「容器」獨立出共用部分*/
.container{
  max-width: 1500px;
  margin:20px 40px;
}
/*不一樣的樣式再分開寫*/
header{
  background-color: #bbb;
}
footer{
  background-color: #ccc;
}
```
優點是感覺code好像變得很乾淨，缺點是HTML上的class數量可能會變很多個(如果又再加上很多utilities) <br>
<strong>SMACSS:</strong>全名為「Scalable and Modular Architecture for CSS」，一即可擴展與模組化的設計模式。他將CSS分為Base、Layout、Module、State、Theme五個層級。<br>
  Base: 全域設定，用來定義HTML的基本樣式，例如h1, h2, a... <br>
  Layout: 網頁版面架構，例如.container <br>
  Module: 代表獨立、可重複的元件，也可以說是模組規範，在整個網頁的區塊視為一個個的模組，例如 .btn, .nav <br>
  State: 元素狀態，網頁中有不同的狀態顏色或行為改變所呈現的結果，例如 .active, .disabled <br>
  Theme: 元素的顏色、字體等主題，指網頁外觀的顏色、圖片，例如 .theme-dark, .theme-light <br>
<strong>BEM:</strong>全名是Block Element Modiifier，單字分別拆開來就是
Block: 塊是一個獨立的元件，以小寫字母命名，例如 .header, .menu <br>
Element: 元素是塊的一部分，他們利用兩個下底線「　＿＿　」連接起來，例如　.header_text, .menu_item <br>
Modifier: 用於修改塊或元素的外觀及狀態，通常用兩個破折號「  - - 」連起來，例如 header--dark, menu__item--active
```
.header{   } // 區塊
.header__element{} // 區塊+區塊裡的元件
.header__element--modifier{} // 區塊+區塊裡的元件+狀態
```
<br>而BEM好處就是能一眼看出來這個class是什麼用途的，而反之缺點就是一個class他的命名可能因此變得很長 <br>
Q2-2: Tell us which naming guideline is your favorite, and give an example to demonstrate the main concept of that guideline. For example, you can demo how to apply the OOCSS naming guideline to the CSS code in our week 1 tasks. <br>
A2-2: Maybe is 'BEM'.，因為在瀏覽HTML CODE中這麼多行程式碼下，能夠透過觀察class，就能立馬了解CSS架構，這樣就不用再回去看CSS CODE裡，哪一個Layout、Module等，也能讓團隊都有一個統一的命名規則，讓彼此在看時都能一目了然。
<br>
from week1 tasks
```

```
## Task3- Fetch and CORS 
Using built-in JavaScript fetch function, we can send HTTP requests to the back-end and get HTTP responses without refreshing or redirecting the page. Cross Origin Resource Sharing (CORS) concept plays a critical role if we want to send a request to a different domain with the fetch function. <br>
Q3-1: What is CORS? <br>
A3-1: 中文叫做"來源資源共享"，此機制支持瀏覽器和伺服器之間的安全跨來源請求和數據傳輸，是一種基於HTTP標頭的機制，簡單來說就是當我們訪問一個網站，而這個網站的(圖片、資料或腳本)不存在於同一個伺服器上，這時瀏覽器就會幫我們建立一個HTTP的跨域請求(cross-origin HTTP request)，例如 在A網站要放入一張來源在B網站的圖片，如果沒有CORS，瀏覽器本身的同源政策會阻止這個跨來源的請求發生，用以保護使用者的資訊安全。<br>
(<strong>同源政策:</strong>確保一網站的資源不能隨便干涉或使用來自另一個網站的資料或功能，以保護你的資料不被其他不相干的網站訪問或濫用，而如果沒有這層防護，很可能連個資都會被竊取。)
```
<img src="http://domain-b.com/image.jpg">
```
同源指的是:scheme、domain、port一樣，則會被視為同源，舉例 假如有一個網站是https://micky.com
```
http://micky.com // 不同源，scheme不同
https://hey.micky.com  //不同源，domain不同
https://micky.com:55  // 不同源，port不同
https://micky.com/cash  // 同源
```
有關CORS的設定方式:
分成「簡單請求(simple requests)」以及「預檢請求(preflighted requests)」，除非包含基本請求的條件，如fetch中的(GET/POST/HEAD)或是設定header、Content type等這類以外的，都會是預檢請求;當我們用fetch的(PUT/DELETE/PATCH)
或XMLHttpRequest來存取資料時，瀏覽器都會先發送一個preflighted requests，這個請求目的是確認伺服器端是否有正確設定允許跨網域的HTTP標頭，當這個檢查通過後，真正的請求才會被發送
```
fetch('https://micky.com/img/',{
  method: 'POST',
  headers:{
    'Content-Type': 'application/json',
  }
})
```
而發出的請求可能會長這樣:
```
OPTIONS /img/
Host: micky.com
Origin: https://myweb.com/
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type 
```
如果遇到CORS有問題時，跨域設定常見就是Access-Control-Request-Origin
```
// 如果要允許所有跨域來源的請求，可以用星號
Access-Control-Request-Origin:*
// 如果要允許特定來源的跨域請求，就直接放入該來源
Access-Control-Request-Origin: https://mini.com
```
Q3-2: Can we use the fetch function in our localhost page, to send a request to https://www.google.com/ and get a response? <br>
A3-2: No, because【Access to fetch at 'https://www.google.com/' from origin 'http://localhost:8000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.】
 if we fetch it will have this above message.

Q3-3: Can we use the fetch function in our localhost page, to send a request to https://cwpeng.github.io/test/assignment-3-1 and get a response? Compared to the previous case, what’s the difference? <br>
A3-3: code
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>fetch google test</title>
</head>
<body>
<script>
    fetch("https://cwpeng.github.io/test/assignment-3-1")
        .then(res => res.text())
        .then(data => console.log(data))
        .catch(err => console.error("Error:", err));
</script>
    
</body>
</html>
```
在Terminal先啟動
```
cd C:\Users\USER\Desktop\penguininthesnow\wehelp\week8\Task3
//接著啟動伺服器
python -m http.server 8000
```
google.com不會回傳Access Control Allow Origin，而github.com會回傳Access Control Allow Origin: *

Q3-4: How to share APIs we developed to other domains, just like what we experienced in step 3. Could you give us an example? <br>
A3-4: 在FastAPI設定CORS middleware:
```
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"], #或設定特定網址
  allow_methods=["*"],
  allow_headers=["*"]
)
```

## Task4 - Connection Pool 
The standard procedure to work with databases is: connect, execute SQL statements, and finally close the connection. Connection Pool is a programming technique to make the connection between back-end system and database more stable, and increase overall throughput.
Q3-1: What is Connection Pool? Why do we want to use Connection Pool? <br>
A3-1:

Q3-2: How to create a Connection Pool by the official mysql-connector-python package? <br>
A3-2:

Q3-3: If we want to make database operations, we get a connection from Connection Pool, execute SQL statements, and finally return connection back to the Connection Pool. Demo your code which implements the above procedure. <br>
A3-3:

## Task5 - Cross-Site Scripting(XSS)
Cross-Site Scripting (XSS) is one of the most common attack methods. Try to study the basic concept, replicate the attack steps, and tell us how to prevent this kind of attack from the developer’s view.
Q5-1: What is XSS? <br>
A5-1:

Q5-2: You are a hacker! Design and do a real XSS attack on a web system. Show us your work. <br>
A5-2:

Q5-3: Based on the scenario you did in the previous step, how could it be prevented? <br>
A5-3:

