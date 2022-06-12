const roomName = JSON.parse(document.getElementById('room-name').textContent);
const user = JSON.parse(document.getElementById('user').textContent);
const conversation=document.getElementById("conversation")
console.log(roomName)
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log("message:"+data.message)
    console.log(data.created_date)
    console.log(user)
    if (user === e.data.user){
        var message=`<div class="row message-body">
                <div class="col-sm-12 message-main-sender">
                    <div class="sender">
                        <div class="message-text">
                            ${data.message}
                        </div>
                        <span class="message-time pull-right">
                            ${data.created_date}
                        </span>
                    </div>
                </div>
            </div>`
    }else{
        var message=`<div class="row message-body">
                <div class="col-sm-12 message-main-receiver">
                    <div class="receiver">
                        <div class="message-text">
                            ${data.message}
                        </div>
                        <span class="message-time pull-right">
                            ${data.created_date}
                        </span>
                    </div>
                </div>
            </div>`
    }
    conversation.innerHTML += message
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#comment').focus();

document.querySelector('#comment').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#send').click();
    }
};

document.querySelector('#send').onclick = function(e) {
    const messageInputDom = document.querySelector('#comment');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};