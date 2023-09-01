class TicketInformation:
    def __init__(self, source, destination, transport_type, seat=None, additional_info=None):
        # Constructor for the TicketInformation class
        # Initializes the object with provided attributes

        # The source of the ticket
        self.source = source

        # The destination of the ticket
        self.destination = destination

        # The type of transport for the ticket (e.g., bus, train, plane)
        self.transport_type = transport_type

        # The seat information for the ticket (optional, may be None)
        self.seat = seat

        # Additional information related to the ticket (optional, may be None)
        self.additional_info = additional_info
