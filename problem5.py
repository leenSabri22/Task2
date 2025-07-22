class Report:
    def __init__(self, title, has_toc, has_data, has_chart, has_appendix):
        self.title = title
        self.has_toc = has_toc
        self.has_data = has_data
        self.has_chart = has_chart
        self.has_appendix = has_appendix
        self.toppings = []

    def display(self):
        print(f"Title: {self.title}")
        print(f"Table of Contents: {self.has_toc}")
        print(f"Has Data: {self.has_data}")
        print(f"Has Chart: {self.has_chart}")
        print(f"Has Appendix: {self.has_appendix}")
        print(f"Toppings: {self.toppings}")


class ReportBuilder:
    def __init__(self):
        self.title = None
        self.has_toc = None
        self.has_data = None
        self.has_chart = None
        self.has_appendix = None
        self.toppings = []

    def set_title(self, title):
        self.title = title
        return self

    def set_has_toc(self, has_toc):
        self.has_toc = has_toc
        return self

    def set_has_data(self, has_data):
        self.has_data = has_data
        return self

    def set_has_chart(self, has_chart):
        self.has_chart = has_chart
        return self

    def set_has_appendix(self, has_appendix):
        self.has_appendix = has_appendix
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def build(self):
        report = Report(
            self.title, self.has_toc, self.has_data, self.has_chart, self.has_appendix
        )
        report.toppings = self.toppings
        return report


def main():
    report = (
        ReportBuilder()
        .set_title("Monthly Report")
        .set_has_toc(True)
        .set_has_data(True)
        .set_has_chart(True)
        .set_has_appendix(False)
        .add_topping("Summary")
        .add_topping("Graphs")
        .build()
    )

    report.display()


if __name__ == "__main__":
    main()
