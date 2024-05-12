from slugify import slugify


def sanitize_filename(filename):
    return slugify(filename)
