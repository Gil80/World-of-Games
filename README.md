## World Of Games


This simple python program allows a user to select from three different games games with varying difficulties.

1. A memory game.
2. A guess game.
3. A currency roulette game.

Socres are stored on a `.txt` file and presented via HTTP request using the Flask framework.

Additional to this python program, there's a Dockerfile that builds an image with Selenium. This in turn will run a test script to check whether the Flask server is accessible, i.e., the HTTP page is accessible. If not, it will return an error (1).
