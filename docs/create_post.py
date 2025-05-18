import os
from datetime import datetime
import sys

def slugify(title):
    return title.lower().replace(" ", "-").replace(":", "").replace("?", "").replace(",", "")

def create_post(title, categories=None, tags=None):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    slug = slugify(title)
    filename = f"docs/_posts/{date}-{slug}.md"
    if not categories:
        categories = "data_science"

    front_matter = f"""---
title: "{title}"
date: {time} +0000
layout: single
categories: {categories}
---

<!-- Write your content here -->
    """

    with open(filename, 'w') as f:
        f.write(front_matter.strip() + "\n")

    print(f"Created post: {filename}")

# Example usage:
# create_post("My New Blog Post", categories="tech", tags="[jekyll, automation]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_post.py 'Post Title'")
    else:
        title = sys.argv[1]
        create_post(title)
