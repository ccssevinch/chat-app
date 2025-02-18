<h3>Breakdown of How the Trigger Works</h3>

<h5>Ensures the Message is Being Sent to a Valid Group</h5>

```sql
IF NEW.group_id IS NOT NULL AND NEW.receiver_id IS NULL THEN
```

This checks if the message is meant for a group.

It ensures that the message is NOT also linked to a receiver_id (which would mean a private message).


<h5>Prevents Messages from Being Sent to Deleted Groups</h5>

```sql
IF NOT EXISTS (SELECT 1 FROM Group_Chats WHERE id = NEW.group_id) THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Cannot insert messages into a deleted group';
END IF;
```


Ensures that a group_id actually exists in Group_Chats

If the group was deleted, it blocks the insert and throws an error.

Users can still view past messages or chat history but can not insert new messages.

This prevents orphaned messages (messages with a group_id that no longer exists).



<h5>Automatically Inserts Read Status for Group Members</h5>


```sql
INSERT INTO Message_Status (message_id, user_id, is_read, read_at)
SELECT NEW.id, user_id, FALSE, NULL FROM Group_Members group_id = NEW.group_id;
```


Automatically adds a read status for every group member.

Marks all messsages as unread (is_read = FALSE) when first inserted.

Ensures group messages are delivered to all group members



<h5>Ensures the Message is Being Sent as a Private Message (One-on-One)</h5>


```sql
ELSEIF NEW.receiver_id IS NOT NULL AND NEW.group_id IS NULL THEN
```

Checks if the message is for a one-on-one chat.

Ensures that group_id IS NULL to avoid conflicts (message can't belong to both a private and group chat).



<h5>Inserts Read Status for Private Messages</h5>


```sql
INSERT INTO Message_Status (message_id, user_id, is_read, read_at)
VALUES (NEW.id, NEW.receiver_id, FALSE, NULL);
```

Ensures the private message gets an unread (is_read = FALSE) status.

Automatically tracks message delivery for one-on-one chats.



<h5>Prevents Invalid Messages (If Neither a group_id Nor a receiver_id is Set)</h5>


```sql
ELSE
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Message must have either a group_id or a receiver_id,';
END IF;
```


Prevents the message form being inserted if it's missing both group_id and receiver_id.

Ensures every message has a clear destination (either a private chat or a group).







