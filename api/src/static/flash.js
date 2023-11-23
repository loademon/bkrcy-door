function closeFlashMessage(event) {
    var div = event.target.parentElement;
    div.style.opacity = "0";
    setTimeout(function () { div.style.display = "none"; }, 600);
}

window.onload = function () {
    var alerts = document.querySelectorAll('.alert');
    for (var i = 0; i < alerts.length; i++) {
        fadeIn(alerts[i], 600);
    }
};

function fadeIn(element, time) {
    var last = +new Date();
    var tick = function () {
        element.style.opacity = +element.style.opacity + (new Date() - last) / time;
        last = +new Date();

        if (+element.style.opacity < 1) {
            (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
        }
    };
    tick();
}