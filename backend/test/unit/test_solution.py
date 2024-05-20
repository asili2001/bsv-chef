from unittest import mock
from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet, from_string
import pytest

recipes = [
        {
            "name": "recipe1",
            "diets": [
                "vegetarian",
                "normal",
                "vegan"
            ],
            "ingredients": {
                "ingredient1": 2,
                "ingredient2": 1
            }
        },
        {
            "name": "recipe2",
            "diets": [
                "vegetarian",
                "normal",
                "vegan"
            ],
            "ingredients": {
                "ingredient1": 2,
                "ingredient2": 1
            }
        },
        {
            "name": "recipe3",
            "diets": [
                "vegetarian",
                "normal",
                "vegan"
            ],
            "ingredients": {
                "ingredient1": 2,
                "ingredient2": 1
            }
        }
    ]


@pytest.fixture
def FRecipeController():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    return rc


@pytest.fixture
def rc_readiness_len_0():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    rc.get_readiness_of_recipes = MagicMock()
    rc.get_readiness_of_recipes.return_value = {}
    return rc

@pytest.fixture
def rc_readiness_all_0():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    rc.get_readiness_of_recipes = MagicMock()
    rc.get_readiness_of_recipes.return_value = {
        "recipe1": 0.0,
        "recipe2": 0.0,
        "recipe3": 0.0
    }
    return rc

@pytest.fixture
def rc_readiness_one_01():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    rc.get_readiness_of_recipes = MagicMock()
    rc.get_readiness_of_recipes.return_value = {
        "recipe1": 0.1,
        "recipe2": 0.0,
        "recipe3": 0.0
    }
    return rc

@pytest.fixture
def rc_readiness_one_1():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    rc.get_readiness_of_recipes = MagicMock()
    rc.get_readiness_of_recipes.return_value = {
        "recipe1": 1.0,
        "recipe2": 0.0,
        "recipe3": 0.0
    }
    return rc

@pytest.fixture
def rc_readiness_all_1():
    dao = MagicMock()
    dao.find.return_value = recipes
    rc = RecipeController(dao)
    rc.get_readiness_of_recipes = MagicMock()
    rc.get_readiness_of_recipes.return_value = {
        "recipe1": 1.0,
        "recipe2": 1.0,
        "recipe3": 1.0
    }
    return rc


def randint_0(value1, value2):
    return 2



@pytest.mark.unit
def test_case_0(rc_readiness_len_0):
    """
        get recipe with readiness length of 0

        expected: None
    """
    diet: Diet = from_string("vegetarian")
    recipe = rc_readiness_len_0.get_recipe(diet, take_best=True)

    assert recipe == None

@pytest.mark.unit
def test_case_1(rc_readiness_all_0):
    """
        get recipe with readiness of all 0

        expected: None
    """
    diet: Diet = from_string("vegetarian")
    recipe = rc_readiness_all_0.get_recipe(diet, take_best=True)

    assert recipe == None


@pytest.mark.unit
def test_case_2(rc_readiness_one_01):
    """
        test get the best recipe for a vegetarian diet and of readiness 0.1

        expected: recipe3
    """
    diet: Diet = from_string("vegetarian")
    recipe = rc_readiness_one_01.get_recipe(diet, take_best=True)

    assert recipe == "recipe3"


@pytest.mark.unit
def test_case_3(rc_readiness_one_1):
    """
        test get the best recipe for a vegan diet and of readiness 1

        expected: recipe3
    """
    diet: Diet = from_string("vegan")
    recipe = rc_readiness_one_1.get_recipe(diet, take_best=True)

    assert recipe == "recipe3"

@pytest.mark.unit
def test_case_4(rc_readiness_one_1):
    """
        test get a random recipe for a vegan diet and of readiness 1

        expected: recipe1
    """
    diet: Diet = from_string("vegan")

    with mock.patch('random.randint', randint_0):
        recipe = rc_readiness_one_1.get_recipe(diet, take_best=False)

        assert recipe == "recipe1"

@pytest.mark.unit
def test_case_5(rc_readiness_all_1):
    """
        test get recipe that diet is not available

        expected: None
    """
    diet: Diet = from_string("")
    recipe = rc_readiness_all_1.get_recipe(diet, take_best=False)

    assert recipe == None
