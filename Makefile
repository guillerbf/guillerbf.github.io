run-local:
	cd docs && bundle exec jekyll serve --livereload

update-site:
	git add .
	git commit -m "$(m)"
	git push origin main

new-post:
	python docs/create_post.py "$(title)"