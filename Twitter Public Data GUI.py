import tkinter as tk
from tkinter import messagebox
import tweepy

# Replace with your Twitter API credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Set up Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_tweets():
    username = entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a Twitter username")
        return
    try:
        tweets = api.user_timeline(screen_name=username, count=5, tweet_mode="extended")
        result_text.delete(1.0, tk.END)
        for tweet in tweets:
            result_text.insert(tk.END, f"{tweet.created_at}: {tweet.full_text}\n\n")
    except tweepy.TweepyException as e:
        messagebox.showerror("Error", f"Failed to fetch tweets: {str(e)}")

# Create GUI
root = tk.Tk()
root.title("Twitter Public Data Fetcher")
root.geometry("600x400")

tk.Label(root, text="Enter Twitter Username:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Fetch Tweets", command=fetch_tweets).pack(pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()