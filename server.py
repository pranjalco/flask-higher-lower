from flask import Flask
import random

"""
p34 30 jan
"""

app = Flask(__name__)
correct_number = random.randint(0, 10)


@app.route("/")
def home_url():
    return (f"<h1 style= 'text-align: center'>Guess a number between 0 and 9</h1>"
            f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'"
            f"style= 'display: block; margin-left: auto; margin-right: auto; width: 50%;'>")


@app.route("/<number>")
def check_number(number):
    try:
        number = int(number)
    except:
        return (f"<h1 style='color: red; text-align: center'>Please enter an integer number between 0 and 10</h1>"
                f"<img src='https://media.giphy.com/media/dJE9Zd0O4prEI/giphy.gif?cid=ecf05e473kz9tzp39eri6p3as3jh18cpbe4dkeb1z10uf841&ep=v1_gifs_search&rid=giphy.gif&ct=g'"
                f"style= 'display: block; margin-left: auto; margin-right: auto; width: 50%;'>")

    if number < correct_number:
        return (f"<h1 style= 'color: red; text-align: center'>Too low, try again!</h1>"
                f"<img src='https://media.giphy.com/media/xUA7bgMrnN7c27iQJG/giphy.gif?cid=790b7611ur1lv8zd3w32kg3lf0nw895ubccjsafqxtc5o9u5&ep=v1_gifs_search&rid=giphy.gif&ct=g'"
                f"style= 'display: block; margin-left: auto; margin-right: auto; width: 50%;'>")
    elif number > correct_number:
        return (f"<h1 style= 'color: blue; text-align: center'>Too high, try again!</h1>"
                f"<img src='https://media.giphy.com/media/3og0ICJy5uWPzPrIiY/giphy.gif?cid=790b7611ur1lv8zd3w32kg3lf0nw895ubccjsafqxtc5o9u5&ep=v1_gifs_search&rid=giphy.gif&ct=g'"
                f"style= 'display: block; margin-left: auto; margin-right: auto; width: 50%;'>")
    else:
        return (f"<h1 style='color: green; text-align: center'>You found me!</h1>"
                f"<img src='https://media.giphy.com/media/q8eXkJGJpFmFi/giphy.gif?cid=790b7611ur1lv8zd3w32kg3lf0nw895ubccjsafqxtc5o9u5&ep=v1_gifs_search&rid=giphy.gif&ct=g'"
                f"style= 'display: block; margin-left: auto; margin-right: auto; width: 50%;'>")


if __name__ == "__main__":
    app.run(debug=True)
