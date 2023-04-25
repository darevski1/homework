# GitHub Actions

1. First create new repository on github or use exiting repository. I created new instalation for laravel app, and push to github.
Then we are going to create new **github workflow** open you repository and navigate to ***actions*** and chooes you **workflow** based on application type.

Create workflow.yml file with the folowing content. Ad Commit directly to the **main** branch.

    name: Laravel

    on:
    push:
        branches: [ "main" ]
    pull_request:
        branches: [ "main" ]

    jobs:
    laravel-tests:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v3
        - name: Copy .env
        run: php -r "file_exists('.env') || copy('.env.example', '.env');"
        - name: Update Composer
        run: composer update
        - name: Install Dependencies
        run: composer install
        - name: Generate key
        run: php artisan key:generate
        - name: Directory Permissions
        run: chmod -R 777 storage bootstrap/cache

  ![github action](./images/1.png "k8")


2. We have to **Create self-hosted runner** navigate to settings / actions  and click  Runners from left side menu, and than click on the button **New self-hosted runner** to create runner for the app.
![github action](./images/2.png "k8")


Chooes your OS and run the lollowing commands on you VPS/localhost to create new runner
!   [github action](./images/3.png "k8")

Download

    # Create a folder
    $ mkdir actions-runner && cd actions-runner# Download the latest runner package
    $ curl -o actions-runner-linux-x64-2.303.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.903.0/actions-runner-linux-x64-2.303.0.tar.gz# Optional: Validate the hash
    $ echo "e4a9fb721c1a156eb5d5333232d0cd62e06bec2fd2b321600e85ac914a9cc73  actions-runner-linux-x64-2.303.0.tar.gz" | shasum -a 256 -c# Extract the installer
    $ tar xzf ./actions-runner-linux-x64-2.303.0.tar.gz

Configure

    # Create the runner and start the configuration experience
    $ ./config.sh --url https://github.com/darevski1/happy_card --token ADT6VXPPE5ASDASDASD3EI6QMU# Last step, run it!
    $ ./run.sh

