# AI-Based Resume Screening System

## Overview
The **AI-Based Resume Screening System** automates candidate evaluation by extracting and analyzing resume content using NLP and ML. It ranks applicants based on job requirements and presents results via a Flask web interface, streamlining the hiring process. 📄🤖

## Features
- 📝 **Resume Parsing** – Extracts key information from resumes.
- 🤖 **AI-Based Ranking** – Uses machine learning to score candidates.
- 🌍 **Flask Web Interface** – Provides an intuitive UI for recruiters.
- 🔍 **NLP Processing** – Analyzes job descriptions and applicant profiles.
- 📊 **Data Visualization** – Displays candidate insights and rankings.

## Repository Structure
```
Resume-Screening-System/
│── models/              # Pretrained ML models for resume evaluation
│── data/                # Sample resumes and job descriptions
│── frontend/            # Flask-based web interface
│── scripts/             # Utility scripts for data processing
│── results/             # Logs and analysis outputs
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
│── main.py              # System execution file
```

## Technologies Used
- **Programming Language**: Python
- **Machine Learning**: Scikit-Learn, TensorFlow
- **Natural Language Processing**: SpaCy, NLTK
- **Web Framework**: Flask
- **Data Processing**: Pandas, NumPy

## Installation & Usage
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- TensorFlow & Scikit-Learn
- Flask & SpaCy

### Setup & Run
```bash
# Clone the repository
git clone https://github.com/your-username/Resume-Screening-System.git

# Navigate to the project directory
cd Resume-Screening-System

# Install dependencies
pip install -r requirements.txt

# Start the system
python main.py
```

## Usage
1. **Upload Resumes** – Upload multiple resumes via the web interface.
2. **Analyze Candidates** – AI extracts and evaluates resume content.
3. **View Rankings** – Check candidate scores based on job criteria.
4. **Make Decisions** – Use insights to streamline hiring.

## Contributing
Contributions are welcome! If you find any issues or want to improve the project, feel free to fork the repository and submit a pull request.

---
Developed with ❤️ to simplify recruitment using AI.
