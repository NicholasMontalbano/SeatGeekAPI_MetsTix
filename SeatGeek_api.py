# SeatGeek API
import requests
import json
from datetime import datetime
import csv
from os.path import os

class SeatGeek():

    results = []

    def fetch(self, url):
        response = requests.get(url)
        return(response)

    def date_hour(self): 
        now = datetime.now()
        date_hour = now.strftime("%m/%d/%y %H:%M")
        return(date_hour)

    def parse(self, response, date_hour):
        content = json.loads(response.text)
        print(content)
        id = content['id']
        lowest_price = content['stats']['lowest_price']
        median_price = content['stats']['median_price']
        highest_price = content['stats']['highest_price']
        listing_count = content['stats']['listing_count']
        popularity = content['score']

        self.results.append({
                    'id': id,
                    'lowest_price': lowest_price, 
                    'median_price': median_price, 
                    'highest_price': highest_price, 
                    'listing_count' : listing_count, 
                    'popularity': popularity,
                    'date_hour': date_hour
            })

    def to_csv(self):
        if (os.path.exists('listing_stats.csv') == False):
            with open('listing_stats.csv', 'w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
                writer.writeheader()

                for row in self.results:
                    writer.writerow(row)
        else: 
            with open('listing_stats.csv', 'a+', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())

                for row in self.results:
                    writer.writerow(row)

    def run(self):
        client_id = '' # Add SeatGeek Client ID here
        event_id = '5464980'
        url = f'https://api.seatgeek.com/2/events/{event_id}?client_id={client_id}'
        res = self.fetch(url)
        dh = self.date_hour()
        self.parse(res, dh)
        self.to_csv()


if __name__ == '__main__':
    SG = SeatGeek()
    SG.run()
