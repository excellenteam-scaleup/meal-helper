import random
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def get_meal_options(main_ingredient: str) -> list:
    return requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={main_ingredient}").json()["meals"]


def get_full_recipe(meal_id: int) -> dict:
    return requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}").json()["meals"][0]


def format_ingredients(full_recipe: dict) -> dict:
    return {
        full_recipe[f"strIngredient{index}"]: full_recipe[f"strMeasure{index}"]
        for index in range(1, 21)
        if full_recipe[f"strIngredient{index}"]
    }


def get_recipe_for(main_ingredient: str) -> dict:
    """
    Fetch a random recipe with a specified main ingredient.
    The recipes are requested from "themealdb" API.
    """
    selected_meal = random.choice(get_meal_options(main_ingredient))
    full_recipe = get_full_recipe(selected_meal["idMeal"])
    # 4. Fill in the details of the returned object in the format below
    return dict(
        name=full_recipe["strMeal"],
        image=full_recipe["strMealThumb"],
        video=full_recipe["strYoutube"],
        instructions=full_recipe["strInstructions"],
        ingredients=format_ingredients(full_recipe)
    )


@app.route('/')
def index_page():
    """
    Renders and returns the main page HTML.
    """
    return render_template("index.html")


@app.route('/recipe/<ingredient>')
def recipe(ingredient):
    """
    Renders and returns an HTML page with a random recipe for a given main ingredient.
    """
    return render_template("recipe.html",
                           ingredient=ingredient,
                           recipe=get_recipe_for(ingredient))


@app.route('/recipe/<ingredient>/json')
def recipe_json(ingredient):
    return jsonify(get_recipe_for(ingredient))


if __name__ == '__main__':
    app.run(debug=True)
