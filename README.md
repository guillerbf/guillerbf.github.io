# Usage

## Running locally.
We need to choose the right version of ruby with `rbenv global 3.3.1` and then run a local server with `make run-local`. If we do changes in _config.yml we need to restart the local server to see them applied. All other changes will display inmediately with reload.

## Create new empty post
`make new-post title={POST_TITLE}`

## Deploy changes to the site
We deploy changes via github based on `main - /docs/`. With `make update-site m="your_commit_message` we automate the stage, commit and push that will therefore update our live site.

