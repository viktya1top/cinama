import requests
from bs4 import BeautifulSoup
class CinemaParser:
    '''класс CinemaParser '''
    def __init__(self, town='msk'):
        self.city = town
        self.content = None
    def extract_raw_content(self):
        '''ХАкеры достают ссыло4ку со страницы'''
        inf = requests.get('https://{}.subscity.ru/'.format(self.city))
        self.content = inf.text
    def print_raw_content(self):
        '''Вывод информации со страницы'''
        soup = BeautifulSoup(self.content)
        return(soup.prettify())
PB_PARSER = CinemaParser('spb')
SPB_PARSER.extract_raw_content()