# Python Snake Game: An OOP Implementation

A classic Snake game built with **Python 3** and the `turtle` graphics library. This project demonstrates the application of **Object-Oriented Programming (OOP)** principles to manage game state, collision logic, time delay, and user input.


https://github.com/user-attachments/assets/3d381e21-c5a7-4c1f-9e8a-008f2cb61abb


### Key Features
* **Modular Architecture:** Organized into distinct classes for the `Snake`, `Food`, and `Scoreboard`, ensuring a clean separation of concerns.
* **Dynamic Difficulty:** Real-time tail growth and speed management as the player progresses.
* **State Persistence:** High-score tracking using file I/O to save player progress across sessions.
* **Event-Driven Controls:** Seamless user interaction via keyboard listeners.

### Technical Stack & Concepts
* **Language:** Python
* **Graphics:** Turtle Graphics Engine
* **OOP Principles:** Utilized Class Inheritance (specifically inheriting from the `Turtle` class for food and scoreboard) and Encapsulation.
* **File I/O:** Implemented persistent data storage to track all-time high scores.
* **Coordinate Systems:** Applied Cartesian coordinate logic for boundary detection and collision physics.

### Project Structure
* `main.py`: The game loop and screen initialization.
* `snake.py`: Logic for segment movement and head-to-tail collision.
* `food.py`: Randomized spawning (of food) logic using the `random` module.
* `scoreboard.py`: UI management and score logic.
* `timer.py`: Time delays using the `time` module

### Engineering Challenges
* **Collision Logic:** Implemented precise coordinate-based detection to handle head-to-wall and head-to-tail interactions.


<img width="600" height="600" alt="Snake Game 10_02_2026 18_36_10" src="https://github.com/user-attachments/assets/faaaf540-7bdb-4bcb-92f4-183e7971b303" />


<img width="601" height="632" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/cb318db8-85a6-46b4-bdbf-3eefc55f7133" />


* **State Management:** Managed real-time updates of the snake's body segments using a list-based data structure to ensure smooth movement.

## How to Run
1. Ensure you have **Python 3** installed.
2. Clone this repository: `git clone https://github.com/Prosper06-dev/snake_game.git`
3. Navigate to the directory and run: `python main.py`
