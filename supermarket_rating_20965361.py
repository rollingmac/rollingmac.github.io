# Yeung Pok 20965361

import csv
from collections import defaultdict


class SupermarketSales:
    def __init__(self, filename):
        self.filename = filename
        self.sales_data = []

    def read_data(self):
        """Reads the CSV file and stores data in the sales_data list."""
        with open(self.filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.sales_data.append(row)

    def calculate_average_ratings(self):
        """Calculates average ratings for each city."""
        city_ratings = defaultdict(list)

        for record in self.sales_data:
            city = record['City']
            rating = float(record['Rating'])
            city_ratings[city].append(rating)

        average_ratings = {
            city: sum(ratings) / len(ratings) for city, ratings in city_ratings.items()
        }

        return average_ratings

    def find_lowest_average_rating_city(self):
        """Finds the city with the lowest average rating."""
        average_ratings = self.calculate_average_ratings()
        lowest_city = min(average_ratings, key=average_ratings.get)
        lowest_rating = average_ratings[lowest_city]

        return lowest_city, lowest_rating


def main():
    filename = 'supermarket_sales.csv'
    sales = SupermarketSales(filename)
    sales.read_data()
    lowest_city, lowest_rating = sales.find_lowest_average_rating_city()

    print(f"The city with the lowest average rating is {lowest_city} with a rating of {lowest_rating:.2f}.")


if __name__ == "__main__":
    main()
