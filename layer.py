import logging

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity

from bot import reader

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        # send receipt otherwise we keep receiving the same message over and
        # over

        if True:
            receipt = OutgoingReceiptProtocolEntity(
                messageProtocolEntity.getId(),
                messageProtocolEntity.getFrom(),
                'read',
                messageProtocolEntity.getParticipant()
            )
            message = reader(messageProtocolEntity.getBody())
            def send_text_message(body):
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    body,
                    to=messageProtocolEntity.getFrom())
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
            if isinstance(message, list):
                for part in message:
                    send_text_message(part)
            else:
                send_text_message(message)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(
            entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
