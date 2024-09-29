# ScorePredictor

## Data Analysis System for Sports Betting

### Description
This project is a statistical analysis system for Brasileirão 2024 football matches, developed in Prolog, to assist in decision-making in sports betting, showing the probabilities of the match result.

### Features
- **User interaction menu**: The user informs the home and away teams, as well as the level of absence of each one.
- **Probability of match outcome**: The system returns the probabilities of the match result, based on team statistics provided by the user.

### System modeling
From the definition of the data set, which will be imported when starting the program, including previous matches, information about the teams and players, together with the specific data of the confrontation, the probabilities of the result of the duel are calculated, through weights assigned to the parameters.

### Data manipulation
The system uses a dynamic calculation that adjusts the strength of each team based on their stats and absences, as well as adjusting for head-to-head matches between teams of similar status (famous derbies). As the code progresses, the odds are recalculated to ensure that the sum of the 3 possibilities (home win, draw, and away win) is 100%, offering a balanced and realistic prediction of the results.

### Goals
This project combines sports statistics with logic programming to provide well-founded predictions for football matches. Through factors such as recent performance, absences, and history, Score Predictor becomes an effective tool for analyzing and predicting results for the 2024 Brasileirão.

### Languages and Tools
<div style="display: inline_block"><cbr>
  <img align = "top" alt = "gabrielbribeiroo_Prolog" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/prolog/prolog-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_VSCode" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_PowerShell" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/powershell/powershell-original.svg" />
</div>

### Instructions for use
- **Clone the repository**: git clone https://github.com/gabrielbribeiroo/ScorePredictor.git
- **Interpret the project**: Use a Prolog interpreter for the project files.
- **Run the program**: After interpreting, run the function consultar_jogo.
- **Navigate through the menu**: know the probability of the match result.
