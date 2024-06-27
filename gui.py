import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_channel_stats():
    channel_id = id_entry.get()
    if not channel_id:
        messagebox.showerror("Input Error", "Please enter a YouTube channel ID.")
        return
    try:
        response = requests.post('http://127.0.0.1:5000/channel_stats', json={'channel_id': channel_id})
        response_data = response.json()
        if response.status_code == 200:
            result_text = (f"Channel Name: {response_data['channel_name']}\n"
                           f"Average Views per Video: {response_data['average_views']}\n"
                           f"Average Likes per Video: {response_data['average_likes']}\n"
                           f"Average Comments per Video: {response_data['average_comments']}")
            result_label.config(text=result_text)
            save_results(response_data)
        else:
            messagebox.showerror("Error", response_data.get('error', 'An error occurred'))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", str(e))
def save_results(data):
    channel_name = data['channel_name']
    avg_views = data['average_views']
    avg_likes = data['average_likes']
    avg_comments = data['average_comments']
    with open("channel_stats.txt", "a") as file:
        file.write(f"Channel: {channel_name}\n")
        file.write(f"Average Views per Video: {avg_views}\n")
        file.write(f"Average Likes per Video: {avg_likes}\n")
        file.write(f"Average Comments per Video: {avg_comments}\n")
        file.write("\n" + "-"*40 + "\n\n")

root = tk.Tk()
root.title("YouTube Channel Stats")
tk.Label(root, text="YouTube Channel ID:").pack(pady=5)
id_entry = tk.Entry(root, width=50)
id_entry.pack(pady=5)
request_button = tk.Button(root, text="Get Channel Stats", command=get_channel_stats)
request_button.pack(pady=10)
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)
root.mainloop()
