"""I investigated the coronavirus case dataset by state. The dataset is from
https://github.com/nytimes/covid-19-data/ (updated daily)
"""

import csv
import typing

import matplotlib.pyplot as plt


def main() -> None:
    """Investigate and display the data"""
    headers, data = get_data()

    # Let's print the headers
    print_title("Headers")
    print(", ".join(headers))

    # Let's get all the data by state
    data_by_state = {}
    for row in data:
        data_by_state[row[1]] = row

    # Let's see the Texas data
    print_title("Texas Statistics")
    texas_data = data_by_state["Texas"]
    for iterator, item in enumerate(headers):
        item_title = item.capitalize()
        print(f"{item_title}: {texas_data[iterator]}")

    # Now, let's plot the confirmed cases and confirmed deaths for each state
    plot_data(data_by_state, 4)
    plot_data(data_by_state, 5)


def get_data() -> typing.Tuple[list, typing.List[list]]:
    """Read the dataset, and return the headers and the actual data"""
    with open("cases_by_state.csv") as data_file:
        data_reader = csv.reader(data_file)
        all_data = list(data_reader)
        return all_data[0], all_data[1:]


def print_title(title: str, underline_char="-") -> None:
    """Pretty print a title"""
    underline = underline_char * len(title)
    print(f"\n{title}\n{underline}")


def plot_data(data_by_state, plot_index):
    """Plot data by state given an index"""
    names, values = [], []
    for state_name, state_data in data_by_state.items():
        try:
            data_val = int(state_data[plot_index])
        except ValueError:
            continue
        names.append(state_name)
        values.append(data_val)
    plt.bar(names, values)
    plt.show()


if __name__ == "__main__":
    main()
