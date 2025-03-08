from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from ayaka_ms_orchestrator.Utils.CassandraMethods import DBGetUserByLineId
from ayaka_utils.Defs.pprint import pprint

load_dotenv()

# Example usage - Lookup a user by LineId:
if __name__ == "__main__":

    # Set up the secure connect bundle and credentials
    cloud_config = {'secure_connect_bundle': os.getenv("CASSANDRA_SECURE_BUNDLE_PATH")}
    CLIENT_ID = os.getenv("CASSANDRA_RW_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CASSANDRA_RW_CLIENT_SECRET")
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect(os.getenv("CASSANDRA_KEYSPACE"))

    # Example: Lookup a user by LineId
    user = DBGetUserByLineId(session, os.getenv("DEBUGGING_LINE_ID"))
    pprint(
        f"User ID: {user['id']} – ",
        f"Name: {user['preferred_name']} – ",
        f"Active Conversation: {user['active_conversation']}"
        )

    # # Example using the runnable lambda version:
    # add_message_runnable = RAddMessage(session, "cid=1", "uid=99", "This message was added via lambda.", message_time)
    # # When ready, execute the lambda:
    # lambda_timeuuid = add_message_runnable()
    # print("Lambda inserted message with timeuuid:", lambda_timeuuid)

    cluster.shutdown()
