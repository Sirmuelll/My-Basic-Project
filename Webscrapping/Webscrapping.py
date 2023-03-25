# In this project, we will scrape data from "imdb" website
# --> First of all, we will automate the process of selecting some criteria like date of movie release, etc.
# --> Then, we will proceeed with scrapping the data using Selenium
# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


# Initialize chrome
service = Service(executable_path='C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome('./chromedriver')

# Open up our imdb website
website = 'https://www.imdb.com'
driver.get(website)  # this opens the website
driver.maximize_window()  # This maximizes the window
time.sleep(3)

# Click on the dropdown beside the searchbar
all_button = driver.find_element(By.CLASS_NAME, "nav-search-form__categories")
all_button.click()
time.sleep(2)

# click on "Advanced Search"
advanced_search_button = driver.find_element(By.LINK_TEXT, "Advanced Search")
advanced_search_button.click()
time.sleep(2)

# click on "Advanced Title Search"
advanced_title_button = driver.find_element(
    By.LINK_TEXT, "Advanced Title Search")
advanced_title_button.click()
time.sleep(2)

# selecting the important criteria on the page
tv_series = driver.find_element(By.ID, "title_type-3")
tv_series.click()  # this checks the tv series box

feature_film = driver.find_element(By.ID, "title_type-1")
feature_film.click()  # this checks the feature film box

tv_movie = driver.find_element(By.ID, "title_type-2")
tv_movie.click()  # this checks the tv movie box

# Input the values of the release date
from_date = driver.find_element(By.NAME, "release_date-min")
# this inputs the value for the starting date
from_date.send_keys("1997-01-01")

to_date = driver.find_element(By.NAME, "release_date-max")
to_date.send_keys("2022-10-01")  # this inputs the value for the ending date

# Select the user rating
min_rating = driver.find_element(By.NAME, "user_rating-min")
min_rating.click()
mmin_rating = Select(min_rating)
# this selects 7.0 as the minimum user rating
mmin_rating.select_by_visible_text("7.0")

max_rating = driver.find_element(By.NAME, "user_rating-max")
max_rating.click()
mmax_rating = Select(max_rating)
# this selects 10 as the minimum user rating
mmax_rating.select_by_visible_text("10")

# selecting the important genres
action_genre = driver.find_element(By.ID, "genres-1")
action_genre.click()  # this checks the Action box

romance_genre = driver.find_element(By.ID, "genres-20")
romance_genre.click()  # this checks the Romance box

crime_genre = driver.find_element(By.ID, "genres-6")
crime_genre.click()  # this checks the Crime box

# Select your preferred language
language = driver.find_element(By.NAME, "languages")
lang = Select(language)
lang.select_by_visible_text("English")

# Click on the search button
search = driver.find_element(By.CLASS_NAME, "primary")
search.click()
time.sleep(2)

# By now, we will be on the page where we would be extracting our data from.
# We will still Selenium to extract the data instead of alternatives like beautifulsoup
# this finds all the name data
names = driver.find_elements(
    By.XPATH, "//div[@class='lister-item-content']/h3/a")
# this finds all the movies date-released data
date_released = driver.find_elements(
    By.XPATH, '//div[@class = "lister-item-content"]/h3/span[2]')
# This finds all the genre
genre = driver.find_elements(By.XPATH, "//span[@class='genre']")
# This finds all the duration of the movie
duration = driver.find_elements(By.XPATH, "//span[@class='runtime']")
# This finds all the ratings
rating = driver.find_elements(
    By.XPATH, "//div[@class='inline-block ratings-imdb-rating']/strong")
# This finds all the movie descriptions
movie_description = driver.find_elements(By.XPATH, "//p[@class='text-muted']")

"""Now, these are the things we will do in the bullet point below:
- Create lists for all the variables
- Loop through the variables and append them to the lists
- Convert this list to "key-value" pairs to keep them in the dictionary format
- Hand this dictionary to the pandas dataframe"""
names_list = []
date_released_list = []
genre_list = []
duration_list = []
rating_list = []
movie_description_list = []

for n in names:
    names_list.append(n.text)
for d in date_released:
    date_released_list.append(d.text)
for g in genre:
    genre_list.append(g.text)
for l in duration:
    duration_list.append(l.text)
for r in rating:
    rating_list.append(r.text)
for m in movie_description:
    movie_description_list.append(m.text)

print("Here are the list items")
print(names_list)
print(date_released_list)
print(genre_list)
print(duration_list)
print(rating_list)
print(movie_description_list)
