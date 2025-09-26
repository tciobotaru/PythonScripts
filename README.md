# PythonScripts

This repository contains multiple Python tasks covering file handling, data processing, system information retrieval, and API integration.

---

## Task 1

### 1. File Extension Extractor
- **Goal:** Create a script that:
  - Accepts a file name as input.
  - Outputs the file's extension.
  - Raises an exception if no extension exists.

---

### 2. List Deduplication & Min/Max Finder
- **Goal:** Given a list of integers:
  - Remove duplicates.
  - Convert the resulting list to a tuple.
  - Find the minimum and maximum numbers.

---

### 3. Access Log Analyzer
- **Goal:** Create a script that:
  - Reads an access log from a file (file name provided as argument).
  - Outputs:
    1. Total number of unique User Agents.
    2. Statistics with the number of requests per User Agent.
- **Note:** Example `access.log` file link provided.

---

### 4. Character Counter
- **Goal:** Given an input string, count the occurrences of all characters.  
  - Example: `pythonnohtyppy → p:3, y:3, t:2, h:2, o:2, n:2`.

---

### 5. System Information Script
- **Goal:** Write a script that retrieves system information:
  - **Distro info**  
  - **Memory:** total, used, free  
  - **CPU info:** model, core numbers, speed  
  - **Current user**  
  - **System load average**  
  - **IP address**
- **Arguments:**
  - `-d` → Distro info  
  - `-m` → Memory info  
  - `-c` → CPU info  
  - `-u` → User info  
  - `-l` → Load average  
  - `-i` → IP address  

---

## Task 2: Survey Monkey API Integration

Create a script that integrates with [Survey Monkey](https://www.surveymonkey.com) to create a survey.

### Prerequisites
1. Sign up at [Survey Monkey](https://www.surveymonkey.com).  
2. Create a draft application at [Survey Monkey Developer](https://developer.surveymonkey.com).  
3. Obtain an **ACCESS_TOKEN** for making API requests.
4. Set the required permissions for the application.

---

### Requirements
- The script should:
  - Accept a **JSON file** with survey questions.
  - Accept a **text file** with a list of email addresses.
- **JSON file structure example:**

```json
{
  "Survey_Name": {
    "Page_Name": {
      "Question1_Name": {
        "Description": "Description of question",
        "Answers": [
          "Answer1",
          "Answer2",
          "Answer3"
        ]
      },
      "Question2_Name": {
        "Description": "Description of question",
        "Answers": [
          "Answer1",
          "Answer2",
          "Answer3"
        ]
      }
    }
  }
}
EMAIL COLLECTION DIDNT WORK AS I HAD TO UPGRADE TO THE PAID VERSION BUT HERE IS THE LINK FOR THE FREE COLLECTOR https://www.surveymonkey.com/r/FXXK69M



