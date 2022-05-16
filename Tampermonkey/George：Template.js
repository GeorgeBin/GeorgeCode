// ==UserScript==
// @name         George：xxx
// @version      0.1
// @description  xxx
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @match        https://xxx/*
// @author       George
// @namespace    http://tampermonkey.net/
// @license      MIT
// @grant        none
// ==/UserScript==


(function() {
    'use strict';

    console.log("脚本运行");

    // -------------------- 生命周期 --------------------

    // 页面加载完成
    window.onload=function(){
        console.log("onload");



        // ---------- 全局功能 ----------
        window.print();// 触发打印



        // ---------- 常用语句 ----------

        // title
        console.log(document.title); // 获取title
        document.title = '需要设置的值'; // 设置title
        document.getElementsByTagName("title")[0].innerText = format; // 设置title（方式2）

        var view1 = document.getElementsByClassName("header-container")[0].style.display = 'none';// 隐藏控件
        if (!!view1)// 判断是否为空
        {
            var text = view1.innerText; // 获取控件内容
            console.log("内容："+text); // 打印log
        }

        // 新控件
        var cloneView = view1.cloneNode(true); // 克隆节点
        var printBtn = document.createElement("div");// 手动创建节点
        // 设置各种属性
        printBtn.setAttribute("_ngcontent-vuw-c81","");// 空的属性
        printBtn.setAttribute("class","like");
        printBtn.title="收藏";
        printBtn.id="HtmToPDF";



        // ---------- 调用：通用方法 ----------
        // 日期格式化
        var date = new Date();
        var format = dateFormat('yyyy.mm.dd',date);
        console.log("时间："+format);
    };

    // 页面加载完成
    window.onfocus = function () {
        document.title = '恢复正常了...';
    };

    // 失去焦点（例如）
    window.onblur = function () {
        document.title = '快回来~页面崩溃了';
    };



    // -------------------- 通用方法 --------------------

    // 日期格式化
    function dateFormat(fmt, date) {
        let ret;
        const opt = {
            "y+": date.getFullYear().toString(), // 年
            "m+": (date.getMonth() + 1).toString(), // 月
            "d+": date.getDate().toString(), // 日
            "h+": date.getHours().toString(), // 时
            "M+": date.getMinutes().toString(), // 分
            "s+": date.getSeconds().toString() // 秒
            // 有其他格式化字符需求可以继续添加，必须转化成字符串
        };
        for (let k in opt) {
            ret = new RegExp("(" + k + ")").exec(fmt);
            if (ret) {
                fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
            };
        };
        return fmt;
    }

    // 触发打印
    function gotoPrint() {
        window.print();
    };
})();