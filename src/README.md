# UWB Online Initialization Pipeline for Drone Applications

## Overview

This repository implements a sophisticated Ultra-Wideband (UWB) anchor localization system for drone applications. The pipeline enables a drone to efficiently gather measurements from UWB devices, create initial position estimates, optimize flight trajectories to improve estimates, and finalize precise localizations, all in an online manner without requiring prior knowledge of anchor positions.

![Pipeline Overview](path/to/pipeline_overview.gif)

## Core Components

### 1. Measurement Processing (`measurement_processor.py`)

The measurement processor handles how distance measurements are collected from UWB anchors:

- Implements intelligent measurement collection strategies to ensure geometric diversity
- Controls when to accept or reject measurements based on drone movement
- Features outlier detection and removal capabilities
- Separate handling for pre-estimation and post-optimization measurements

![Measurement Collection Strategy](path/to/measurement_collection.png)

### 2. Position Estimation (`estimation_interface.py`)

Multiple estimation strategies are implemented through a flexible interface:

- **Linear Estimation**:
 - Simple linear least squares
 - Reweighted linear least squares with robustness to outliers
 - Trimmed reweighted estimation for improved robustness

- **Nonlinear Estimation**:
 - Levenberg-Marquardt optimization
 - Iteratively Reweighted Least Squares (IRLS)
 - Expectation-Maximization (EM) algorithm
 - Gaussian Mixture Model (GMM) approach

The estimation interface also provides utilities for:
- Converting between formulations with different bias models
- Computing covariance matrices for uncertainty quantification
- Calculating residuals and error metrics

![Estimation Results Comparison](path/to/estimation_comparison.png)

### 3. Quality Metrics (`metrics_calculator.py`)

Provides metrics to evaluate estimation quality and determine when sufficient measurements have been collected:

- Geometric Dilution of Precision (GDOP)
- Fisher Information Matrix (FIM) and its determinant
- Residual statistics
- Matrix condition numbers
- Convergence detection

![Metrics Evolution](path/to/metrics_evolution.png)

### 4. Trajectory Optimization (`trajectory_optimisation.py`, `trajectory_manager.py`)

Once a rough position estimate is obtained, this component optimizes the drone's trajectory to improve estimation accuracy:

- Information-theoretic optimization using FIM or GDOP
- Strategic waypoint generation for measurement collection
- Multiple strategies for returning to the original mission path
- Evaluation of trajectory quality and information gain

![Trajectory Optimization](path/to/trajectory_optimization.gif)

### 5. Anchor Data Management (`anchor_data.py`)

Structured representation of all data related to each anchor:

- Measurement storage (both pre and post optimization)
- Status tracking through defined states
- Storage for estimates and quality metrics
- Convergence counters for stopping criteria

### 6. Pipeline Coordination (`uwb_online_initialisation_pipeline.py`)

Coordinates all components into a cohesive system:

- Controls state transitions between initialization phases
- Triggers estimations and trajectory optimizations at appropriate times
- Manages measurement collection and processing
- Handles initialization finalization

![Pipeline State Machine](path/to/state_machine.png)

## ROS Integration

For deployment and visualization, ROS2 integration is provided:

- `uwb_online_initialisation_node.py`: Main ROS node that interfaces with the drone system
- `uwb_config_loader.py`: Loads configuration from YAML files
- Subscribers for drone position and anchor information
- Publishers for estimates and optimized trajectories
- Visualization markers for Rviz

![RViz Visualization](path/to/rviz_screenshot.png)

## Simulation Framework

A comprehensive simulation framework enables testing without ROS dependencies:

- `drone_simulator.py`: Simulates drone dynamics and UWB measurements
- `UWB_protocol.py`: Models realistic UWB anchor behavior with biases and noise
- `monte_carlo_simulating.py`: Performs parameter sweeps and statistical analysis

![Monte Carlo Simulation Results](path/to/monte_carlo_results.png)

## Configuration System

The system uses a hierarchical configuration framework:

- `config_params.py`: Defines all configuration parameters and defaults
- Support for loading from YAML files
- Extensive options for tuning all pipeline components

## Pipeline Workflow

1. **Initial Measurement Collection**:
  - Drone collects UWB range measurements at various positions
  - Measurements are accepted based on movement criteria

2. **Initial Estimation**:
  - Linear estimation provides rough position and bias estimates
  - Quality metrics are tracked to determine when sufficient measurements are available

3. **Stopping Criteria Evaluation**:
  - Multiple criteria can be configured (number of measurements, GDOP, residuals, etc.)
  - Once triggered, the pipeline proceeds to trajectory optimization

4. **Trajectory Optimization**:
  - Generates optimal waypoints to improve estimation
  - Considers information gain balanced with mission constraints

5. **Additional Measurement Collection**:
  - Drone follows optimized trajectory
  - Collects additional measurements at strategic positions

6. **Final Estimation**:
  - Nonlinear methods refine the estimate
  - Final position and bias estimates are determined

![Complete Workflow](path/to/complete_workflow.gif)

## Usage

### ROS Integration

1. Configure the system through YAML files
2. Launch the ROS node along with simulation or real hardware
3. Monitor estimated positions and trajectory optimizations through Rviz

### Monte Carlo Simulation

For scientific evaluation and parameter tuning:

```bash
python monte_carlo_simulating.py --test all --generate-data --num-runs 10
```

### Key options:

--test: Select specific test types (linear, stopping, nonlinear, trajectory)
--generate-data: Create new measurement datasets
--trajectory-type: Select trajectory pattern (random, spiral, grid, circular)
--num-runs: Number of repetitions for statistical significance
--num-processes: Enable parallel processing for faster simulation

### Dependencies

Python 3.8+
NumPy, SciPy, Matplotlib
Pandas (for data analysis)
scikit-learn (for GMM implementation)
ROS2 (for deployment and visualization)

### License
This project is licensed under the MIT License - see the LICENSE file for details.