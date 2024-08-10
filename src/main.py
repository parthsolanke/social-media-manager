from manager import Manager
      
def main():
    manager = Manager()
    
    while True:
        print("\n=== Social Media Management System ===")
        print("0. Exit")
        print("1. Add User")
        print("2. Follow a User")
        print("3. Unfollow a User")
        print("4. Retrive followers list")
        print("5. Retrive following list")
        
        option = int(input("\nEnter Option: "))
        
        if option == 1:
            uid = input("\nEnter User ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            success = manager.addUser(id=uid, name=name, email=email)
            
            if success:
                print("\nUser added successfully!")
            else:
                continue
        
        elif option == 2:
            uid = input("\nEnter Your user ID: ")
            id_to_follow = input("Enter user Id to follow: ")
            
            success = manager.followUser(id=uid, id_to_follow=id_to_follow)
            if success:
                print(f"\nUser {uid} is now following user {id_to_follow}")
            else:
                continue
            
        elif option == 3:
            uid = input("\nEnter Your user ID: ")
            id_to_unfollow = input("Enter user Id to unfollow: ")
            
            success = manager.unfollowUser(id=uid, id_to_unfollow=id_to_unfollow)
            if success:
                print(f"\nUser {uid} unfollowed user {id_to_unfollow}")
            else:
                continue
        
        elif option == 4:
            uid = input("\nEnter User ID: ")
            lst = manager.retrieve_followers(id=uid)
            
            if lst:
                print(f"\nFollowers of user {uid}: {lst}")
            else:
                continue
        
        elif option == 5:
            uid = input("\nEnter User ID: ")
            lst = manager.retrieve_following(id=uid)
            
            if lst:
                print(f"\nUsers followed by {uid}: {lst}")
            else:
                continue
        
        elif option == 0:
            print("\nExiting Program")
            exit()
    
if __name__ == "__main__":
    main()