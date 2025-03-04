# TxtPersona CrewAI 🚀  

TxtPersona CrewAI is a multi-agent AI system built with [CrewAI](https://crewai.com) that reads structured user notes and generates a formatted user persona while analyzing the completeness of the provided information.  

## ✨ Features  
- **Reads user profiles** from a text file (`users.txt`)  
- **Formats the extracted data** into structured user personas  
- **Evaluates the completeness** of each persona and suggests missing details  
- **Combines the persona and evaluation** into a final structured report  
- **Saves the output to a markdown file**  

---

## 📛 Installation  
Ensure you have **Python 3.10 - 3.12** installed on your system.  

### **1 Install Dependencies**  
First, install `crewai` and other required packages:  
```bash
pip install crewai
```
OR use `uv` for dependency management:  
```bash
pip install uv
uv venv
uv install
```

### **2⃣ Set Up Environment Variables**  
Create a `.env` file and add your **OpenAI API key**:  
```bash
OPENAI_API_KEY=your_api_key_here
```

---

## 🛠️ Customization  
Modify the configuration files to adjust agent behavior:  
- **Define agents** in `src/txtpersona/config/agents.yaml`  
- **Set up tasks** in `src/txtpersona/config/tasks.yaml`  
- **Adjust logic** in `src/txtpersona/crew.py`  
- **Modify inputs** in `src/txtpersona/main.py`  

---

## 🚀 Running the Project  
To execute the AI agents and generate the user persona reports, run:  
```bash
crewai run
```
This will process `users.txt`, format user personas, evaluate completeness, and save the final output to `user_personas/{date}_user_personas.md`.

---

## 📄 Example Output  
```
**Name**: John Doe  
**Age**: 29  
**Profession**: Software Engineer  
**Location**: Canada  
**Missing**: Education  
**Additional Information**: Interested in improving coding skills, contributing to open-source projects.  

The persona is 80% complete. Consider adding details about John's education background and personal interests to make it more comprehensive.
```

---

## 🏰 How It Works  
TxtPersona CrewAI consists of multiple AI agents:  

### **1⃣ Reader Agent 📚**  
- Extracts structured user details from `users.txt`.  

### **2⃣ Formatter Agent 📝**  
- Converts extracted data into a structured user persona.  

### **3⃣ Evaluator Agent ✅**  
- Assesses the **completeness** of the persona and suggests missing details.  

### **4⃣ Merger Agent 🔗**  
- Combines the persona with the completeness evaluation.  

### **5⃣ File Writer Agent 💾**  
- Saves the final structured output to a markdown file.  

---

## 🌟 Contributing  
1. **Fork this repository**  
2. **Create a feature branch** (`git checkout -b new-feature`)  
3. **Commit your changes** (`git commit -m "Added new feature"`)  
4. **Push to GitHub** (`git push origin new-feature`)  
5. **Open a Pull Request**  


---

## 🐜 License  
This project is licensed under the **MIT License**.

---
🚀 **Happy Building!**  
```

