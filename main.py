import requests
from bs4 import BeautifulSoup
from googlesearch import search

# ----- Llama Function -----
def ask_llama(prompt):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=data)
    return response.json()["response"]

# ----- Resume (Simplified Version) -----
resume_text = """
AI-focused engineering student with internship experience at NF3 Labs.
Skilled in Python, Machine Learning, Data Analysis, React, Node.js.
Built AI-powered analytics systems and IoT-based smart irrigation systems.
Experience with NumPy, Pandas, Scikit-learn, MongoDB, SQL.
"""

# ----- Job Search -----
def find_jobs(role):
    query = f"{role} remote OR worldwide jobs"
    
    print("\nSearching jobs globally...\n")
    
    results = []
    for url in search(query, num_results=5):
        results.append(url)
    
    return results

# ----- Match Resume -----
def analyze_match(job_description):
    prompt = f"""
    Compare this resume with the job description.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Give:
    - Match percentage
    - Strengths
    - Missing skills
    """
    
    return ask_llama(prompt)

# ----- MAIN -----
role = input("Enter role (e.g., Python Developer, AI Engineer): ")

job_links = find_jobs(role)

print("Top Job Links Found:\n")
for link in job_links:
    print(link)

print("\nCopy one job description and paste below:\n")

job_desc = input("Paste job description:\n")

result = analyze_match(job_desc)

print("\n--- Resume Match Analysis ---\n")
print(result)