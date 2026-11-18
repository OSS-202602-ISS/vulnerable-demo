"""Download one web page and print the result. Settings come from config.yaml."""
import requests
import yaml

with open("config.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)

response = requests.get(config["url"], timeout=config["timeout"])
print(config["name"], "->", response.status_code, len(response.text), "characters")
