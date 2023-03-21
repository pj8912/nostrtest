import json 
import ssl 
import time
from nostr.relay_manager import RelayManager

relay_manager = RelayManager()
#add relays
relay_manager.add_relay("wss://nostr-pub.wellorder.net")
relay_manager.add_relay("wss://relay.damus.io")

#open connections

relay_manager.open_connections({"cert_reqs":ssl.CERT_NONE})
time.sleep(1.25)

try:
    while relay_manager.message_pool.has_notices():
        notice_msg = relay_manager.message_pool.get_notice()
        print(notice_msg.content)

except KeyboardInterrupt:
    relay_manager.close_connections()




