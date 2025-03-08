import os

from cassandra.cluster import Cluster
from ayaka_ms_orchestrator.Utils.CassandraMethods import create_new_conversation

from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
load_dotenv()

# Example usage - create a new conversation
if __name__ == "__main__":
    # Set up your secure connect bundle and credentials (adjust paths as needed)
    cloud_config = {'secure_connect_bundle': os.getenv("CASSANDRA_SECURE_BUNDLE_PATH")}
    CLIENT_ID = os.getenv("CASSANDRA_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CASSANDRA_CLIENT_SECRET")

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    # Connect to your keyspace (replace 'userprofilesks' with your keyspace name)
    session = cluster.connect(os.getenv("CASSANDRA_KEYSPACE"))
    
    # Define a list of participant user IDs (as stored in your users table)
    participants = ['uid=0', 'uid=h']  # update this list as needed

    new_conv_id = create_new_conversation(session, participants)
    print("New conversation created with ID:", new_conv_id)
    
    cluster.shutdown()