class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Souheila", "souheila@gmail.com")
user2 = User("Francisco", "frfrfr")

user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
