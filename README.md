# Ticket Boarding Sorter

This Python program allows you to sort a list of travel tickets to create a journey itinerary. It provides clear instructions for each leg of the journey, starting from the initial point and ending at the final destination.

## How to Execute the Code

1. **Clone the Repository:**

   Clone this repository to your local machine using Git:

   ```shell
   git clone https://github.com/MarkAvilin1/boarding-cards.git
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project folder:

   ```shell
   cd ticket-boarding-sorter
   ```

3. **Run the Main Application:**

   Execute the main application by running `main.py`. You can provide your list of travel tickets in this file. Modify the `ticket_info` list in `main.py` with your own ticket information.

   ```shell
   python main.py
   ```

   This will print the sorted journey instructions to the console.

## How to Run Tests

The project includes unit tests to verify the functionality of the TicketSorter class. You can run these tests using the following steps:

1. **Install Dependencies:**

   If you haven't already, create a virtual environment and install the required dependencies:

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Navigate to the Tests Directory:**

   Change your current directory to the `tests` folder:

   ```shell
   cd tests
   ```

3. **Run the Tests:**

   Execute the tests using the `unittest` test runner:

   ```shell
   python -m unittest test_tickets_sort.py
   ```

   This will run the test cases and display the results in the console.

## Assumptions

- The travel tickets are provided as a list of `TicketInformation` objects, where each object contains the source, destination, transport type, seat (optional), and additional information (optional).
