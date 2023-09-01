import unittest
from ticket_information import TicketInformation
from ticket_sorting import TicketSorter


class TestTicketSorter(unittest.TestCase):
    def test_sort_tickets_with_valid_data(self):
        # Create test ticket data with a valid journey
        tickets = [
            TicketInformation("A", "B", "Train"),
            TicketInformation("B", "C", "Bus"),
            TicketInformation("C", "D", "Flight"),
            TicketInformation("D", "E", "Subway"),
        ]

        # Initialize the TicketSorter and call the sorting method
        ticket_sorter = TicketSorter(tickets)
        sorted_instructions = ticket_sorter.sort_tickets()

        # Expected sorted order
        expected_order = [
            "1. Train from A to B.",
            "2. Bus from B to C.",
            "3. Flight from C to D.",
            "4. Subway from D to E.",
            "You have arrived at your final destination."
        ]

        # Test if the sorted instructions match the expected order
        self.assertEqual(expected_order, sorted_instructions)

    def test_sort_tickets_with_missing_starting_ticket(self):
        # Create test ticket data with a missing starting ticket
        tickets = [
            TicketInformation("B", "C", "Bus"),
            TicketInformation("C", "D", "Flight"),
            TicketInformation("D", "E", "Subway"),
        ]

        # Initialize the TicketSorter and call the sorting method
        ticket_sorter = TicketSorter(tickets)

        # Test if the sorting method returns a list containing the error message string
        expected_error_message = "No starting ticket found. Please provide a valid starting point."

        # Get the sorted instructions
        sorted_instructions = ticket_sorter.sort_tickets()

        # Check if the error message is not present in the sorted instructions list
        self.assertNotIn(expected_error_message, sorted_instructions)

    def test_sort_tickets_with_empty_ticket_list(self):
        # Create an empty list of ticket data
        tickets = []

        # Initialize the TicketSorter and call the sorting method
        ticket_sorter = TicketSorter(tickets)

        # Test if the sorting method returns an error message for an empty ticket list
        expected_error_message = ["No tickets provided. Please provide valid ticket information."]
        self.assertEqual(expected_error_message, ticket_sorter.sort_tickets())


if __name__ == "__main__":
    unittest.main()
