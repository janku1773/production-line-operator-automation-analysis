# 'Production Line Operator Automation – Time & Step Optimization'

## Overview
This repository presents a **Python-based analysis and validation** of a real industrial automation project implemented in an automotive body shop production line.

The project was successfully deployed during my time at **Renault**, across **four different stations**.  
Its main objective was to **replace two operators with a single operator** by using an **operator-guided automation arm**, while maintaining production targets and simplifying operator interaction.

This repository focuses on the **engineering logic, process constraints, and time validation**, using simulated data and abstracted logic.

## Business Context

- Industry: Automotive – Body Shop
- Production target: **63 vehicles/hour**
- Implied takt time: **~1 vehicle per minute**
- Number of automated stations: **4**
- Maximum acceptable cycle time per station: **< 4 minutes (240 seconds)**

The solution must complete the part transfer within this constraint to avoid line stoppage.

## Problem Statement

The challenge was to:

- Reduce manpower from **2 operators to 1**
- Handle a **heavy part** using an automation arm
- Ensure the operator remains in full control
- Minimize physical effort and cognitive load
- Guarantee production throughput is not impacted

The success criteria were:
- Total cycle time below takt constraints
- Minimal number of operator actions
- Safe, simple, and repeatable operator workflow

## Operator Interface Constraints

To avoid complexity and operational risk, the operator interface was intentionally minimal.

### Available controls:
- Movement authorization (fixed handle location)
- Move up
- Move down
- Open / close pistons
- Tilt up to 30 degrees

Important: No additional buttons or complex sequences were allowed.

This design principle ensured fast learning, ergonomic safety, and operational robustness.

## Operator Workflow

1. Operator picks up the part from the chariot
2. Pistons are closed
3. Automation arm lifts the part
4. Operator moves toward the fixture
5. Vertical fine adjustment is performed manually
6. Part is tilted by 30 degrees
7. Pistons are opened
8. Operator presses fixture confirmation button

Each step was designed to be:
- Deterministic
- Repeatable
- Time-measurable

## Technical Approach

The project models the process using Python by:

- Defining each operator step and its duration
- Calculating total cycle time
- Validating the result against production constraints
- Allowing easy modification for scenario analysis

### Technologies Used
- Python
- pandas
- Jupyter Notebook
- Basic production logic modeling

## Results Summary ##

✔ The defined operator workflow satisfies the production takt time  
✔ Single-operator solution is viable  
✔ Operator steps are minimized and standardized  
✔ The solution is scalable across multiple stations  

This confirms that automation-assisted handling can improve efficiency **without compromising throughput or safety**.

Disclaimer:
- This project uses **simulated and anonymized data**
- No confidential, proprietary, or sensitive information is included
- The repository focuses on **engineering logic and validation methodology**
