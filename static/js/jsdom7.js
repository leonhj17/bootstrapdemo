/**
 * Created by Thinkpad on 2018/2/7.
 */
document.write("<p>this is inserted.</p>");

window.onload = function () {
    var testdiv = document.getElementById("testdiv");
    testdiv.innerHTML = "<P>I inserted <em>this</em> content.</P>"
};