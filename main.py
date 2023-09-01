from ticket_information import TicketInformation
from ticket_sorting import TicketSorter

# Example usage
tickets = [
    # Create instances of TicketInformation for different legs of the journey
    TicketInformation("Barcelona", "Gerona Airport", "Take the airport bus"),
    TicketInformation("Madrid", "Barcelona", "Take train 78A", "Sit in seat 45B"),
    TicketInformation("Gerona Airport", "Stockholm", "Take flight SK455", "Gate 45B, seat 3A",
                      "Baggage drop at ticket counter 344"),
    TicketInformation("Stockholm", "New York JFK", "Take flight SK22", "Gate 22, seat 7B",
                      "Baggage will be automatically transferred from your last leg"),
]

# Create a TicketSorter instance and call the sorting method
ticket_sorter = TicketSorter(tickets)
sorted_instructions = ticket_sorter.sort_tickets()

# Print out each instruction in the sorted list
for instruction in sorted_instructions:
    print(instruction)
