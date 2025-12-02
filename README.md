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
Module: 代表獨立、可重複的元件，例如 .btn, .nav <br>
State: 元素狀態，例如 .active, .disabled <br>
Theme: 元素的顏色、字體等主題，例如 .theme-dark, .theme-light <br>
<strong>BEM:</strong>
<br>
Q2-2: Tell us which naming guideline is your favorite, and give an example to demonstrate the main concept of that guideline. For example, you can demo how to apply the OOCSS naming guideline to the CSS code in our week 1 tasks. <br>
A2-2:
<br>

## Task3- Fetch and CORS 
Using built-in JavaScript fetch function, we can send HTTP requests to the back-end and get HTTP responses without refreshing or redirecting the page. Cross Origin Resource Sharing (CORS) concept plays a critical role if we want to send a request to a different domain with the fetch function.
Q3-1: What is CORS? <br>
A3-1: 

Q3-2: Can we use the fetch function in our localhost page, to send a request to https://www.google.com/ and get a response? <br>
A3-2:

Q3-3: Can we use the fetch function in our localhost page, to send a request to https://cwpeng.github.io/test/assignment-3-1 and get a response? Compared to the previous case, what’s the difference? <br>
A3-3:

Q3-4: How to share APIs we developed to other domains, just like what we experienced in step 3. Could you give us an example? <br>
A3-4:

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

