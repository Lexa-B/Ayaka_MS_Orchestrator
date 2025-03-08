import sys
import os

from cassandra.cluster import Cluster

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from ayaka_ms_orchestrator.Utils.CassandraMethods import DBReadMessagesCass
from ayaka_utils.Defs.pprint import pprint
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
load_dotenv()

# Example usage - Read the 5 most recent messages from conversation 'cid=0':
if __name__ == "__main__":

    cloud_config = {'secure_connect_bundle': os.getenv("CASSANDRA_SECURE_BUNDLE_PATH")}
    CLIENT_ID = os.getenv("CASSANDRA_RW_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CASSANDRA_RW_CLIENT_SECRET")
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect(os.getenv("CASSANDRA_KEYSPACE"))

    # Use DBReadMessagesCass to fetch the 5 most recent messages from conversation 'cid=1'
    messages = DBReadMessagesCass(session, "cid=0", 5)
    print("Most recent messages (direct function):")
    for msg in messages:
        pprint(msg)

    # # Now use the RunnableLambda version:
    # rread = RReadMessages(session)
    # runnable_messages = rread.invoke("cid=0", 5)
    # print("\nMost recent messages (RunnableLambda):")
    # for msg in runnable_messages:
    #     print(msg)

    cluster.shutdown()