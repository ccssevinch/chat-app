Chat App Database Documentation (MySQL)

This document explains the MySQL database structure, queries, and logic used in the chat application.


<h2>1. Database Schema</h2>
<h3>Users Table</h3>
Stores registered users and their credentials

```sql
CREATE TABLE Users (
    id INT NOT NULL AUTO_INCREMENT, 
    username VARCHAR(50) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL, 
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY(id),
    UNIQUE KEY username (username),
    UNIQUE KEY email (email)
)
 ```
<h3> Contacts Table</h3>
```sql
id INT NOT NULL AUTO_INCREMENT, 
user_id INT NOT NULL, 
contact_id INT NOT NULL, 
added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
is_blocked BOOLEAN DEFAULT FALSE,
PRIMARY KEY (id),
UNIQUE KEY (user_id, contact_id)
FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
FOREIGN KEY (contact_id) REFERENCES Users(id) ON DELETE CASCADE
);
```


<h3>Messages Table</h3>
<h4>Stores both private and group messages</h4>

```sql
CREATE TABLE Messages (
    id INT NOT NULL AUTO_INCREMENT, 
    sender_id INT DEFAULT NULL, 
    receiver_id INT DEFAULT NULL, -- NULL for group messages
    message_text TEXT NOT NULL, 
    sent_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    status ENUM('sent', 'delivered', 'read') DEFAULT 'delivered',
    is_private TINYINT(1) DEFAULT '0',
    group_id INT DEFAULT NULL, 
    PRIMARY KEY (id),
    KEY sender_id (sender_id),
    KEY receiver_id (receiver_id),
    CONSTRAINT messages_ibfk_1 FOREIGN KEY (sender_id) REFERENCES Users (id) ON DELETE SET NULL, 
    CONSTRAINT messages_ibfk_2 FOREIGN KEY (receiver_id) REFERENCES Users (id) ON DELETE SET NULL
)
```

<h3>Groups or Group Chats Table</h3>
<h4>Stores all group chats created by users</h4>

```sql
CREATE TABLE Group_Chats (
    id INT NOT NULL AUTO_INCREMENT, 
    group_name VARCHAR(100) NOT NULL, 
    created_by INT DEFAULT NULL, 
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (id),
    UNIQUE KEY group_name (group_name),
    KEY created_by (created_by), 
    CONSTRAINT group_chats_ibfk_1 FOREIGN KEY (created_by) REFERENCES Users (id) ON DELETE RESTRICT
)
```

<h3>Group Members Table</h3>
<h4>Tacks which users belong to which groups</h4>

```sql
CREATE TABLE Group_Members (
    id INT NOT NULL AUTO_INCREMENT,
    group_id INT DEFAULT NULL, 
    user_id INT NOT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_admin BOOLEAN DEFAULT FALSE,
    muted BOOLEAN DEFAULT FALSE,
    last_seen DATETIME NULL,
    is_typing BOOLEAN DEFAULT FALSE,
    timed_chat_expiry DATETIME NULL,
    PRIMARY KEY (id),
    UNIQUE KEY group_id (group_id, user_id),
    KEY user_id (user_id),
    CONSTRAINT group_members_ibfk_1 FOREIGN KEY (group_id) REFERENCES Group_Chats (id) ON DELETE SET NULL, 
    CONSTRAINT group_members_ibfk_2 FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE
)
```

<h3>Message Status Table</h3>
<h4>Tracks whether a message has been read</h4>

```sql
CREATE TABLE Message_Status (
    id INT NOT NULL AUTO_INCREMENT, 
    message_id INT DEFAULT NULL, 
    user_id INT DEFAULT NULL, 
    is_read TINYINT(1) DEFAULT '0', 
    read_at TIMESTAMP NULL DEFAULT NULL, 
    PRIMARY KEY (id), 
    KEY user_id (user_id), 
    KEY message_status_ibfk_1 (message_id),
    CONSTRAINT message_status_ibfk_2 FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE SET NULL
)
```

<h2>2. Important Queries</h2>
<h3>Insert a User</h3>

```sql
INSERT INTO Users (username, email, password_hash)
VALUES ('john_doe', 'john@eexample.com', 'hashed_pasword');
```
<h3>Insert a Private Message</h3>

```sql  
INSERT INTO Messages (receiver_id, sender_id, message_text, is_private)
VALUES (38, 47, 'Hello, this is a private message.', TRUE);
```
<h3>Insert a Group Message</h3>

```sql 
INSERT INTO Messages (group_id, sender_id, message_text, is_private)
VALUES (5, 47, 'Hello, group!', FALSE);
```
<h3>Find All Messages Sent to a Group</h3>

```sql  
SELECT id AS message_id, sender_id, message_text, sent_at
FROM messages
WHERE group_id = 6
ORDER BY sent_at DESC;
```
<h3>Find Members of a Group</h3>

```sql
SELECT user_id 
FROM group_members
WHERE group_id = 6; 
```
<h3>Check Who Has Read a Message</h3>

```sql
SELECT ms.message_id, u.username, ms.is_read, ms.read_at
FROM message_status ms
JOIN Users u ON ms.user_id = u.id
WHERE ms.message_id = 6;
```
<h2>3. Triggers & Business Logic</h2>
<h3>Trigger: Automatically Insert Message Status</h3>

<h4>after_insert_message_status trigger ensures two main things</h4>

<h4>1. It inserts a corresponding read status (Message_Status) for every new message.</h4>
<h4>It determines whether the message should go into a group chat or a private chat before allowing inserting</h4>

```sql
CREATE TRIGGER after_insert_message_status
AFTER INSERT ON Messages
FOR EACH ROW
BEGIN
    IF NEW.group_id IS NOT NULL AND NEW.receiver_id IS NULL THEN
        IF NOT EXISTS (SELECT 1 FROM Group_Chats WHERE id = NEW.group_id) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cannot insert messages into a deleted group';
        END IF;

        INSERT INTO Message_Status (message_id, user_id, is_read, read_at)
        SELECT NEW.id, user_id, FALSE, NULL FROM Group_Members WHERE group_id = NEW.group_id;

    ELSEIF NEW.receiver_id IS NOT NULL AND NEW.group_id IS NULL THEN
        INSERT INTO Message_Status (message_id, user_id, is_read, read_at)
        VALUES (NEW.id, NEW.receiver_id, FALSE, NULL);
    
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Message must have either a group_id or a receiver_id.';
    END IF;
END;
```


**For a detailed breakdown of how this trigger works, see [TRIGGER_BREAKDOWN.md](TRIGGER_BREAKDOWN.md).**













