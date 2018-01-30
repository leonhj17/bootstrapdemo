/**
 * Created by Thinkpad on 2018/1/30.
 */
function multiple(num1,num2) {
    result = num1*num2;
    alert(result);
};
function showPic(whichPic) {
    var source = whichPic.getAttribute("href");
    var placeholder = document.getElementById("placeholder");
    placeholder.setAttribute("src",source);
};