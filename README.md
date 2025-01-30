# **Project 34: Flask Higher-Lower Game**

## **Author**
- **Name**: Pranjal Sarnaik  
- **Date**: 30 Jan 2025  

## **Description**
A **Flask-based number guessing game** where:  
- The server randomly selects a number between **0 and 10**.  
- The user guesses by entering a number in the **URL** (e.g., `http://example.com/5`).  
- Based on the guess, the app responds with:  
  - **"Too high, try again!"** (with a GIF from a URL)  
  - **"Too low, try again!"** (with a GIF from a URL)  
  - **"You found me!"** (with a GIF from a URL)  
- Includes **error handling**: If a non-integer is entered, it shows an error message.  

## **How to Use**
1. Run the Flask server (`app.py` or `server.py`).  
2. Open the displayed **server IP (http://example.com/5)** in your browser.  
3. Enter a number (0-10) in the **address bar** after `/`, like:  
   ```
   http://example.com/5
   ```
4. The page will display feedback (**high, low, or correct**) along with a **GIF from an online source**.  
5. If a non-integer is entered (e.g., `/hello`), it shows an **error message**.  

## **Level & Skills**
- **Level**: 🟢 **Simple**  
- **Skills Used**: Flask, Python, Routing, Exception Handling, Web UI  
- **Domain**: Web Development  

## **Features**
✔ **Flask-powered** number guessing game  
✔ **GIFs loaded via URLs** (no local files needed)  
✔ **Error handling** (checks if input is an integer)  
✔ **Lightweight & easy to run**  

## **Installation**
1. Clone this repository:  
   ```bash
   git clone https://github.com/pranjalco/flask-higher-lower.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd flask-higher-lower
   ```
3. Install dependencies (if needed):  
   ```bash
   pip install flask
   ```  

## **Running the Program**
1. **Ensure Python 3.9 or later** is installed on your system.  
2. Run the program using any of the following methods:  
   - **Using PyCharm**: Open the project in PyCharm and run `server.py` and open given url in browser.  
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:  
     ```bash
     python server.py
     ```  
   - **By Double-Clicking**: Double-click `server.py` to run it directly, provided Python is set up to execute `.py` files.  
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.  

## **File Structure**
```
flask-higher-lower/
│── app.py         # Main Flask application
│── README.md      # Project documentation
│── screenshots    # Program screenshots
```

---

📌 **No local GIFs needed** (uses GIFs from URLs).