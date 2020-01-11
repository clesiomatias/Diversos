import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy import Config
Config.set('graphics', 'multisamples', '0')

kivy.require('1.9.1')

class PrimeiroApp(App):
	def build(self):
	    return Label(text='Hello World, Kivy!')

if __name__ == '__main__':
	PrimeiroApp().run()
