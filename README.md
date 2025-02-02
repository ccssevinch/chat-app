**Chat Application**

A real-time chat application built using Flask, Flask-SocketIO, HTML, CSS, and JavaScript. This project allows multiple users to exchange messages in a shared char room, showcasing bidirectional communication with WebSocket.

**Features**

- Real-time messaging across all connected clients.
- A single chat room where multiple users can join.
- Simple and responsive frontend interface.

**Tools and Technologies**

- Backend: Flask and Flask-SocketIO
- Frontend: HTML, CSS, JavaScript
- WebSocket Protocol: For real-time, bidirectional communication

**Project Structure**
chat-app/
│
├── app.py          # Main backend Flask application
└── index.html      # Frontend HTML with embedded CSS and JavaScript

**Install Dependencies**

pip3 install flask flask-socketio 

**Run the Application**

python app.py

**Open in Browser**

Navigate to http://127.0.0.1:5000/ in your broswer to use the application.

**How It Works**

Backend:
- Flask handles routing and serves the frontend HTML.
- Flask-SocketIO enables WebSocket support for real-time communication.
- Defines WebSocket events for sending and receiving messages.

**Frontend:**

- HTML provides the structure of the chat interface.
- CSS styles the application for a clean, responsive layout.
- JavaScript manages WebSocket communication and dynamically updates the chat interface. 

**Communication Workflow:**

1. A user enters a username and message and clicks "Send".
2. The username and message is sent to the backend using WebSocket(send_message event).
3. The backend processes the username and message and broacasts it to all connected clients (receive_message event).
4. All clients display the new username and message in their chat interface.

**Dependencies**

- Flask
- Flask-SocketIO
  
**Testing**

- Open the application in multiple browser tabs or windows.
- Send messages from one tab and observe them appearing in real time in all connected tabs.
- Check the server terminal for debugging logs (e.g., "Message received").

**Command to Install Dependencies**
  
  pip3 install -r requirements.txt

**Acknowledgments** 

- Flask documentation: https://flask.palletsprojects.com/
- Flask-SocketIO documentation: https://flask-socketio.readthedocs.io/

















