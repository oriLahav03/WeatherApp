import datetime
import threading
import time

import pygame
from utilities.weather import Weather
from utilities.button import Button
from utilities.text_box import TextBox


class Window:
    """
    The class represents the window object.
    """

    def __init__(self, data=Weather().get_weather_data()):
        pygame.init()

        # Defines
        self.data = data
        self.degree_type = 'C'
        self.speed_type = ' km/h'
        self.window_width, self.window_height = 410, 350
        self.valid_city = True
        self.clock = pygame.time.Clock()

        # create all the variables
        self.date_text_box = self.city_text_box = self.search_button = self.degree_button = self.degree_text_box = \
            self.sunsets_text_box = self.sunrise_text_box = self.sky_view_text_box = self.wind_speed_text_box = \
            self.max_min_degree_text_box = self.sky_description_text_box = None

        # Functions calling
        self.create_objects()
        self.window = self.create_window()

    def update(self, stop_threads):
        """
        The function updates the data every 30 seconds.
        :param stop_threads: the stop indicator.
        :type stop_threads: bool
        :return: None
        :rtype: None
        """
        while True:
            self.redraw_game_window()
            if stop_threads:
                break
            time.sleep(30)

    def create_objects(self):
        """
        The function creates the objects.
        :return: None
        :rtype: None
        """
        # Create the date text box
        self.date_text_box = TextBox((self.window_width / 3, 0), (140, 32),
                                     datetime.datetime.now().strftime('%d/%m/%Y'), 20, False)
        # Create the city text box
        self.city_text_box = TextBox((10, 40), (140, 32), self.data['city'])
        # Create the search button
        self.search_button = Button((170, 40), (140, 32), 'Search')
        # Create the sky view text box
        self.sky_view_text_box = TextBox((305, 80), (50, 15), self.data['sky']['view'], 15, False)
        # Create the sky description text box
        self.sky_description_text_box = TextBox((275, 110), (50, 15), self.data['sky']['description'], 15, False)
        # Create the degrees text box
        self.degree_text_box = TextBox((5, 85), (140, 32),
                                       str(self.data[self.check_degree_type()]['temperature'])
                                       + (' C°' if self.check_degree_type() == 'temperature_celsius' else ' F°'),
                                       30, False)
        # Create the change degree type button
        self.degree_button = Button((160, 95), (120, 32), 'C° | F°', )
        # Create the max and min degrees text box
        self.max_min_degree_text_box = TextBox((5, 150), (self.window_width, 32), self.get_min_max(), 25, False)
        # Create the sunrise text box
        self.sunrise_text_box = TextBox((5, 300), (140, 32), self.data['sunrise'], 20, False)
        # Create the sunset text box
        self.sunsets_text_box = TextBox((150, 300), (140, 32), self.data['sunsets'], 20, False)
        # Create the wind speed text box
        self.wind_speed_text_box = TextBox((285, 300), (140, 32),
                                           str(round(self.data['wind'] * 3.6, 2)) + self.check_speed_type(), 20, False)

    def create_window(self):
        """
        The function creates the window.
        :return: the window
        :rtype: pygame.Surface
        """
        pygame.init()
        pygame.display.set_caption('Weather')
        pygame.display.set_icon(pygame.image.load('icons/icon.png'))
        return pygame.display.set_mode((self.window_width, self.window_height))

    def start_window(self):
        """
        The function start the TutorialGame.
        :return: None
        :rtype: None
        """
        stop_threads = False
        refresh_data_thread = threading.Thread(target=self.update, args=(lambda: stop_threads,))
        refresh_data_thread.start()

        run = True
        while run:
            self.clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.check_clicks(event)
            self.redraw_game_window()

        stop_threads = True
        refresh_data_thread.join()
        pygame.quit()

    def check_clicks(self, event):
        """
        The function checks the clicks of the user.
        :param event: the event happening
        :type event: pygame.Event
        :return: None
        :rtype:None
        """
        self.check_keys_city(event)
        self.search_click(event)
        self.degree_click(event)

    def redraw_game_window(self):
        """
        The function update the window after every frame change.
        :return: None
        :rtype: None
        """
        self.date_text_box.draw(self.window)
        self.window.blit(pygame.image.load('icons/background.png'), (0, 0))
        self.search_button.draw(self.window)
        self.city_text_box.draw(self.window)

        if not self.valid_city:
            pygame.display.flip()
            return

        self.window.blit(pygame.image.load(f'icons/{self.data["icon"]}.png'), (280, 5))
        self.sky_view_text_box.draw(self.window)
        self.sky_description_text_box.draw(self.window)
        self.degree_text_box.draw(self.window)
        self.degree_button.draw(self.window)
        self.max_min_degree_text_box.draw(self.window)
        self.window.blit(pygame.image.load('icons/sunrise.png'), (5, 200))
        self.window.blit(pygame.image.load('icons/sunset.png'), (150, 200))
        self.window.blit(pygame.image.load('icons/wind.png'), (285, 200))
        self.sunrise_text_box.draw(self.window)
        self.sunsets_text_box.draw(self.window)
        self.wind_speed_text_box.draw(self.window)

        pygame.display.flip()

    def check_keys_city(self, event):
        """
        The function checks the clicks of the user on the city input box.
        :param event: the event happening
        :type event: pygame.Event
        :return: None
        :rtype: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.city_text_box.input_box.collidepoint(event.pos):
                # Toggle the active variable.
                self.city_text_box.active = not self.city_text_box.active
                self.city_text_box.text = ''
            else:
                self.city_text_box.text = self.data['city']
                self.city_text_box.active = False
            # Change the current color of the input box.
            self.city_text_box.color = self.city_text_box.color_active if self.city_text_box.active \
                else self.city_text_box.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.city_text_box.active:
                if event.key == pygame.K_RETURN:
                    self.update_data(Weather(self.city_text_box.text).get_weather_data())
                elif event.key == pygame.K_BACKSPACE:
                    self.city_text_box.text = self.city_text_box.text[:-1]
                    self.search_button.city = self.city_text_box.text[:-1]
                else:
                    self.city_text_box.text += event.unicode
                    self.search_button.city += event.unicode

    def search_click(self, event):
        """
        The function checks the clicks of the user on the search button.
        :param event: the event happening
        :type event: pygame.Event
        :return: None
        :rtype: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.search_button.button.collidepoint(event.pos):
                self.update_data(Weather(self.search_button.city).get_weather_data())

    def degree_click(self, event):
        """
        The function checks the clicks of the user on the degree button.
        :param event: the event happening
        :type event: pygame.Event
        :return: None
        :rtype: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.degree_button.button.collidepoint(event.pos) and self.valid_city:
                self.degree_type = 'C' if self.degree_type == 'F' else 'F'
                symbol = ' C°' if self.check_degree_type() == 'temperature_celsius' else ' F°'
                self.degree_text_box.text = str(self.data[self.check_degree_type()]['temperature']) + symbol
                self.max_min_degree_text_box.text = self.get_min_max()
                speed_type = self.check_speed_type()
                if speed_type == ' km/h':
                    self.wind_speed_text_box.text = str(round(self.data['wind'] * 3.6, 2)) + speed_type
                elif speed_type == ' m/h':
                    self.wind_speed_text_box.text = str(round(self.data['wind'] * 3.6 * 0.621371, 2)) + speed_type

    def check_degree_type(self):
        """
        The function checks the degree type.
        :return: the degree type (C or F)
        :rtype: str
        """
        return 'temperature_celsius' if self.degree_type == 'C' else 'temperature_fahrenheit'

    def check_speed_type(self):
        """
        The function checks the wind speed type.
        :return: the wind speed type (km/h or m/h)
        :rtype: str
        """
        return ' km/h' if self.degree_type == 'C' else ' m/h'

    def get_min_max(self):
        """
        The function returns the min and max temperature in a nice format.
        :return: the min and max temperature in a nice format
        :rtype: str
        """
        symbol = " C°" if self.check_degree_type() == "temperature_celsius" else " F°"
        return f'{self.data[self.check_degree_type()]["min_temperature"]}' \
               f'{symbol} ---------> ' \
               f'{self.data[self.check_degree_type()]["max_temperature"]}{symbol}'

    def update_data(self, data):
        """
        The function updates the data.
        :param data: the weather data
        :type data: dict
        :return: None
        :rtype: None
        """
        self.data = data
        self.search_button.city = ''
        if 'temperature_celsius' not in self.data:
            self.city_text_box.text = 'City not found'
            self.valid_city = False
            return

        self.valid_city = True
        self.city_text_box.text = data['city']
        self.degree_text_box.text = str(self.data[self.check_degree_type()]['temperature']) + (
            ' C°' if self.check_degree_type() == 'temperature_celsius' else ' F°')
        self.max_min_degree_text_box.text = self.get_min_max()
        self.sky_view_text_box.text = data['sky']['view']
        self.sky_description_text_box.text = data['sky']['description']
        self.sunrise_text_box.text = data['sunrise']
        self.sunsets_text_box.text = data['sunsets']
        self.wind_speed_text_box.text = str(round(self.data['wind'] * 3.6, 2)) + self.check_speed_type()


