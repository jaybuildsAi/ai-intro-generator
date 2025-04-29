def generate_intro(name, interest, fav_tool, goal):
    return f"""👋 Hi, I'm {name}!
    I'm passionate about {interest}, and my favorite AI tool is {fav_tool}.
    I'm on a mission to {goal}. Let's build the future together! 🚀
    """ 
if __name__ == "__main__":
    print("Welcome to the AI Intro Generator!")
    name = input("What's your name? ")
    interest = input("What are you passionate about? ")
    fav_tool = input("What's your favorite AI tool? ")
    goal = input("What's your biggest goal right now? ")

intro = generate_intro(name, interest, fav_tool, goal)
print("\nHere's your generated intro:\n")
print(intro)