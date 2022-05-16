// ==UserScript==
// @name         George：网站 hifini.com 自动签到
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  网站 hifini.com 自动签到
// @author       George
// @match        *www.hifini.com/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function()
 {
    function enterCourse()
    {
        console.log("自动签到");
        var dom = document.getElementById('sg_sign');
        if (!!dom)
        {
            console.log("找到签到按钮");
            var sign = document.getElementById('sign');
            if (!!sign)
            {
                var text = sign.innerText;
                console.log("文字："+text);
                if(text=="已签"){
                    console.log("已经签到");
                }else{
                    dom.click();
                }
            }
        }}

    enterCourse();
})();