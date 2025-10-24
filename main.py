import turtle,pandas
from country import Country

country = Country()

screen = turtle.Screen()
screen.bgpic('map.gif')
screen.setup(width=768,height=461)
screen.title('Map Game')

# #_______
# def my_function(x,y):
#     print(x,y)
# screen.onscreenclick(my_function)
# #_______


data = pandas.read_csv('coordinates.csv')
countries = data['country'].to_list()
guessed = []

# screen.exitonclick()
while len(guessed) < 24:
    answer = screen.textinput(title=f"{len(guessed)}/23",prompt='Type a country name and hit Enter !').title()
    if answer in countries:
        guessed.append(answer)

        country_x = data[data.country == answer]['x'].item() # i did int() and it worked as well
        country_y = data[data.country == answer]['y'].item()
        country.display_country(answer,country_x,country_y)