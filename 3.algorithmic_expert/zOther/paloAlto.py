# https://jsonplaceholder.typicode.com/users
# https://jsonplaceholder.typicode.com/posts

# User = "Patricia Lebsack" 
# Translate User into "id" in the 'Users' docment
# In 'posts' entry, the users are tracked by "userId":  "id" == "userId"
# Provide total count of entries fround in the "Posts" document.  The only output is a number. 
# Users doc: `https://jsonplaceholder.typicode.com/users`
# Posts doc: `https://jsonplaceholder.typicode.com/posts`

# first link - looked up the user "Patricia Lebsack" from user doc, find the id the person has

# input the name - 
# convert the id to userId 
# find the userId in the Posts Doc and count how many userId posts are there

import requests

class User:
    def __init__(self, name):
        self.name = name # name of the user
        self.id = self.get_id() # print(User('Patricia Lebsack').get_posts())

    def get_id(self):
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        for user in users.json(): # loop through the users
            if user['name'] == self.name: # if the name of the user is the same as the name of the user
                return user['id'] # return the id of the user

    def get_posts(self):
        posts = requests.get(f'https://jsonplaceholder.typicode.com/posts')
        count = 0
        for post in posts.json(): # loop through the posts
            if post['userId'] == self.id: # if the userId of the post is the same as the id of the user
                count += 1
        return count

def main():
    user = User('Patricia Lebsack')
    print(user.get_posts())

main()
