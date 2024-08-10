class Manager:
    def __init__(self):
        self.db = {}
        
    def addUser(self, id, name, email):
        if not self.checkUser(id):
            self.db[id] = {
                "name": name,
                "email": email,
                "following": [],
                "followers": [],
            }
            return True
        else:
            print("\nUser alredy exists.")
            return False
        
    def followUser(self, id, id_to_follow):
        if id == id_to_follow:
            print("error")
            return False
        if self.checkUser(id) and self.checkUser(id_to_follow):
            if not id_to_follow in self.db[id]["following"]:
                self.db[id]["following"].append(id_to_follow)
                self.db[id_to_follow]["followers"].append(id)
                return True
            else:
                print(f"\nYou are alredy following {id_to_follow}")
                return False
        else:
            print("\nUser does not exist")
            return False
    
    def unfollowUser(self, id, id_to_unfollow):
        if id == id_to_unfollow:
            print("error")
            return False
        if self.checkUser(id) and self.checkUser(id_to_unfollow):
            if id_to_unfollow in self.db[id]["following"]:
                self.db[id]["following"].remove(id_to_unfollow)
                self.db[id_to_unfollow]["followers"].remove(id)
                return True
            else:
                print(f"\nYou are alredy not following {id_to_unfollow}")
                return False
        else:
            print("\nUser does not exist")
            return False
        
    def retrieve_followers(self, id):
        if self.checkUser(id):
            if len(self.db[id]["followers"]) != 0:
                return self.db[id]["followers"]
            else:
                print("\nNo followers")
                return False
        else:
            print("\nUser does not exist")
            return False
    
    def retrieve_following(self, id):
        if self.checkUser(id):
            if len(self.db[id]["following"]) != 0:
                return self.db[id]["following"]
            else:
                print("\nNo followings")
                return False
        else:
            print("\nUser does not exist")
            return False
    
    # helper functions
    def getUser(self, id):
        return self.db[id]
    
    def checkUser(self, id):
        return True if id in self.db else False
