import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def get_recipe_for(main_ingredient: str) -> dict:
    """
    Fetch a random recipe with a specified main ingredient.
    The recipes are requested from "themealdb" API.
    """
    # YOUR CODE HERE:
    # 1. Use `requests` to fetch a list of recipes with `main_ingredient`
    #    - Here is a useful URL: www.themealdb.com/api/json/v1/1/filter.php?i=chicken_breast
    #    - Hint: `response.json()`
    # 2. Choose a random recipe from the list
    #    - Hint: `random.choice()`
    # 3. Use `requests` again to fetch the full recipe instructions
    #    - Here is another useful URL: www.themealdb.com/api/json/v1/1/lookup.php?i=52772
    # 4. Fill in the details of the returned object in the format below
    return dict(
        name="",
        image="",
        video="",
        instructions="",
        ingredients=dict(
            # ingredient: measure,
        )
    )


@app.route('/')
def index():
    """
    Renders and returns the main page HTML.
    """
    return render_template("index.html")


# YOUR CODE HERE:
# Make this endpoint get called when for the following routes: "/recipe/<ingredient>"
def recipe(ingredient):
    """
    Renders and returns an HTML page with a random recipe for a given main ingredient.
    """
    return render_template("recipe.html",
                           ingredient=ingredient,
                           recipe=get_recipe_for(ingredient))


# YOU CODE HERE:
# Add another endpoint:
# Route "/recipe/<ingredient>/json" should return a JSON with the output of `get_recipe_for`.
# Hint: `flask.jsonify()`


if __name__ == '__main__':
    app.run(debug=True)
