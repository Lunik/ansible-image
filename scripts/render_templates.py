import json
import os
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape


TEMPLATE_FOLDER = "templates"


def generate_templates(config, output):

  os.makedirs(output, exist_ok=True)

  env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
  )

  for template_file in os.listdir(TEMPLATE_FOLDER):
    template = env.get_template(template_file)

    template.stream(**config).dump(os.path.join(output, template_file))


if __name__ == "__main__":
  config = json.loads(sys.argv[1])
  output = sys.argv[2]

  generate_templates(config, output)