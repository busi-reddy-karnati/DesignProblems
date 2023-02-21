class User:
    
    '''
    Terminology:
        followers: People following the user
        user_following: People the user is following
    '''
    def __init__(self, user_name, name):
        #Name of the user
        self.name = name
        #username of the user: different from name
        self.user_name = user_name
        self.number_of_followers = 0
        self.number_user_following = 0
        self.followers = set()
        self.user_following = set()
        