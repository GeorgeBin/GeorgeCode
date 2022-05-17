## Tampermonkey脚本

### 简介：

[Tampermonkey 官方文档](https://www.tampermonkey.net/documentation.php?ext=dhdg)、[HTML](https://www.w3school.com.cn/h.asp)、[JavaScript](https://www.w3school.com.cn/js/index.asp)



### 常用步骤：

1. 声明头：权限、引用、运行时机
2. 在需要的时机，执行代码
3. 通用方法



### 常用：

@run-at

```js
// @run-at document-start
// @run-at document-body
// @run-at document-end
// @run-at document-idle
// @run-at context-menu
```

运行模式：
1. 网页生命周期加载：window.onload

   ```javascript
   window.onload=function(){
       console.log("onload");
       // 要执行的代码
   };
   ```

   > 理论上讲，此回调会在HTML加载完毕后执行，但不能保证网页包含的js等执行完毕

2. 定时执行：[setTimeout](https://www.runoob.com/w3cnote/javascript-settimeout-usage.html)

   ```js
   setTimeout(addButton,5000); // 可以直接传方法名，注意方法名后没有括号
   或：
   setTimeout(function(){ //使用匿名的function
       // 要执行的代码
   },200);
   ```

3. 鼠标右键手动执行

   ```js
   // @run-at context-menu
   ```

4. 网页加载完成后执行

5. 等待某个元素出现：[参考1](https://stackoverflow.com/questions/32412900/modify-elements-immediately-after-they-are-displayed-not-after-page-completely)、[参考2](https://stackoverflow.com/questions/12897446/userscript-to-wait-for-page-to-load-before-executing-code-techniques) 、[waitForKeyElements](https://gist.github.com/BrockA/2625891#file-waitforkeyelements-js) 

   ```js
   1. 添加头：
   // @run-at        document-start
   
   2. 加载后，等待 “.audience-info”
   
   var observer = new MutationObserver(function(mutations) {
       for (var i=0; i<mutations.length; i++) {
           var mutationAddedNodes = mutations[i].addedNodes;
           for (var j=0; j<mutationAddedNodes.length; j++) {
               var node = mutationAddedNodes[j];
             // 判断条件，以及要执行的代码
               if (node.classList && node.classList.contains("audience-info")) {
                   node.firstElementChild.innerHTML = node.firstElementChild.innerHTML
                       .replace(/[\d.]+/g, function(m) { return 2 * m });
                   // don't hog resources any more as we've just done what we wanted
                   observer.disconnect();
                   return;
               }
             
           }
       }
   });
   observer.observe(document, {childList: true, subtree: true});
   ```

4. 其他



### JavaScript

#### 基础：

1. 生命周期
2. 基础功能
3. 其他

#### 控件

1. title：获取、设置 [参考链接](https://segmentfault.com/a/1190000012116616)
2. div
3. 其他



#### 高级：

1. 使用jquery



### jQuery

1. 引入**jQuery**

   ```js
   // @require  	http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js
   ```

2. 避免和网页本身的**jQuery**冲突

   ```js
   this.$ = this.jQuery = jQuery.noConflict(true);
   ```

3. 其他



常用教程：

[HTML](https://www.w3school.com.cn/h.asp)

[JavaScript](https://www.w3school.com.cn/js/index.asp)

