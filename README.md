# Reinforcement Learning-based Resource Management xApp for O-RAN

Welcome to the repository for my xApp developed for resource management in communication networks using a Reinforcement Learning (RL) model. This xApp is part of the research published in the paper titled ["Actor-Critic Network for O-RAN Resource Allocation: xApp Design, Deployment, and Analysis"](https://ieeexplore.ieee.org/abstract/document/10008713).

## 📜 Overview

This xApp implements a resource management solution for O-RAN using an A2C (Advantage Actor-Critic) RL model. The model is designed to optimize the allocation of resources in a communication network by learning from the environment and making decisions that maximize efficiency and performance. The xApp leverages the modularity and scalability provided by containerization and Kubernetes to deliver a robust solution for dynamic network environments.

## What is an xApp?

An xApp is a containerized microservice designed to perform specific network functions, such as resource management or optimization, within a distributed network environment. xApps are typically deployed on Kubernetes clusters, running as pods within the nodes of the cluster. Each xApp operates independently, interacting with other network elements through well-defined APIs. The containerized nature of xApps allows for scalability, flexibility, and ease of deployment, enabling them to be seamlessly integrated into existing network infrastructures. These applications are highly modular and can be updated or scaled without impacting the rest of the system, making them ideal for dynamic network environments where real-time adjustments are critical for maintaining performance and efficiency.

### Key Features:
- **Reinforcement Learning Model:** Utilizes the A2C (Advantage Actor-Critic) architecture to learn and optimize resource allocation strategies in real-time.
- **O-RAN Integration:** Designed specifically for O-RAN networks, allowing seamless integration and deployment.
- **InfluxDB Integration:** Efficiently handles time-series data, supporting the creation, deletion, fetching, and processing of large datasets.
- **Shared Data Layer (SDL):** Enables seamless data sharing between different components, such as the RL model, agents, and the simulated environment.
- **Scalability:** Capable of handling high-dimensional state spaces and large action spaces, making it suitable for complex network environments.
- **Real-Time Decision Making:** The xApp makes resource allocation decisions every second, ensuring timely and efficient management of network resources.

## 🛠️ Project Structure

### Root Directory

- `init/`: Initialization scripts and configurations.
- `mr/`: Contains the main logic of the xApp, including the RL model, database interactions, and shared data layer.
  - `main.py`: The entry point of the xApp, where the environment is initialized, and the RL loop is executed.
  - `db.py`: Handles all interactions with the InfluxDB time-series database, including creating databases, measurements, fetching, and writing data.
  - `populate.py`: Responsible for data insertion and processing within the InfluxDB database.
  - `sdl.py`: Implements the shared data layer, which facilitates data sharing between the environment, RL model, and agents.
  - `mobile_env/`: Contains the environment simulation for mobile network scenarios.
- `release/`: Scripts and configurations for releasing the xApp.
- `Dockerfile`: Dockerfile for containerizing the xApp, including setting up dependencies and configuring the runtime environment.
- `setup.py`: Script for setting up and installing the xApp package and its dependencies.
- `mr10-config-file.json`: Configuration file specifying the xApp's settings, including container image, messaging ports, and RMR (RIC Message Router) configurations.

## 🚀 Deployment and Execution

### Building the Docker Image

The xApp is packaged as a Docker container to ensure portability and ease of deployment on a Kubernetes cluster. The `Dockerfile` defines the steps to build the container image:

1. **Base Image Selection**:
   - The `Dockerfile` begins with an Ubuntu base image, followed by the use of an Alpine-based Miniconda image to leverage Python's Conda environment for dependency management.

2. **RMR Setup**:
   - RMR (RIC Message Router) libraries are copied into the container to handle message routing between the xApp and the O-RAN infrastructure.

3. **Dependency Installation**:
   - The `setup.py` script and other dependencies are installed inside the container using `pip`, ensuring all required packages are available.

4. **Copying Application Files**:
   - The application files from the `mr/` directory are copied into the container.

5. **Entrypoint Definition**:
   - The `CMD` directive sets the entry point for the container, running the `run-mr.py` script which internally calls the `start` function in `main.py`.

### Running the xApp on Kubernetes

To deploy this xApp on Kubernetes:

1. **Build the Docker Image**:
   - Navigate to the root directory of the repository and build the Docker image:
     ```bash
     docker build -t xapp-mr:0.0.1 .
     ```

2. **Push the Image to a Registry** (Optional):
   - If you're using a container registry, tag and push the image:
     ```bash
     docker tag xapp-mr:0.0.1 your-registry/xapp-mr:0.0.1
     docker push your-registry/xapp-mr:0.0.1
     ```

3. **Deploy on Kubernetes**:
   - Create a Kubernetes deployment that uses the Docker image. This deployment will create a pod running the xApp within the Kubernetes cluster.

4. **Monitor the xApp**:
   - Use `kubectl` commands to monitor the deployment, view logs, and ensure that the xApp is functioning as expected.

### Main Components Inside the Kubernetes Pod

- **`main.py`:** 
  - This script is the central hub of the xApp, responsible for initializing the environment, running the reinforcement learning loop, and interacting with the InfluxDB and SDL. When the Docker container starts, `main.py` will be automatically executed inside the pod, orchestrating the resource management tasks in real-time.

- **`setup.py`:**
  - This script ensures that all necessary Python packages are installed inside the Docker container. It also defines the entry point (`run-mr.py`) which the Docker container uses to start the xApp.

- **`Dockerfile`:**
  - The Dockerfile defines the entire build process for creating the container image, ensuring that all dependencies and configurations are properly set up to run the xApp in a Kubernetes environment.

## 🧠 Model Architecture

### A2C (Advantage Actor-Critic) Model

The Advantage Actor-Critic (A2C) model is a type of reinforcement learning algorithm that combines both policy-based and value-based methods. The A2C model maintains two neural networks:

- **Actor Network:** Responsible for selecting actions based on the current state. It outputs a probability distribution over actions.
- **Critic Network:** Estimates the value function, which represents the expected cumulative reward of the current state. It helps the actor by providing feedback on the actions it selects.

The A2C model introduces the concept of "advantage," which is the difference between the expected return (value) of an action and the average return. This advantage helps to reduce variance in the policy gradient updates, leading to more stable learning.

### Components:
- **Actor Network:** Determines the best action to take based on the current state.
- **Critic Network:** Evaluates the action taken by the actor and provides feedback to improve future decisions.

## 📝 Reference

This work is based on the research paper: ["Actor-Critic Network for O-RAN Resource Allocation: xApp Design, Deployment, and Analysis"](https://ieeexplore.ieee.org/abstract/document/10008713).

## 📫 Contact

If you have any questions or suggestions, feel free to reach out to me:

- **Email:** [mrkouchakii@gmail.com](mailto:mrkouchakii@gmail.com)
- **LinkedIn:** [linkedin.com/in/mohammadreza-kouchaki](https://www.linkedin.com/in/mohammadreza-kouchaki/)
