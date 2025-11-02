## ✅ Task 1: AI-Powered Code Completion

This task explored how AI tools like GitHub Copilot assist in writing Python functions. The goal was to sort a list of dictionaries by a given key.

### 🔍 Manual vs AI Comparison
- **Manual code**: Simple and correct, but assumes all keys exist.
- **AI-suggested code**: Used `.get()` to handle missing keys safely.
- **Efficiency**: AI code is more robust for real-world data.

### 📌 Insight
AI tools enhance reliability by anticipating edge cases and improving error handling. In this task, Github Copilot added value by making the function safer and more flexible.

## ✅ Task 2: Automated Testing with AI (Testim.io)

This task involved automating login functionality using [Testim.io](https://www.testim.io), targeting the demo site [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login). 
The goal was to validate both valid and invalid credential scenarios.

### 🔍 Test Configuration
- **Tool**: Testim.io (AI-powered test automation)
- **Browser**: Chrome (1024 × 600 resolution)
- **Test Name**: Automated testing with AI
- **Duration**: 45 seconds
- **Result**: ❌ Failed (1 warning, 1 failed step, 2 passed)

### Test Steps
1. Setup: Define login test with valid/invalid credentials – ⚠️ Warning  
2. Click “Login” – ✅ Passed  
3. Click “Logout” – ✅ Passed  
4. Click “Username” (post-login) – ❌ Failed  


### 🤖 AI Benefits Observed 
- Auto-detection of UI elements (login/logout buttons, input fields)  
- Visual step tracking with screenshots  
- Smart handling of dynamic content and reusable components  

### Insight from Test scripts
AI-enhanced testing improved speed and element recognition, but the failed step highlights the importance of refining assertions and handling post-login states. This demonstrates how AI tools can accelerate testing while still requiring human oversight.


## ✅ Task 3: Predictive Analysis with ML

### 📊 Dataset
Used the Kaggle Breast Cancer Dataset to simulate issue prioritization.

### 🎯 Goal
- Preprocess the data: clean, label, and split into training/testing sets.
- Train a classification model (e.g., Random Forest) to predict issue priority levels: **high**, **medium**, or **low**.
- Evaluate model performance using **accuracy** and **F1-score**.

### Outcome
This task demonstrates how machine learning can be applied to structured data for prioritization tasks. It also highlights the importance of preprocessing and balanced evaluation metrics.


## ✅ Task 4:Fairness Check with IBM AI Fairness 360

This task used IBM’s AI Fairness 360 toolkit to detect and mitigate bias in a simulated dataset.

### 🔍 Fairness Metrics
- **Before mitigation**:
  - Mean difference: `0.0319`
  - Disparate impact: `1.0895`
- **After reweighing**:
  - Mean difference: `0.0`
  - Disparate impact: `1.0`

### 📌 Insight
Even simulated data showed mild bias. Reweighing successfully balanced outcomes across protected groups. Fairness tools are essential for ethical AI development and should be integrated into model pipelines.











