import tkinter as tk
from tkinter import messagebox
import requests

def get_exchange_rate(from_currency, to_currency="LKR"):
    """Fetches real-time exchange rate using a free API provider."""
    url = f"https://er-api.com{from_currency}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("result") == "success":
            return data["rates"].get(to_currency)
        else:
            return None
    except Exception:
        return None

def create_currency_window(title, from_currency, geometry_pos):
    """Creates an individual display window for a specific currency."""
    window = tk.Tk()
    window.title(title)
    window.geometry(f"320x180+{geometry_pos}+250")
    window.configure(bg="#f4f6f9")
    window.resizable(False, False)

    # UI Styling Elements
    title_label = tk.Label(
        window, 
        text=f"{from_currency} to LKR", 
        font=("Arial", 14, "bold"), 
        bg="#f4f6f9", 
        fg="#333333"
    )
    title_label.pack(pady=15)

    rate_label = tk.Label(
        window, 
        text="Fetching...", 
        font=("Arial", 22, "bold"), 
        bg="#f4f6f9", 
        fg="#1a73e8"
    )
    rate_label.pack(pady=5)

    def refresh_rate():
        rate = get_exchange_rate(from_currency, "LKR")
        if rate:
            rate_label.config(text=f"{rate:,.2f} LKR")
        else:
            rate_label.config(text="Error", fg="#d93025")

    # Manual refresh button
    refresh_btn = tk.Button(
        window, 
        text="Refresh Rate", 
        command=refresh_rate,
        font=("Arial", 10),
        bg="#ffffff",
        fg="#5f6368",
        relief="groove",
        padx=10
    )
    refresh_btn.pack(pady=10)

    # Initial data pull
    refresh_rate()
    return window

if __name__ == "__main__":
    # Create the Euro Window (Positioned on the left side of the screen)
    euro_window = create_currency_window("Euro Exchange Rate", "EUR", 150)
    
    # Create the Dollar Window (Positioned on the right side of the screen)
    usd_window = create_currency_window("USD Exchange Rate", "USD", 520)

    # Keeps both windows open and processing events simultaneously
    euro_window.mainloop()
