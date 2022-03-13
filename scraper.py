# import module
import requests
import bs4

# Taking the city name as an input from the user
city = str(input('Enter city/country: '))

# Generating the url
url = "https://google.com/search?q=time+in+" + city

# Sending HTTP request and storing result in a variable
request_result = requests.get(url)

# Pulling HTTP data from internet and storing it in a variable
soup = bs4.BeautifulSoup(request_result.text, "html.parser")

# Finding time element from the google search.
# The time is stored inside the class "BNeawe".
time = soup.find("div", class_='BNeawe').text

print(time)
