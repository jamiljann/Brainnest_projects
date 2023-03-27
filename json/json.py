  
'''
1. Write a Python program that reads in a JSON file containing data on a set of customers, 
and outputs a list of all the unique countries that the customers are from.
'''
import json 

try: 
    countries = []
    with open('customers.json', 'r') as f:
        data = json.load(f)
        
    for i in data:
        countries.append(i['country'])

    print(countries)
except Exception as e:
    print('Something is wrong: ', e)
    
'''
2. Write a Python program that takes a JSON file containing data on a set of products, 
and outputs the name and price of the most expensive product.
'''
import json 

try: 
    # Opening JSON file
    with open('products.json', 'r') as f:
        data = json.load(f)
    
    most_expensive_price = 0
    most_expensive_name =  ''
    
    for item in data:
        if item['price'] > most_expensive_price:
            most_expensive_price = item['price']
            most_expensive_name = item['name']
    
    print('The most expensive name:', most_expensive_name) 
    print('The most expensive  price', most_expensive_price)
except Exception as e:
    print('Something is wrong: ', e)
    
'''
3. Write a Python program that takes a JSON file containing data on a set of users, and creates a dictionary
 where each key is a user ID and each value is a list of the user's followers.
 {1: [2, 3], 2: [1], 3: [1]}
'''
import json 

out_put = {}                                     # output dictionary is empty
try: 
    # Opening JSON file
    with open('users.json', 'r') as f:
        data = json.load(f)
    
    for item in data:                            # data is a list of users
        followers = []
        my_key = item['id']                      # This is the key of each items of output dictionary
        for follow in item['followers']:         # explore in followers list
            followers.append(follow['id'])       # add id of followers list

        out_put.update({my_key : followers})     # update output dictionary with new data
except Exception as e:
    print('Something is wrong: ', e)

print(out_put)


'''
4. Write a Python program that takes a JSON file containing data on a set of tweets, and outputs the number of 
times each hashtag is used.
'''
import json 

out_put = {}                                            # output dictionary
followers = []                                          # a list of exist hashtags   
                                 
try: 
    # Opening JSON file
    with open('tweets.json', 'r') as f:
        data = json.load(f)
    
    for item in data:                                   # data is a list of tweets
        for follow in item['hashtags']:                 # explore in hashtags list
            followers.append(follow)                    # add hashtags to a list
    for item in followers:
        out_put.update({item : followers.count(item)})

except Exception as e:
    print('Something is wrong: ', e)

print('output: ', out_put)

'''
5. Write a Python program that takes a JSON file containing data on a set of movies, and creates 
a bar chart showing the number of movies released in each year from 2000 to the current year.
'''
import json 
import numpy as np
import matplotlib.pyplot as plt

movies = []  # Number of movies
years = []   # movies years                                                                         
try: 
    # Opening JSON file
    with open('movies.json', 'r') as f:
        data = json.load(f)
    
    for item in data:     # data is a list of movies                              
        if item['year'] >= 2000 and item['year'] <= 2023:
            years.append(item['year'])
            movies.append(len(item['cast']))
except Exception as e:
    print('Something is wrong: ', e)

print('years: ', years)
print('movie numbers: ', movies)

x = np.array(years)
y = np.array(movies)

plt.bar(x,y, width = 0.3)
plt.show()
