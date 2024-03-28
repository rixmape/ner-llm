from run_pipeline import run_pipeline


if __name__ == "__main__":
    config_path = "fewshot.cfg"
    examples_path = "examples.json"

    sample_text = "Sriracha sauce goes really well with hoisin stir fry, but you should add it after you use the wok."
    run_pipeline(sample_text, config_path, examples_path, verbose=True)
