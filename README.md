<h2>Chat Application</h2>

A real-time chat application built using Flask, Flask-SocketIO, HTML, CSS, and JavaScript. This project allows multiple users to exchange messages in a shared char room, showcasing bidirectional communication with WebSocket.

<h2>Features</h2>

- Real-time messaging across all connected clients.
- A single chat room where multiple users can join.
- Simple and responsive frontend interface.

<h2>Upcoming Features</h2>

I am currently working on adding the following features to improve the application:

<h3>Backend</h3>

<h3>Secure Authentication</h3>

 - User registration, login, JWT-based authentication.

<h3>Real-Time Messaging</h3>

- Instant one-on-one and group chats with WebSockets.

<h3>Chat History and Storage</h3>

- Messages saved in MySQL for easy retrieval

<h3>Message Status Updates</h3>

- Delivered and read receipts for messages

<h3>Group Chat Support</h3>

- Create, join, and leave groups with message history

<h3>Optimized Performance</h3>

- Flask-SocketIO, MySQL indexing, and caching

<h3>Security Enhancements</h3>

- Password Hashing, JWT protection, and CORS settings

<h3>Deployment Ready</h3>

- AWS Lambda Configuration (Serverless Deployment)

<h3>Frontend</h3>

<h3>Intuitive Chat</h3>

- Clean, responsive design with message bubbles

<h3>Notifications and Mentions</h3>

- Notifications for new messages and tagged mentions

<h3>Typing Indicator</h3>

- Show when a user is typing a message

<h3>Pinned Messages</h3>

- Keep important messages at the top

<h3>Dark Mode</h3>

- Toggle between light and dark themes

<h2>Tools and Technologies</h2>

- Backend: Flask and Flask-SocketIO
- Frontend: HTML, CSS, JavaScript
- WebSocket Protocol: For real-time, bidirectional communication

**Project Structure**

chat-app/

│

├── app.py          # Main backend Flask application

└── index.html      # Frontend HTML with embedded CSS and JavaScript


<h2>Install Dependencies</h2>

pip3 install flask flask-socketio 

<h2>Run the Application</h2>

python app.py

<h2>Open in Browser</h2>

Navigate to http://127.0.0.1:5000/ in your broswer to use the application.

<h2>How It Works</h2>

<h3>Backend:</h3>
- Flask handles routing and serves the frontend HTML.
- Flask-SocketIO enables WebSocket support for real-time communication.
- Defines WebSocket events for sending and receiving messages.

<h3>Frontend:</h3>

- HTML provides the structure of the chat interface.
- CSS styles the application for a clean, responsive layout.
- JavaScript manages WebSocket communication and dynamically updates the chat interface. 

<h2>Communication Workflow</h2>

1. A user enters a username and message and clicks "Send".
2. The username and message is sent to the backend using WebSocket(send_message event).
3. The backend processes the username and message and broacasts it to all connected clients (receive_message event).
4. All clients display the new username and message in their chat interface.

<h2>Dependencies</h2>

- Flask
- Flask-SocketIO
  
<h2>Testing</h2>

- Open the application in multiple browser tabs or windows.
- Send messages from one tab and observe them appearing in real time in all connected tabs.
- Check the server terminal for debugging logs (e.g., "Message received").

<h2>Command to Install Dependencies</h2>
  
  pip3 install -r requirements.txt

<h2>Acknowledgments</h2>

- Flask documentation: https://flask.palletsprojects.com/
- Flask-SocketIO documentation: https://flask-socketio.readthedocs.io/


<h4>Stay tuned for more updates as I work on new features!</h4>













