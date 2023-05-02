# Python Chess

## A fully functional chess game with the option of playing against 3 different AI powered difficulties with the computer.

## Index
1. [About](#about)
2. [Demo](#demo)
3. [Usage](#usage)
    * [Installation](#installation)
    * [Game Controls](#controls)
    * [Commands](#commands)
4. [Developer Features](#dev)
5. [Future Improvements](#future)
    * [Efficiency and AI Power](#power)
    * [Gameplay](#gameplay)
6. [Credits](#credits) 
7. [License](#license)
 

<a name="about"></a>
## About
This is a chess game built using Python and Pygame that incorporates all standard chess rules and functionalities such as unpassant, castles, checks, promotions, and checkmates. In addition to these features, the game includes an AI move calculation system that allows the computer to make informed decisions about its moves based on the current state of the board. The AI engine utilizes the minimax and alpha beta pruning algorithms with addition of teaching the AI proper positional advantage of each piece. Main features include:

* Class based design for more scalable and structured code
* Various algorithm implementation such as valid move calculation
* Implemenation of Minimax algorithm for move score calculation, optimzed with Alpha-Beta Pruning
* Various move visualization
* Sound and image implementation

<a name="demo"></a>
## Demo
A GUI chess game including a simple AI, all written in Python.
<p align="center"><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWM4ZDAwYzg2OGJhNWNkZmIzMTUzZTc5NzZiNjEwMmZkYTdhNjU3NyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/UemgyvVLgpZdmFz1AO/giphy.gif" width="600"/>
</p>

<p align="center">
<img src="github-static/main.png" width="600"/>
</p>

| Human vs Human   | Human vs AI (AI is controlling black)  |
|:----------------------|:------------------|
| <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWY4Mjg5YTdkNDczMDNhYzRiMDQ5YzdlMzU0YjM2OTUwZGIxMGU4ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/EnyTrJyjjwTcAkM862/giphy.gif" width="420"  frameBorder="0" class="giphy-embed" allowFullScreen /> | <img src="https://media.giphy.com/media/YNZ1U9FB1VM9KDmdsG/giphy.gif" width="420" frameBorder="0" class="giphy-embed" allowFullScreen /> |


<a name="usage"></a>
## Usage
A link to executable file to play this game is here: For Windows users <a style="color:blue;" href="https://drive.google.com/file/d/10omrOwOEGRWuktQmulFdMlf-dh1gP57q/view?usp=share_link">CLICK HERE</a>. For Linux users <a style="color:orange;" href="https://drive.google.com/file/d/1fv38zVT_72w5eTOCWYMTKEJs6T6PzNjM/view?usp=share_link">CLICK HERE</a>. After downloading the zip file, simply unzip and run the executable file.
Additionally, you can use the following installation to clone and run the file locally on your computer.

To install this project, make sure you have the correct version of Python and Pygame.

<a name="installation"></a>
### Installation
- Switch to Python3.
- Follow the code below to create virtual environment and install the necessary libraries.
(Currently tested on Python 3.8 and Python 3.10)
```
git clone https://github.com/samyarsworld/chess-ai.git
cd chess-ai
python3 -m venv venv
source venv/bin/activate
pip install pygame
cd src
python3 -W ignore main.py
```

<a name="controls"></a>
### Game Controls
To make a move, click on the piece you want to move and drag the piece while holding down the key, then release on the square you want to move it to. If the move is legal, the piece will move to the new square. If the move is not legal, nothing will happen. You have the ability to undo using `u` key unless the game is in checkmate. After checkmate, new game start in a couple of seconds.

On the main menu you have the option to choose a player vs player game, which you and your friend control the pieces on the local computer. Or you can choose to play against the computer by choosing of the three difficulty options available.

<a name="commands"></a>
### Commands
- To start the game, run `python3  main.py` (or hit the run command on your chosen IDE), while in the src directory. While you are in the game:
- To undo a move, press `u`.
- To reset the board, press `r`.


<a name="dev"></a>
## Developer Features
Here are some technical considerations that was used to build and design this project:

**Built with Python and Pygame Libraries:** Your chess app was built using the Python programming language and the Pygame library, which provided the necessary tools for developing the game's graphical interface and handling user input.

**Used Various Pygame Methods and Functions:** In order to create the game's user interface, you utilized various Pygame methods and functions such as display, font, mouse, blit, events, and render. These methods allowed you to create and manipulate visual elements such as game pieces, the game board, and text displays.

**Created Multiple Classes to Organize the Code:** To make your code more modular and easier to manage, you created several classes to represent different elements of the game. These classes included the game itself, the game board, each individual game piece, each square on the board, and each individual move that can be made in the game.

**Implemented Inheritance to Streamline Code:** In order to avoid repeating code and improve code efficiency, you implemented inheritance on the game pieces. By creating a parent class for all game pieces and then creating child classes for each specific piece type (such as the rook, bishop, or queen), you were able to reuse common code across all the different pieces and streamline your codebase.

**Used Pyinstaller to Create a Standalone Executable:** To make your game accessible and easy to install, you used Pyinstaller to create a standalone executable file. This allowed users to download and install the game on their computers without needing to install any additional libraries or dependencies.


<a name="future"></a>
## Future Improvements
<a name="power"></a>
### Efficiency and AI Power
There are several ways that the AI and algorithms of the game could be improved in the future. Here are a few suggestions:

- **Implement a more sophisticated AI system:** Implementing a machine learning-based AI system is a significant improvement over the simple minimax algorithm. You can use a neural network to make decisions in real-time gameplay. The network is trained on a dataset of board states and moves, and it learns to predict the most likely move given the current state of the board. One of the main advantages of a machine learning-based AI system is its ability to adapt to new situations.

- **Add more depth to the minimax algorithm:** While the current minimax algorithm with alpha-beta pruning is effective, it may struggle to find the best move in more complex positions. One potential solution is to add more depth to the search tree, but this could result in the algorithm running out of space or time. To address this issue, you could explore other optimization techniques such as iterative deepening, transposition tables, or move ordering.

- **Save each state of the board in a clever hashmap with the score:** To avoid repeating calculations for the same positions multiple times, you could use a hash table to store the board state and its corresponding score. This would allow you to quickly look up the score for a given position without having to recalculate it. However, you would need to be careful about the size of the hash table, as it could quickly become too large to fit into memory. One potential solution is to use an LRU (least recently used) cache to limit the number of entries in the hash table.

- **Calculate check state moves by looking at how king might be in check:** Instead of simply checking whether the king is in the path of an opponent's piece, you could also consider how the opponent's pieces might attack the king in future moves. This would allow you to identify potential checkmate positions earlier in the game and avoid making moves that leave your king vulnerable.

- **Using python numpy arrays for faster arrays:** To improve the performance of the game, you could consider using numpy arrays instead of regular Python lists for storing the board state. Numpy arrays are optimized for numerical operations and can be significantly faster than lists for large datasets.

- **Add an opening move database:** Another potential improvement would be to add a database of opening moves that the AI could use to make informed decisions at the beginning of the game. There are many existing databases of opening moves available online, such as the "Chess Openings Explorer" on Chess.com or the "ECO Codes" on Chessgames.com. By using these databases, the AI could make more strategic opening moves and gain an advantage over its opponent.


<a name="gameplay"></a>
### Gameplay
Here are some possible suggestions to make a improve the gameplay and add more user experience features:

- **Multiplayer Mode for More Engaging Gameplay:** Add a multiplayer mode to the game to provide players with a more challenging and engaging experience. Allow players to compete against each other online or locally, and provide options for creating custom games and tournaments.

- **Improved Menu System for Better User Experience:** Improve the game's menu system to make it more user-friendly and intuitive. Add a tutorial or help section to guide new players, and organize menu items in a clear and organized way.

- **More AI Players with Varying Skill Levels:** Add more AI players with varying skill levels to provide players with a wider range of opponents to play against. Include beginner, intermediate, and advanced AI players, each with different strengths and weaknesses.

- **More Theme Colors and Customization Options:** Add more theme colors and customization options to the game to make it more visually appealing and personalized. Allow players to choose from a variety of colors and themes to customize their game board and pieces.

- **Move Suggestions for Improved Gameplay:** Provide move suggestions for players to make the game more accessible and helpful for new players. Include a feature that shows players possible moves and strategies based on the current game state.

- **Live Board Score Bar for More Exciting Gameplay:** Add a live board score bar that updates in real-time to make the game more exciting and competitive. Show players the current score and give them an idea of how they are doing compared to their opponent.

- **Ability to Save Games and Analyze Gameplay:** Allow players to save their games to come back to later or analyze their gameplay. Include a feature that allows players to study different game positions and strategies and learn from their mistakes.


<a name="credits"></a>
## Contributors

- SAMYAR FARJAM (https://github.com/samyarsworld)

<a name="license"></a>
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
