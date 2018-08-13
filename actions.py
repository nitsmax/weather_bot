from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		'''
		It is currently Partly cloudy in London at the moment. The temperature is 21.0 degrees, the humidity is 69% and the wind speed is 10.5 mph
		from apixu.client import ApixuClient
		api_key = 'f3cb818ef41140ba967141849181008' #your apixu key
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location')
		current = client.getCurrentWeather(q=loc)
		
		
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']
		'''
		loc = tracker.get_slot('location')
		condition = 'Partly cloudy'
		city = loc
		temperature_c = 21.0
		humidity = 69
		wind_mph = 10.5

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]
