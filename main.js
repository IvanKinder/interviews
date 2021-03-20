"use strict";

let socket = new WebSocket("ws://127.0.0.1:5678");

socket.onopen = function () {
    document.getElementById("button").onclick = function () {
        socket.send(document.getElementById("1").value);
    };
};

socket.onerror = function () {
    console.log('Ошибка при подключении');
};

socket.onmessage = function (e) {
    alert(e.data)
};