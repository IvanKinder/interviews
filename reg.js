"use strict";

let socket = new WebSocket("ws://localhost:5678");

socket.onopen = function () {
    document.getElementById("button").onclick = function () {
        socket.send("reg_user_new " + document.getElementById("login").value + " " + document.getElementById("pass").value);
    };
};

socket.onerror = function () {
    console.log('Ошибка при подключении');
};

let p = "";
socket.onmessage = function (e) {
    p = document.createElement("p");
    p.innerHTML = e.data;
    document.querySelector(".message").appendChild(p);
};
