from datetime import datetime
import Constants as keys
import requests
import spacy
import Weather as W

nlp = spacy.load("en_core_web_md")

def sample_responses(input_text):
  user_message = str(input_text).lower()
  min_similarity = 0.75
  user_message = nlp(user_message)


  hello = nlp("hello")
  if hello.similarity(user_message) >= min_similarity:
    return "Hi, how're you doing?"


  who = nlp("who are you?")
  if who.similarity(user_message) >= min_similarity:
    return "Hey, it's me! You don't know who I am?"


  rtime = nlp("what time is it?")
  if rtime.similarity(user_message) >= min_similarity:
    now = datetime.now()
    date_time = now.strftime("Now is %H:%M, but why not just check your phone?")
    return str(date_time)
  

  weather = nlp("Current weather in a city")
  if weather.similarity(user_message) >= min_similarity:
    for ent in user_message.ents:
      if ent.label_ == "GPE": # GeoPolitical Entity
        city = ent.text
        break
      else:
        return "You need to tell me a city to check."

    city_weather = W.get_weather(city)
    if city_weather is not None:
      return "In " + city + ", the current weather is: " + city_weather
    else:
      return "Something went wrong."

  
  else:
    return "Sorry I don't understand that. Please rephrase your statement."
