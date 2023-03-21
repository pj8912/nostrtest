import json 
import ssl
import time

from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.message_type  import ClientMessageType
from nostr.key import PrivateKey


relay_manager = RelayManager()
relay_manager.add_relay("wss://nostr-pub.wellorder.net")
relay_manager.add_relay("wss://relay.damus.io")
relay_manager.open_connections("{cert_reqs" : ssl.CERT_NONE})
time.sleep(1.25)
private_key  = PrivateKey()

event = Event("Hello Nostr")
private_key.sign_event(event)

relay_manager.publish_event(event)

time.sleep(1) 

relay_manager.close_connections()


