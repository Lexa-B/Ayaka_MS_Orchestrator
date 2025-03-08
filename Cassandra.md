# Frequent Operations
## Use the userprofilesks keyspace
USE ayaka_sks;

## Users
### Get all users with their preferred name and active conversation
SELECT uid, preferred_name, active_conversation FROM users LIMIT 100;

### Get all users with their preferred name and LINE ID
SELECT uid, preferred_name, lineid FROM users LIMIT 100;

## Conversations
### Get all users in a conversation
SELECT * FROM conversation_users LIMIT 100;

### Get all messages in a conversation
SELECT * FROM conversation_messages WHERE conversation_id = 'cid=4' LIMIT 100;

### Get all conversations for a user
SELECT * FROM user_conversations LIMIT 100;

### Delete all messages in a conversation
DELETE FROM conversation_messages WHERE conversation_id = 'cid=0';

### Delete all users in a conversation
DELETE FROM conversation_users WHERE conversation_id = 'cid=0';

### Delete a conversation for a user
DELETE FROM user_conversations WHERE user_id = 'uid=#' AND conversation_id = 'cid=#';

### Delete specific message in a conversation
DELETE FROM conversation_messages WHERE conversation_id = 'cid=4' AND message_time = '98fae668-fbcb-11ef-9e8e-b2b06724f49f';

### Get the messages in a conversation sorted by timestamp
SELECT dateof(message_time) AS message_timestamp, sender_id, message FROM conversation_messages WHERE conversation_id = 'cid=0';

### Update the active conversation for a batch of users
BEGIN BATCH
  UPDATE users SET active_conversation = 'cid=5' WHERE uid = 'uid=h';
  UPDATE users SET active_conversation = 'cid=0' WHERE uid = 'uid=0';
  UPDATE users SET active_conversation = 'cid=0' WHERE uid = 'uid=4';
APPLY BATCH;

### Update the LINE ID for a user
UPDATE users
SET LineId = '###'
WHERE uid = 'uid=#';

### Null-out the LINE ID for a user
UPDATE users
SET LineId = null
WHERE uid = 'uid=#';
