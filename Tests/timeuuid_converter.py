from cassandra.util import datetime_from_uuid1
import uuid

def main():
    print("Please paste your Cassandra TimeUUID:")
    uuid_str = input().strip()
    
    try:
        # Convert string to UUID object
        time_uuid = uuid.UUID(uuid_str)
        
        # Convert TimeUUID to datetime
        timestamp = datetime_from_uuid1(time_uuid)
        
        # Print in human readable format
        print("\nHuman readable timestamp:")
        print(f"UTC: {timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')} UTC")
        
    except ValueError as e:
        print("Error: Invalid UUID format. Please make sure you've pasted a valid TimeUUID.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 