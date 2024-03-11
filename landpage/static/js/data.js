function updateTime() {
    var now = new Date();
    var time = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
    document.getElementById("currentTime").textContent = time;
}

setInterval(updateTime, 1000);
