# AICP Week 2 Tasks

class OutingPlanner:
    def __init__(self):
        self.min_seniors_required = 10
        self.max_seniors_allowed = 36
        self.min_carers_required = 2
        self.additional_carers_threshold = 24

        self.cost_ranges = {
            '12-16': {'coach': 150, 'meal': 14.00, 'ticket': 21.00},
            '17-26': {'coach': 190, 'meal': 13.50, 'ticket': 20.00},
            '27-39': {'coach': 225, 'meal': 13.00, 'ticket': 19.00}
        }

        self.num_seniors = 0
        self.num_carers = 0
        self.total_expenses = 0
        self.expenses_per_person = 0
        self.total_collection = 0
        self.participant_list = []

    def calculate_outing_expenses(self):
        if self.num_seniors < self.min_seniors_required or self.num_seniors > self.max_seniors_allowed:
            print("Error: Number of seniors should be between 10 and 36.")
            return

        if self.num_seniors > self.additional_carers_threshold:
            self.num_carers = self.min_carers_required + 1

        for age_range, costs in self.cost_ranges.items():
            range_start, range_end = map(int, age_range.split('-'))
            if range_start <= self.num_seniors <= range_end:
                self.total_expenses = costs['coach'] + costs['meal'] * self.num_seniors + costs['ticket'] * self.num_seniors
                self.expenses_per_person = self.total_expenses / self.num_seniors
                break

    def record_participant_details(self):
        print("Enter the names and amounts paid by the participants:")
        for _ in range(self.num_seniors + self.num_carers):
            name = input("Enter name: ")
            amount_paid = float(input("Enter amount paid: $"))
            self.participant_list.append((name, amount_paid))
            self.total_collection += amount_paid

    def display_participant_list(self):
        print("\nParticipants on the outing:")
        for name, amount_paid in self.participant_list:
            print(f"{name}: ${amount_paid}")

    def analyze_profit_or_break_even(self):
        profit_or_loss = self.total_collection - self.total_expenses
        if profit_or_loss >= 0:
            print(f"\nThe outing has made a profit of ${profit_or_loss:.2f}.")
        else:
            print(f"\nThe outing has broken even.")


def main():
    planner = OutingPlanner()

    # Task 1: Calculate expenses
    planner.num_seniors = int(input("Enter the number of seniors interested in the outing: "))
    planner.calculate_outing_expenses()
    print(f"\nTotal expenses for the outing: ${planner.total_expenses:.2f}")
    print(f"Expenses per person: ${planner.expenses_per_person:.2f}")

    # Task 2: Record participant details
    planner.record_participant_details()
    planner.display_participant_list()

    # Task 3: Analyze profit or break-even
    planner.analyze_profit_or_break_even()


if __name__ == "__main__":
    main()


