import time
import sys

def slow_print(message, delay=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    message = """
    Dear Mom,

    I want you to know how much I love you. You have always been my biggest supporter, my best friend, and the person who believes in me the most.
    
    I am so grateful for everything you've done for me, and I can't imagine my life without your love and care. 
    
    You are the best mother in the world, and I love you more than words can express!

    With all my love,
    Rani Kamble
    """
    
    slow_print("Surprise! This message is just for you, Mom!\n", delay=0.05)
    slow_print(message, delay=0.05)
    
    print("\n" + "*" * 50)
    print("Happy Mother's Day! ")
    print("*" * 50)

if __name__ == "__main__":
    main()
