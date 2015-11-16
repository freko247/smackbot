import logging

from layer import EchoLayer
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks import YowAckProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup import env

from settings import whatsapp_phone, whatsapp_password

logging.basicConfig(filename='yowsup.log', level='INFO')

CREDENTIALS = (whatsapp_phone, whatsapp_password)

if __name__ == "__main__":
    while 1:
        layers = (
            EchoLayer,
            (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer,
             YowReceiptProtocolLayer, YowAckProtocolLayer)
        ) + YOWSUP_CORE_LAYERS

        stack = YowStack(layers)
        # setting credentials
        stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)
        # whatsapp server address
        stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
        stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
        # info about us as WhatsApp client
        stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())

        # sending the connect signal
        stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

        stack.loop()  # this is the program mainloop
