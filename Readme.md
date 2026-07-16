BIOSYNEX Signal Studio

A lightweight biomedical signal inspection and visualization environment built in Python.
BIOSYNEX Signal Studio is the first software module of the BIOSYNEX ecosystem. It is designed to simplify the exploration, inspection, and visualization of biomedical datasets such as EEG, ECG, EMG, biosensor recordings, and other scientific CSV based signal files.
Unlike a traditional CSV viewer, BIOSYNEX Signal Studio focuses on helping researchers quickly understand datasets before analysis by providing organized previews, signal navigation, intelligent inspection, and eventually AI assisted dataset recognition.

Current Features (v0.5.5)

Dataset Management
• Load CSV datasets
• Automatic dataset information panel
• File statistics including
  • Number of rows
  • Number of columns
  • Missing values
  • Numeric columns
  • Text columns

Dataset Navigation

• General dataset preview
• Preview selected columns
• Return to general preview
• Row range selector
• Jump to a specific row
• Column explorer

Signal Visualization

• Plot numeric signal columns
• Embedded Matplotlib graphs
• Interactive graph display within the application

User Interface

• Multi panel dashboard
• Scrollable preview table
• Responsive layout
• Biomedical inspired interface

Project Roadmap

Version 0.1
Initial prototype

Version 0.2
Professional dashboard
Data table
Scrollbars

Version 0.3
Dataset information panel
File metadata

Version 0.4
Column explorer
Preview ranges
Jump to row
Column preview

Version 0.5
Embedded Matplotlib graphs
Version 0.5.5 (Current Development)
Graph workspace tab
Closable graph panels
Improved responsive layout
Scrollable column explorer
Better workspace management

Version 0.6
Statistics
Mean
Median
Minimum
Maximum
Standard deviation
Missing value analysis

Version 0.7
Automatic Dataset Inspector
The software will intelligently recognize biomedical datasets using rule based detection.
Supported datasets will include EEG, ECG, EMG, and general sensor recordings.
The inspector will automatically identify
• Number of channels
• Sampling rate
• Time columns
• Signal columns
• Ready for analysis status
Initially this system will rely on intelligent rules and metadata detection. Machine learning will be introduced only when it provides clear advantages.

Installation
Clone the repository
```bash
git clone https://github.com/owenwogu-ryomen/biosynex-signal-studio.git
```
Navigate into the project
```bash
cd biosynex-signal-studio
```
Install the required libraries
```bash
pip install pandas matplotlib
```
Run the application
```bash
python app_versions/Biosynex_Studio_vo5.5.py
```
Technologies Used
Python
Tkinter
Pandas
Matplotlib
Git
GitHub

Screenshots
Screenshots and demonstrations will be added as development progresses.

Future Plans
The long term goal of BIOSYNEX Signal Studio is to become an intelligent biomedical signal analysis environment capable of supporting
• EEG research
• ECG analysis
• EMG analysis
• Biosensor datasets
• Signal preprocessing
• Signal filtering
• Feature extraction
• Machine learning integration
• AI assisted dataset recognition
• Biomedical research workflows

This application serves as the software foundation for the broader BIOSYNEX project whose mission is to advance accessible biomedical engineering tools for healthcare research and innovation.
Development Status
BIOSYNEX Signal Studio is currently under active development.
The project serves two complementary purposes.
First, it is a structured software engineering journey documenting the development of a biomedical desktop application from concept to a research grade platform.
Second, it is the software foundation for the broader BIOSYNEX ecosystem and is intended to evolve into a practical biomedical signal analysis application.
Every version introduces new capabilities while documenting the software's evolution and the engineering decisions behind it. As development continues, future releases will add statistical analysis, intelligent dataset inspection, signal processing, machine learning support, and advanced biomedical research tools.

Author
Owen Wogu
Biomedical Engineering Student
Federal University of Technology Akure (FUTA)
Founder, BIOSYNEX Project

License
This project is currently under active development.
A formal open source license will be added in a future release.
