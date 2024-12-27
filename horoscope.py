import tkinter as tk
from tkinter import ttk, messagebox

def get_horoscope():
    # Retrieve user input
    month = month_var.get()
    day = day_entry.get()

    try:
        day = int(day)
        if day < 1 or day > 31:
            raise ValueError("Invalid day")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid day (1-31).")
        return

    # Determine the zodiac sign
    zodiac = ""
    if (month == "January" and day >= 20) or (month == "February" and day <= 18):
        zodiac = "Aquarius"
    elif (month == "February" and day >= 19) or (month == "March" and day <= 20):
        zodiac = "Pisces"
    elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
        zodiac = "Aries"
    elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
        zodiac = "Taurus"
    elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
        zodiac = "Gemini"
    elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
        zodiac = "Cancer"
    elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
        zodiac = "Leo"
    elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
        zodiac = "Virgo"
    elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
        zodiac = "Libra"
    elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
        zodiac = "Scorpio"
    elif (month == "November" and day >= 22) or (month == "December" and day <= 21):
        zodiac = "Sagittarius"
    elif (month == "December" and day >= 22) or (month == "January" and day <= 19):
        zodiac = "Capricorn"

    # Lyrics dictionary
    horoscope_lyrics = {
        "Aquarius": "There's travel in your future\nWhen your tongue freezes to the back of a speeding bus\nFill that void in your pathetic life\nBy playing whack-a-mole 17 hours a day",
        "Pisces": "Try to avoid any Virgos or Leos with the ebola virus\nYou are the true Lord of the dance\nNo matter what those idiots at work say",
        "Aries": "The look on your face will be priceless\nWhen you find that 40 pound watermelon in your colon\nTrade toothbrushes with an albino dwarf, then give a hickey to Meryl Streep",
        "Taurus": "You will never find true happiness\nWhat you gonna do, cry about it?\nThe stars predict tomorrow you'll wake up\nDo a bunch of stuff and then go back to sleep",
        "Gemini": "Your birthday party will be ruined\nOnce again by your explosive flatulence\nYour love life will run into trouble\nWhen your fiancé hurls a javelin through your chest",
        "Cancer": "The position of Jupiter says that\nYou should spend the rest of the week face down in the mud\nTry not to shove a roll of duct tape up your nose while taking your driver's test",
        "Leo": "Now is not a good time to photocopy your butt\nAnd staple it to your bosses face, oh no\nEat a bucket of tuna-flavored pudding\nThen wash it down with a gallon of Strawberry Quik",
        "Virgo": "All Virgos are extremely friendly and intelligent, except for you\nExpect a big surprise today\nWhen you wind up with your head impaled upon a stick",
        "Libra": "A big promotion is just around\nThe corner for someone much more talented than you\nLaughter is the very best medicine\nRemember that when your appendix bursts next week",
        "Scorpio": "Get ready for an\nUnexpected trip\nWhen you fall screaming from an open window\nWork a little bit harder on improving your low self-esteem, you stupid freak",
        "Sagittarius": "All your friends are laughing behind your back (kill them)\nTake down all those naked pictures of\nErnest Borgnine, you've got hanging in your den",
        "Capricorn": "The stars say that you're an exciting and wonderful person\nBut, you know they're lying\nIf I were you, I'd lock my doors and windows\nAnd never, never, never, never, never leave my house again",
    }

    # Display result
    if zodiac in horoscope_lyrics:
        messagebox.showinfo("Your Horoscope", f"Sign: {zodiac}\n\n{horoscope_lyrics[zodiac]}")
    else:
        messagebox.showerror("Error", "Something went wrong.")

# Main application
app = tk.Tk()
app.title("Your Horoscope for Today")
app.resizable(False, False)

# Month dropdown menu
month_label = tk.Label(app, text="Select your birth month:")
month_label.pack()

month_var = tk.StringVar()
month_menu = ttk.Combobox(app, textvariable=month_var, state="readonly")
month_menu['values'] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_menu.pack()

# Day entry
day_label = tk.Label(app, text="Enter your birth day:")
day_label.pack()

day_entry = tk.Entry(app)
day_entry.pack()

# Submit button
submit_button = tk.Button(app, text="Get Horoscope", command=get_horoscope)
submit_button.pack()

# Run the application
app.mainloop()
