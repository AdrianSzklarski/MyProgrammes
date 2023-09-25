"""A program that shows currency exchange rates
       @AdrianSzklarski, 09.2023
"""
from privMethods.exchangeratesapi import get_exchangeratesapi
import requests

class Currency:
    def __init__(self):
        self._API_LINK = 'http://api.exchangeratesapi.io/v1/latest?access_key='
        self._API_KEY = f'{get_exchangeratesapi()}'
        self._BASE = 'EUR'
        self._SYMBOLS = 'USD' + ',' + 'GBP' + ',' + 'PLN'

    def get_API(self):
        # Web link building
        return requests.get(self._API_LINK + self._API_KEY + '&' + self._BASE + '&' + self._SYMBOLS)

    def get_program(self):
        """A function that retrieves json from the darom API and works on data related to currencies.

        :param rates: Eexchange rates
        :param base: Base currency (references)
        :param date: Date of data update
        """
        if self.get_API().ok == True:
            data = self.get_API().json()
            self.rates = data["rates"]
            self.base = data["base"]
            self.date = data["date"]


            self.result = []
            for key, value in self.rates.items():
                result = f'{key} : {round(self.rates[key], 3)}'
                self.result.append(result)

            return self.base, self.date, self.result

    def __str__(self):
        cur = f'Base Currency: {self.get_program()[0]}'
        date = f'Date of transaction: {self.get_program()[1]}'
        for i in self.get_program()[2]:
            print(i)

        return cur + '\n' + date


if __name__ == '__main__':
    program = Currency()
    print(program)
