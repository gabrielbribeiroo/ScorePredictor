# ScorePredictor

## **Data Analysis System for Sports Betting**

### **Description**
ScorePredictor is a statistical analysis system designed for Brasileirão 2025 football matches. Developed in Prolog and integrated with Python and web technologies, the system provides data-driven predictions for match outcomes, assisting decision-making in sports betting.

### **Features**
- **Interactive Web Interface**: Enables users to select teams, adjust absence levels, and intuitively view predictions.
- **Probability Analysis**: Calculates match outcome probabilities (home win, draw, away win) based on recent performance, team statistics, and absence levels.
- **Dynamic Updates**: Automatically fetches and updates team statistics from a football data API for the 2025 Brasileirão season.

### **Live Demo**
[Check out the live version on Vercel](https://scorepredictor-woad.vercel.app/)

### **System Architecture**
The system is built around a robust statistical model that dynamically calculates probabilities by:
- **Team Strength**: Based on historical performance, standings, and other key metrics.
- **Recent Form**: Evaluate the last 5 matches to reflect current momentum.
- **Head-to-Head Dynamics**: Considers rivalry matches and derbies for added nuance.
- **Absence Impact**: Weigh the influence of player absences on team performance.

The calculations ensure the sum of probabilities for all three possible outcomes is 100%, providing balanced and reliable predictions.

### **Languages and Tools**
#### **Back-end**
<div style="display: inline_block"><cbr>
  <img align="top" alt="Prolog" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/prolog/prolog-original.svg" />
  <img align="top" alt="Python" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
  <img align="top" alt="FastAPI" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" />
</div>

#### **Front-end**
<div style="display: inline_block"><cbr>
  <img align="top" alt="HTML" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" />
  <img align="top" alt="CSS" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" />
  <img align="top" alt="JavaScript" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" />
  <img align="top" alt="Bootstrap" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" />
</div>

#### **APIs and Integrations**
<div style="display: inline_block"><cbr>
  <img align="top" alt="REST API" height="50" width="50" src="https://img.icons8.com/fluency/48/api.png" />
</div>

#### **🔧 Development Tools**
<div style="display: inline_block"><cbr>
  <img align="top" alt="VSCode" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
  <img align="top" alt="PowerShell" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/powershell/powershell-original.svg" />
</div>


### **Setup and Installation**
Follow the steps below to set up and run the project:

#### **Prerequisites**
1. Install **SWI-Prolog** for Prolog execution.
2. Install Python (>= 3.8) and required libraries: ```pip install fastapi uvicorn requests```

#### **Clone the Repository**
```git clone https://github.com/gabrielbribeiroo/ScorePredictor.git```
```cd ScorePredictor```

#### **Run the Back-End Server**
1. Start the FastAPI server: ```python main.py```
2. The server will run at ```http://127.0.0.1:8000```

#### **Run the Front-End**
Open ```index.html``` in your browser or host it using a local HTTP server (e.g., ```python -m http.server```).


### **Usage Instructions**
- **Access the Web Interface**: Open your browser and navigate to ```http://127.0.0.1:8000``` or the hosted HTML page.
- **Select Teams**: Choose the home and away teams from the dropdown menu.
- **Adjust Absences**: Use the sliders to indicate absence levels for each team.
- **View Predictions**: Click the "Predict" button to see calculated probabilities.


### **Goals**
This project integrates advanced sports statistics with logical programming to:
- Provide realistic predictions for Brasileirão 2025 matches.
- Assist in sports betting decisions with data-driven insights.
- Serve as a learning tool for combining Prolog, Python, and web technologies.


### **Contributing**
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

### **License**
This project is licensed under the MIT License.
