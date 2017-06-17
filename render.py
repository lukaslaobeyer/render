#!/usr/bin/python3

import os
import sys
import pathlib
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIRS = ['src/templates']
TEMPLATE_EXTS = ['html', 'jinja2', 'tmpl']
STATIC_DIRS = ['src/static']
OUTPUT_DIR = 'build'

def ensure_dir(filename):
    dirname = os.path.dirname(filename)
    # Create subdirectory for file if not exists
    if not os.path.exists(dirname):
        os.makedirs(dirname)


# Set up Jinja2 environment
env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIRS),
    autoescape=select_autoescape(['html', 'xml'])
)

# Create output directory
output_dir = str(pathlib.Path(OUTPUT_DIR).absolute())

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print('writing output to "{}"'.format(output_dir))
else:
    print('build directory ("{}") already exists'.format(output_dir))
    print('please remove this directory and try again')
    sys.exit(-1)

# Copy static files
print('copying static files')
for static_dir in STATIC_DIRS:
    for filename in pathlib.Path(static_dir).glob('**/*'):
        if filename.is_file():
            stripped = str(filename)[len(static_dir)+1:]
            print(' copying {}...'.format(stripped))
            dest = os.path.join(output_dir, stripped)
            ensure_dir(dest)
            shutil.copy2(str(filename), dest)

# Render all templates
print('rendering templates')
templates = env.list_templates(extensions=TEMPLATE_EXTS)
for template_name in templates:
    print(' rendering {}...'.format(template_name))
    filename = os.path.join(output_dir, template_name)
    ensure_dir(filename)

    # Render template and write to file
    with open(filename, 'w') as f:
        f.write(env.get_template(template_name).render(tree=templates))
    
print('done!')
