/**
 * Created by Thinkpad on 2018/1/30.
 */
function multiple(num1,num2) {
    result = num1*num2;
    alert(result);
}

function showPic(whichPic) {
    //获取资源路径
    var source = whichPic.getAttribute("href");
    //获取说明文本位置
    var placeholder = document.getElementById("placeholder");

    placeholder.setAttribute("src",source);
    var text = whichPic.getAttribute("id");
    var description = document.getElementById("pictext");
    description.firstChild.nodeValue = text;
}

function popUp(url) {
    window.open(url, 'popUp', 'width=480px,height=320px');
}

window.onload = preparelinks;
function preparelinks() {
    var links = document.getElementsByTagName("a");
    for (var i = 0; i < links.length; i++) {
        //为class="popup"的a标签，添加onclick方法
        if (links[i].getAttribute("class") == "popup") {
            links[i].onclick = function () {
                //onclick执行popUp函数
                popUp(this.getAttribute("href"));
                return false;
            }
        } else if (links[i].getAttribute("class") != "showpic") {
        } else {
            //onclick执行showPic函数
            links[i].onclick = function () {
                showPic(this);
                return false;
                //return showPic(this);
            };
            links[i].onKeyPress = links.onclick;
        }
    }
}

//页面加载完成后，执行函数
function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != func) {
        window.onload = func;
    }else {
        window.onload = function () {
            oldonload();
            func();
        }
    }
}

//增加条件判断
function showPic(whichpic) {
    if (!document.getElementById("placeholder")) return true;
    var source = whichpic.getAttribute("href");
    var placeholder = document.getElementById("placeholder");
    placeholder.setAttribute("src", source);
    if (!document.getElementById("description")) return false;
    var text = whichpic.getAttribute("id");
    var description = document.getElementById("description");
    description.firstChild.nodeValue = text;
    return false
}