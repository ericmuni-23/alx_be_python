#!/usr/bin/env python3

# prompt user for weather input


weather = input("What's the weather like today? (sunny/rainy/cold): " )

# provide clothing recommendations based on weather input

if weather == ("sunny"):
    print("Recommendation: Wear a t-shirt and sun glasses.")
elif weather == ("rainy"):
    print("Recommendation: Dont forget your umbrella and a raincoat.")
elif weather == ("cold"):
    print("Recommendation: Wear a warm coat and a scarf.")
else:
    print("Sorry i dont have recomendations for ths weather.")
