class Diplomat:
    """
    Diplomat class to receive and process reports.
    """
    def __init__(self):
        self.reports = []

    def receive_report(self, report):
        """
        Receives a report and stores it.
        :param report: Dictionary containing report data.
        """
        self.reports.append(report)
        print("Report received:", report)

    def process_reports(self):
        """
        Processes all received reports.
        """
        for report in self.reports:
            # Placeholder for processing logic
            print("Processing report:", report)
        self.reports.clear() # Clear reports after processing

# Example usage:
if __name__ == '__main__':
    diplomat = Diplomat()
    sample_report = {'id': 1, 'content': 'Sample report content'}
    diplomat.receive_report(sample_report)
    diplomat.process_reports()