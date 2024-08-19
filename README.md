# RL-based Resource Management xApp for O-RAN

Welcome to the repository for my xApp developed for resource management in communication networks using a reinforcement learning (RL) model. This xApp is part of the research published in the paper titled ["Actor-Critic Network for O-RAN Resource Allocation: xApp Design, Deployment, and Analysis"](https://ieeexplore.ieee.org/abstract/document/10008713).

## 📜 Overview

This xApp implements a resource management solution for O-RAN using an Actor-Critic RL model. The model is designed to optimize the allocation of resources in a communication network by learning from the environment and making decisions that maximize efficiency and performance. 

### Key Features:
- **Reinforcement Learning Model:** Utilizes the Actor-Critic architecture to learn and optimize resource allocation strategies in real-time.
- **O-RAN Integration:** Designed specifically for O-RAN networks, allowing seamless integration and deployment.
- **Scalability:** Capable of handling high-dimensional state spaces and large action spaces, making it suitable for complex network environments.
- **Real-Time Decision Making:** The xApp makes resource allocation decisions every second, ensuring timely and efficient management of network resources.

## 🛠️ Project Structure

- `mr/`: Contains the main logic of the xApp, including the RL model and environment setup.
- `main.py`: The entry point of the xApp, where the environment is initialized, and the RL loop is executed.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- TensorFlow
- Gym
- Other dependencies listed in `requirements.txt` (if applicable)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mrkouchaki/mr10.git
    cd mr10/mr
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the xApp:
    ```bash
    python main.py
    ```

## 🧠 Model Architecture

The xApp utilizes an Actor-Critic architecture, a combination of policy-based and value-based methods. This allows the model to effectively balance exploration and exploitation, leading to better resource allocation decisions.

### Components:
- **Actor Network:** Determines the best action to take based on the current state.
- **Critic Network:** Evaluates the action taken by the actor and provides feedback to improve future decisions.

## 📝 Reference

This work is based on the research paper: ["Actor-Critic Network for O-RAN Resource Allocation: xApp Design, Deployment, and Analysis"](https://ieeexplore.ieee.org/abstract/document/10008713).

## 📫 Contact

If you have any questions or suggestions, feel free to reach out to me:

- **Email:** [mrkouchakii@gmail.com](mailto:mrkouchakii@gmail.com)
- **LinkedIn:** [linkedin.com/in/mohammadreza-kouchaki](https://www.linkedin.com/in/mohammadreza-kouchaki/)
