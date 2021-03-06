import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for u in range(num_users):
            self.add_user(u)

        # Create friendships
        for user in self.users:
            friend_amount = random.randint(1, 4)
            for i in range(friend_amount):
                self.add_friendship(user, random.randint(1, len(self.users)))

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        """
        visited = {}
        visited[user_id] = [user_id]
        q = Queue()
        q.enqueue(user_id)
        while q.size() > 0:
            current = q.dequeue()
            friends = self.friendships[current]
            for friend in friends:
                if friend not in visited:
                    q.enqueue(friend)
                    path = list(visited[current])
                    path.append(friend)
                    visited[friend] = path
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)




#To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?
    # you would have to call add_friendships() * n times. 
    # The function checks if user exist and if friend is already friend.
    # then just adds friend in O(1)

#If you create 1000 users with an average of 5 random friends each,
# what percentage of other users will be in a particular user's extended social network? 


# What is the average degree of separation between a user and those in his/her extended network?