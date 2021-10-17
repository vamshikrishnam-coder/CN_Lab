# Develop a program to view the data of top 50 movies in IMDB. (Movie name,
# actors, IMDB ratings)
import re
import bs4
import requests

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')

crew = []
for a in soup.select('td.titleColumn a'):
    crew.append(a.attrs.get('title'))

ratings = []
for b in soup.select('td.posterColumn span[name=ir]'):
    ratings.append(b.attrs.get('data-value'))


imdb = []  # list of dictionary

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, 50):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    place = movie[:len(str(index)) - (len(movie))]
    data = {"movie_title": movie_title,
            "place":place,
            "star_cast": crew[index],
            "rating": ratings[index],}
    imdb.append(data)

for item in imdb:
    print(item['place'], '->', item['movie_title'], 'Rating:',
          round(float(item['rating']), 1), '- Starring:', item['star_cast'])
