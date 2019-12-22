import json
import tkinter as tk
import urllib.error
import urllib.request
from tkinter import ttk


def get_user_info(handle):
    url = "https://codeforces.com/api/user.info?handles={}".format(handle)

    try:
        with urllib.request.urlopen(url) as res:
            return json.load(res)["result"][0]
    except urllib.error.HTTPError:
        return {}


def main():
    root = tk.Tk()
    root.title("Codeforces Scraper")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    handle = tk.StringVar()

    current_rating = tk.StringVar()
    max_rating = tk.StringVar()
    current_rank = tk.StringVar()
    max_rank = tk.StringVar()

    not_found = tk.StringVar()

    def update_user_info():
        user_info = get_user_info(handle.get())

        if user_info:
            not_found.set("")
            max_rank.set(user_info["maxRank"])
            current_rank.set(user_info["rank"])
            max_rating.set(str(user_info["maxRating"]))
            current_rating.set(str(user_info["rating"]))
        else:
            not_found.set("Handle '{}' not found".format(handle.get()))

    handle_entry = ttk.Entry(mainframe, width=20, textvariable=handle)
    handle_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

    button = ttk.Button(mainframe, text="Find", command=update_user_info)
    button.grid(column=2, row=1, sticky=tk.W)

    ttk.Label(mainframe, textvariable=not_found).grid(column=1, row=2)

    ttk.Label(mainframe, text="Current Rating:").grid(column=1, row=3, sticky=tk.W)
    ttk.Label(mainframe, textvariable=current_rating).grid(column=2, row=3, sticky=tk.W)

    ttk.Label(mainframe, text="Current Rank:").grid(column=1, row=4, sticky=tk.W)
    ttk.Label(mainframe, textvariable=current_rank).grid(column=2, row=4, sticky=tk.W)

    ttk.Label(mainframe, text="Max Rating:").grid(column=1, row=5, sticky=tk.W)
    ttk.Label(mainframe, textvariable=max_rating).grid(column=2, row=5, sticky=tk.W)

    ttk.Label(mainframe, text="Max Rank:").grid(column=1, row=6, sticky=tk.W)
    ttk.Label(mainframe, textvariable=max_rank).grid(column=2, row=6, sticky=tk.W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    handle_entry.focus()
    root.bind("<Return>", update_user_info)

    root.mainloop()


if __name__ == "__main__":
    main()
