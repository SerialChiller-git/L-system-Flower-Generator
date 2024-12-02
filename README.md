# L-system Flower Plant Generator

How It Works

An L-System uses a string rewriting mechanism:

    Axiom: The starting string (e.g., F).
    Production Rules: Define how characters are replaced (e.g., F → FF+[+F-F-F]-[-F+F+F]).
    Iterations: Apply the rules iteratively to grow the string.
    Turtle Graphics: Interpret the string using drawing commands (e.g., F = forward, + = turn right, - = turn left).

<h2>Getting Started</h2>
<h3>Prerequisites</h3>

    Python 3.x
    Libraries: pygame.

<h3>Installation</h3>

Clone the repository:

    git clone https://github.com/your-username/l-system-flower-generator.git
    cd l-system-flower-generator

Install dependencies:

    pip install pygame

<h3>Usage</h3>

Run the script:

    python lsystem_flower.py

<h3>Example Output</h3>

![Flower](https://i.imgur.com/yC5JN0W.png)

