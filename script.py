import instaloader

# Loading instaloader object
loader = instaloader.Instaloader()

# Username
username = "your_username"
password = "your_password"

try:
    # Loading session stored in the system
    loader.load_session_from_file(username)
    
except:
    # Login with username and password
    loader.login(username, password)

# instaloader profile object
profile = instaloader.Profile.from_username(loader.context, username)



def get_unfollowers():
    # Current followers
    current_followers = [i.username for i in profile.get_followers()]
  
    with open('followers.txt', 'r') as f:
        previous_followers = f.read().splitlines()

    # Converting into sets
    set_of_current_followers = set(current_followers)
    set_of_previous_usernames = set(previous_followers)

    # Finding unfollowers
    unfollowers = set_of_previous_usernames.difference(set_of_current_followers)

    if len(unfollowers) == 0:
        print("No unfollowers")
        pass
    else:
        print(unfollowers)

    # Storing the usernames to followers.txt    
    with open('followers.txt', 'w+') as f:
        for followers in profile.get_followers():
            file = f.write(followers.username+"\n")
      

get_unfollowers()
