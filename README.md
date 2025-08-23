# 🐍 Snake AI with NeuroEvolution

This project implements the **classic Snake game** powered by a **Genetic Algorithm + Neural Networks**.  
The snake learns how to survive and eat food through generations of evolution — no hardcoded rules, only pure AI.

---

## ✨ Features
- ✅ Snake controlled entirely by a Neural Network  
- ✅ Training via **Genetic Algorithm (GA)** with mutation + crossover  
- ✅ Fitness-based evolution (snakes that eat more food live longer)  
- ✅ Visualized in **Pygame**  
- ✅ Adjustable training speed (slow for visualization, fast for training)  

---

## 🧠 How It Works
1. Each snake is controlled by a **Neural Network** that takes inputs as follows:
   - Looks for food in all the eight directions (1 if found otherwise 0)
   - Looks for tail in all the eight directions (1 if found otherwise 0)
   - Normalized distance from wall in all the eight directions

2. The network outputs a direction (turn left / move ahead / turn right).  

3. After each generation:
   - Snakes are evaluated with a **fitness score** based on food eaten & survival time.  
   - The best-performing snakes are selected.  
   - New snakes are generated via **crossover + mutation**. 

4. Over time, the snake learns to **avoid looping, survive longer, and eat more food**.  

---

## 🎮 Controls
- The AI plays automatically.  
- You can **adjust FPS** in the code to make training run faster/slower.  

---

## 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot (75)" src="https://github.com/user-attachments/assets/3c7c5c59-80e6-41a2-98e7-c380ceb4cbad" />

---
