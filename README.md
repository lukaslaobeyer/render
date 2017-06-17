# The simplest static site generator

Less that 100 lines of Python that will take your [Jinja2](http://jinja.pocoo.org/) templates and build them into a static site.

## Why?

There already are [lots](https://www.staticgen.com/) of static site generators. However, I found most of them to be overkill for the small sites I need to make from time to time. Also, most of them impose too much structure on your project and require lots of configuration. Some even try to be your website and include lots of fanciness that is simply unnecessary when you are writing a small site.

## How to build your site

The only structure this script requires your project to have is as following:

 * Place `render.py` in your project's root directory
 * Create `src/templates` and `src/static` directories
 * When you run `render.py`, the output will be in `build`

### Templates

Jinja2 templates should be placed in `src/templates`. Any `.html`, `.jinja2` or `.tmpl` file in `src/templates` will go through the Jinja2 processor.

Processed files will be copied into `build`, preserving the structure of your `src/templates` directory.

### Static assets

Anything you don't want to be preprocessed by Jinja2 should go in `src/static`.

These files will be copied straight into the `build` directory, preserving directory structure.

## Extra features

This script basically just runs all your templates through Jinja2, it doesn't really do anything special besides that. However, all your templates will be passed a `tree` variable that contains all the names of all the files in your `templates` directory.

This can be used to dynamically generate indices and read variables from other templates, for example.
