class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
def display_timeline():
    sm1=SocialMediaProfile('johndoe')
    user=sm1.username
    print(f'{user}')
    p1=sm1.add_post('Hello, world!')
    p2=sm1.add_post('Had a great day at the park!')
    p3=sm1.add_post("What's up, Natalie? How are you?")
    
    

if __name__=="__main__":
    display_timeline()