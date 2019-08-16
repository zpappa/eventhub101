from common import Settings
from azure.eventhub import EventHubClient, EventData


class EventHubService:
    def __init__(self):
        connection_string = "Endpoint=sb://{}/;SharedAccessKeyName={};SharedAccessKey={};EntityPath={}".format(
            Settings.eh.hostname,
            Settings.eh.sas_policy,
            Settings.eh.sas_key,
            Settings.eh.event_hub_name)
        self.client = EventHubClient.from_connection_string(connection_string)
        self.sender = self.client.add_sender(partition="0")
        self.client.run()

    def stop(self):
        self.client.stop()

    def send(self, message):
        try:
            print("Sending: "+message)
            self.sender.send(EventData(body=message))
        except Exception as e:
            print(e)
            self.client.stop()