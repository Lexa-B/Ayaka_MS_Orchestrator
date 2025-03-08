from datetime import datetime

from cassandra.cluster import Cluster
from ayaka_ms_orchestrator.Utils.CassandraMethods import DBAddMessageCass

from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
import os

load_dotenv()

# Example usage - Add a new message to conversation 'cid=1':
if __name__ == "__main__":
    # Set up your secure connect bundle and credentials (adjust paths as needed)
    cloud_config = {'secure_connect_bundle': os.getenv("CASSANDRA_SECURE_BUNDLE_PATH")}
    CLIENT_ID = os.getenv("CASSANDRA_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CASSANDRA_CLIENT_SECRET")
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    # Connect to your keyspace (replace 'userprofilesks' with your keyspace name)
    session = cluster.connect(os.getenv("CASSANDRA_KEYSPACE"))

    # Example: Adding a new message to conversation 'cid=1'
    # Suppose the message was sent on March 6, 2025 at 12:34:56 UTC.
    message_time = datetime(2025, 3, 6, 12, 34, 56)
    new_timeuuid = DBAddMessageCass(session, "cid=1", "uid=99", "Hello, this is a test message.", message_time)
    print("New message inserted with timeuuid:", new_timeuuid)

    # # Example using the runnable lambda version:
    # add_message_runnable = RAddMessage(session, "cid=1", "uid=99", "This message was added via lambda.", message_time)
    # # When ready, execute the lambda:
    # lambda_timeuuid = add_message_runnable()
    # print("Lambda inserted message with timeuuid:", lambda_timeuuid)

    cluster.shutdown()