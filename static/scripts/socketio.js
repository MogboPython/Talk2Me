document.addEventListener('DOMContentLoaded', ()=>{
    var socket = io();

    socket.on('connect', ()=>{
        socket.send("I am connected");
    });

    socket.on('message', data =>{
        console.log(`Message recieved: ${data}`);
    });
    socket.on('Some-event', data =>{
        console.log(data);
    });
})