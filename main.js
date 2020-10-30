"use strict";

let socket = new WebSocket("ws://127.0.0.1:5678");

socket.onopen = function () {
    socket.send("login_user");
    document.getElementById("button").onclick = function () {
        socket.send("login_user;" + document.getElementById("login").value + ";" + document.getElementById("pass").value);
    };
};

socket.onerror = function () {
    console.log('Ошибка при подключении');
};

let p = "";
socket.onmessage = function (e) {
    if (e.data) {
        document.location.href = "messenger.html";
    }
    else {
        p = document.createElement("p");
        p.innerHTML = e.data;
        document.querySelector(".message").appendChild(p);
    }
};
