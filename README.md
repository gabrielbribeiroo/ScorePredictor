# ScorePredictor

## Data Analysis System for Sports Betting

### Description
This project is a statistical analysis system for Brasileirão 2024 football matches, developed in Prolog, to assist in decision-making in sports betting, showing the probabilities of the match result.

### Features
- **User interaction menu**: The user informs the home and away teams and the level of absence of each one.
- **Probability of match outcome**: The system returns the probabilities of the match result, based on team statistics provided by the user.

### System modeling
The definition of the data set, which will be imported when starting the program, includes previous matches, information about the teams and players, and the specific data of the confrontation. Through weights assigned to the parameters, the probabilities of the duel's result are calculated.

### Data manipulation
The system uses a dynamic calculation that adjusts each team's strength based on their stats and absences and for head-to-head matches between teams of similar status (famous derbies). As the code progresses, the odds are recalculated to ensure that the sum of the 3 possibilities (home win, draw, and away win) is 100%, offering a balanced and realistic prediction of the results.

### Goals
This project combines sports statistics with logic programming to provide well-founded predictions for football matches. Through factors such as recent performance, absences, and history, Score Predictor becomes an effective tool for analyzing and predicting results for the 2024 Brasileirão.

### Languages and Tools
#### Back-end
<div style="display: inline_block"><cbr>
  <img align = "top" alt = "gabrielbribeiroo_Prolog" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/prolog/prolog-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_Python" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" /> 
</div>

#### Front-end
<div style="display: inline_block"><cbr>
  <img align = "top" alt = "gabrielbribeiroo_HTML" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_CSS" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_JavaScript" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_Bootstrap" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" />
</div>

#### APIs and Integrations
<div style="display: inline_block"><cbr>
  <img align = "top" alt = "gabrielbribeiroo_FastAPI" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_REST API" height = "50" width = "50" src="https://img.icons8.com/fluency/48/api.png" /> 
</div>

#### 🔧 Development Tools
<div style="display: inline_block"><cbr>
  <img align = "top" alt = "gabrielbribeiroo_VSCode" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
  <img align = "top" alt = "gabrielbribeiroo_PowerShell" height = "50" width = "50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/powershell/powershell-original.svg" />
</div>
  
### Instructions for use
- **Clone the repository**: git clone https://github.com/gabrielbribeiroo/ScorePredictor.git
- **Interpret the project**: Use a Prolog interpreter for the project files (```swipl```).  
- **Run the program**: After interpretation, load the program (```consult('regras.pl').```) and execute the (```consultar_jogo.```) function.
- **Navigate through the menu**: Know the probability of the match result.
