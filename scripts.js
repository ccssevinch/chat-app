const socket = io();

// Elements 
const messagesDiv = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');


// Send message to the server
sendButton.addEventListener('click', () => {
    const message = messageInput.value; 
    if (message) {
        socket.emit('send_message', { text: message });
        messageInput.value = '';
    }
});

// Receive message from the server
socket.on('receive_message', (data) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = data.text;
    messagesDiv.appendChild(messageElement);
})
