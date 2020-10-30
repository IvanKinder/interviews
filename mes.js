"use strict";

let socket = new WebSocket("ws://127.0.0.1:5678");
let flag = new Date();

socket.onopen = function () {
    socket.send("message_from_user");
    document.querySelector("textarea").addEventListener('keyup', function (e) {
        if (e.keyCode === 13) {
            if (this.value.trim() === "") {
                return false;
            }
            socket.send("message_from_user;" + document.getElementById("who").value + ";" + this.value.trim());
            this.value = "";
        }
    });
};

socket.onerror = function () {
    console.log('Ошибка при подключении');
};

let p = "";
let signal = new Audio();
signal.src = "signal.mp3";
socket.onmessage = function (e) {
    if (e.data == "refresh") {
        document.location.href = "index.html";
    }
    else {
        p = document.createElement("p");
        p.innerHTML = e.data;
        document.querySelector(".message").appendChild(p);
        signal.play();
    }
};

