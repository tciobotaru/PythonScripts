#!/usr/bin/env python3

import requests
import json
import sys
import os

ACCESS_TOKEN = os.getenv("SURVEYMONKEY_TOKEN")
BASE_URL = "https://api.surveymonkey.com/v3"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_survey(survey_name):
    """Create a draft survey"""
    data = {"title": survey_name}
    response = requests.post(f"{BASE_URL}/surveys", headers=HEADERS, json=data)
    response.raise_for_status()
    survey_id = response.json()["id"]
    print(f"Created survey '{survey_name}' with ID {survey_id}")
    return survey_id

def create_page(survey_id, page_name):
    """Create a page for a survey"""
    data = {"title": page_name}
    response = requests.post(f"{BASE_URL}/surveys/{survey_id}/pages", headers=HEADERS, json=data)
    response.raise_for_status()
    page_id = response.json()["id"]
    print(f"  Created page '{page_name}' with ID {page_id}")
    return page_id

def create_question(survey_id, page_id, question_name, description, answers):
    """Create a question for a page"""
    data = {
        "headings": [{"heading": description}],
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {"choices": [{"text": ans} for ans in answers]}
    }
    response = requests.post(f"{BASE_URL}/surveys/{survey_id}/pages/{page_id}/questions", headers=HEADERS, json=data)
    response.raise_for_status()
    question_id = response.json()["id"]
    print(f"    Created question '{question_name}' with ID {question_id}")
    return question_id

def create_collector(survey_id, collector_name="Test Collector"):
    """Create a collector without sending emails (safe for draft surveys)"""
    data = {
        "type": "weblink",
        "name": collector_name
    }
    response = requests.post(f"{BASE_URL}/surveys/{survey_id}/collectors", headers=HEADERS, json=data)
    response.raise_for_status()
    collector_id = response.json()["id"]
    print(f"Created collector '{collector_name}' with ID {collector_id} (draft mode, no emails sent)")
    return collector_id

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_survey.py questions.json emails.txt")
        sys.exit(1)

    json_file = sys.argv[1]
    emails_file = sys.argv[2]

    # Load survey questions
    with open(json_file, "r") as f:
        survey_data = json.load(f)

    
    with open(emails_file, "r") as f:
        emails = [line.strip() for line in f if line.strip()]

    if len(emails) < 2:
        print("At least 2 email addresses are required.")
        sys.exit(1)

    # Create survey, pages, questions, and a collector
    for survey_name, pages in survey_data.items():
        survey_id = create_survey(survey_name)

        for page_name, questions in pages.items():
            page_id = create_page(survey_id, page_name)

            for q_name, q_data in questions.items():
                description = q_data.get("Description", "")
                answers = q_data.get("Answers", [])
                if len(answers) < 2:
                    print(f"Question '{q_name}' should have at least 2 answers. Skipping.")
                    continue
                create_question(survey_id, page_id, q_name, description, answers)

        
        create_collector(survey_id)

if __name__ == "__main__":
    main()
