class TicketSorter:
    def __init__(self, ticket_info):
        """
        Initializes the TicketSorter with a list of TicketInformation objects.

        Args:
            ticket_info (list): List of TicketInformation objects representing different legs of the journey.
        """
        self.ticket_info = ticket_info

    def sort_tickets(self):
    """
    Sorts the list of TicketInformation objects to create a journey itinerary.

    Returns:
        list: List of strings containing instructions for each leg of the journey.
    """
    if not self.ticket_info:
        return ["No tickets provided. Please provide valid ticket information."]

    # Create a dictionary with source as key and corresponding ticket as value
    source_to_ticket = {ticket.source: ticket for ticket in self.ticket_info}

    # Create a set of all destination points
    destinations = {ticket.destination for ticket in self.ticket_info}

    # Find the starting point of the journey (a source that's not in destinations)
    valid_starting_points = set(ticket.source for ticket in self.ticket_info if ticket.source not in destinations)

    # Check if there is only one valid starting point
    if len(valid_starting_points) != 1:
        return ["No valid starting ticket found. Please provide a valid starting point."]

    # Pick the valid starting point as the starting ticket
    starting_ticket_source = valid_starting_points.pop()
    starting_ticket = source_to_ticket[starting_ticket_source]

    # Initialize the journey list with the starting ticket
    journey = [starting_ticket]

    # Traverse the journey by finding next tickets based on destinations
    while journey[-1].destination in source_to_ticket:
        next_ticket = source_to_ticket[journey[-1].destination]
        journey.append(next_ticket)

    # Generate instructions for each ticket in the journey
    instructions = []
    for i, ticket in enumerate(journey):
        guide = f"{i + 1}. {ticket.transport_type} from {ticket.source} to {ticket.destination}."
        if ticket.seat:
            guide += f" {ticket.seat}."
        if ticket.additional_info:
            guide += f" {ticket.additional_info}."
        instructions.append(guide)

    # Add a final arrival message to the instructions
    instructions.append("You have arrived at your final destination.")
    return instructions

