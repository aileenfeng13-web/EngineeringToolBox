# EngineeringToolBox
A Python based engineering calculation and analysis toolkit built with Streamlit.

## Overview 
Engineering Toolbox is an interactive web application designed to perform common engineering calculations through a simple Streamlit interface. 

The project combines engineering theory with Python programming, data visualization, input validation, automated testing, and modular software design. 

## Features 

### Unit Conversion 
- Temperature conversion 
- Engineering unit conversions 

### Thermodynamics 
- Ideal Gas Law calculations 
- Pressure, volume, temperature, and mole relationships 

### Fluid Mechanics 
- Reynolds Number calculation 
- Flow regime classification 
- Reynolds Number visualization 
- Darcy-Weisbach pressure drop calculation 
- Darcy friction factor estimation
- Pipe roughness effects

## Software Features
- Interactive Streamlit interface
- Input validation 
- Error handling 
- Automated unit tests
- Modular Python calculation fuctions

## Engineering Calculations 

### Reynolds Number 
The Reynolds Number is calculated using: 
$$
Re = \frac{\rho v D}{\mu}
$$ 
where: 
- $\rho$ = Fluid density 
- $v$ = Fluid velocity 
- $D$ = Pipe diameter 
- $\mu$ = Dynamic viscosity

### Darcy-Weisbach Equation 
Pressure drop is calculated using: 
$$
\Delta P = 
f\frac{L}{D}
\frac{\rho v^2}{2}
$$

where: 
- $f$ = Darcy friction factor
- $L$ = Pipe length 
- $D$ = Pipe diameter\
- $\rho$ = Fluid density 
- $v$ = Fluid velocity

## Technologies
- Python 
- Streamlit
- NumPy 
- Matplotlib 
- Pytest
- Git
- Github

## project Structure

Engineering Tool Box/
- app.py
-  calculators/
    - ideal_gas.py
    -  pipe_flow.py
    - pressure_drop.py
- tests/
    - test_pressure_drop.py
- utils/ 
    - layout.py
- .gitignore
- README.md

## How to Run 

### 1. Clone the repository
git clone https://github.com/aileenfeng13-web/EngineeringToolBox.git 

### 2. Navigate to the project 
cd EngineeringToolBox 

### 3. Create a virtual environment 
puthon -m venv.venv

### 4. Activate the virtual environment 
On macOS/Linux: 
source .venv/bin/activate

### 5. Install dependencies 
pip install -r requirements.txt 

### 6. Run the application 
streamlit run app.py

## Testing 
Automated tests are written using Pytest. 
Run the test suite with: 
python -m pytest

## Learning Goals 
This project was developed to strengthen my skills in: 
- Python programming 
- Chemical engineering calculations
- Fluid mechanics 
- Data visualization 
- Numerical analysis 
- Software testing  
- Git and GitHub
- Modular software design
- Technical documentation

## Future Improvements 
Planned improvements include: 
- Automatic unit conversion 
- Additional fluid mechanics calculations
- Pipe sizing calculations 
- Improved friction factor correlations 
- More automated tests 
- Interactive engineering plots 
- Additional thermodynamics calculations
