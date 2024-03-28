import json
import os

from spacy_llm.util import assemble

CONFIG_PATH = "fewshot.cfg"
EXAMPLES_PATH = "examples.json"


def load_recipes(path="data/recipes", limit=None):
    """Combines all recipe data into a single list."""
    recipes = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        with open(file_path, encoding="utf-8") as f:
            recipe_data = json.load(f)
            recipes.extend(recipe_data)
    return recipes[:limit]


def save_results(results, path="results.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    nlp = assemble(
        CONFIG_PATH,
        overrides={"paths.examples": EXAMPLES_PATH},
    )

    results = []
    for recipe in load_recipes(limit=10):
        ingredients = recipe["ingredients"]
        if not ingredients:
            continue

        ingredients = [ing.lower().strip() for ing in ingredients]
        doc = nlp(" ".join(ingredients))

        entities = {}
        for ent in doc.ents:
            entities.setdefault(ent.label_, []).append(ent.text)

        results.append({"name": recipe["name"], "entities": entities})

    save_results(results)
