import praw
import time
import threading

reddit = praw.Reddit(client_id="nXZFD_h0Z1lZGQ", client_secret="wSC_BPthZK8TP0hNB5D7XFAv1NoDrA", user_agent="Python:MistaSvech:1.0 (by u/ZestyPepperoni)", refresh_token="818119085755-g6HKO9vqcNu68cXSNjm9q8UEFAkyQg")

def commentReply(threadName, delay):
    print("Comment reply Thread starting...")
    subreddit = reddit.subreddit("canes")
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            if "svech" in comment.body:
                print(comment.body)
                print("***Found 'Svech'***")
                comment.reply('AAAHHHHHHHH, MISTA STRECHNIKOV \n\n^^I ^^am ^^a ^^bot. \n^^Downvote ^^me ^^to ^^delete.')
                time.sleep(480)
            elif "andrei" in comment.body:
                print(comment.body)
                print("***Found 'Andrei'***")
                comment.reply('AAAHHHHHHHH, MISTA STRECHNIKOV \n\n^^I ^^am ^^a ^^bot. \n^^Downvote ^^me ^^to ^^delete.')
                time.sleep(480)
    except Exception as e:
        print("There was an error. Fix it idiot lol")
        print(e)

def commentLookup(threadName, delay):
    print("Comment Lookup thread starting...")
    while True:
        print("Checking for downvoted comments...")
        for comment in reddit.user.me().comments.top():
            if comment.score <= 0:
                print("Comment ", comment, " has a score of ", comment.score)
                comment.delete()
        time.sleep(60)

def main():
    try:
        t1 = threading.Thread(target=commentReply, args=("Thread-1", 1, ))
        t2 = threading.Thread(target=commentLookup, args=("Thread-2", 2, ))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except Exception as e:
        print("Error: unable to start thread.")
        print(e)

main()