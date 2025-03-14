<h1>Activity Diagram</h1>

<h4> The WebSocket Activity Diagram 

Detailed Explanation:
- When a user logs in, a WebSocket connection is established
- The message is sent via WebSocket and stored in the database
- If the recipient is online, the message is delivered instantly
- If the recipient is offline, the message is stored and sent upon reconnection
 

![Websocket Activity Diagram](activity_diagram.png)

</h4>
