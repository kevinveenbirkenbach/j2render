#!/usr/bin/env python3

import argparse
from jinja2 import Environment, FileSystemLoader
import os

def main():
    parser = argparse.ArgumentParser(
        description="Render a Jinja2 template file into a final output file.",
        epilog="Example: python j2render.py templates/config.yml.j2 output/config.yml"
    )

    parser.add_argument(
        "template",
        help="Path to the Jinja2 template file (e.g., templates/config.yml.j2)"
    )

    parser.add_argument(
        "output",
        help="Path to the rendered output file (e.g., output/config.yml)"
    )

    args = parser.parse_args()

    # Extract directory and filename from the template path
    template_dir = os.path.dirname(args.template) or "."
    template_file = os.path.basename(args.template)

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Load and render template
    template = env.get_template(template_file)
    rendered_output = template.render()

    # Write rendered output to destination file
    with open(args.output, "w") as out_file:
        out_file.write(rendered_output)

    print(f"✅ Rendered '{args.template}' to '{args.output}'.")

if __name__ == "__main__":
    main()
