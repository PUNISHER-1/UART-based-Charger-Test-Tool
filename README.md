This project is a Python-based desktop application with a graphical user interface (GUI) designed to interact with an EV charging point via a UART connection. It automates the process of reading, logging, and analyzing charger data, and then generating professional reports.

Key Features
UART Communication: Establishes a connection to the EV charger to receive real-time data streams.
Data Extraction: Automatically parses and extracts critical information.
GUI Interface: Provides a user-friendly interface to control the data acquisition process and view logs.
Report Generation: Creates reports in both DOCX and PDF formats, containing the extracted data.
Timestamp Conversion: Automatically converts timestamps from UTC to Indian Standard Time (IST).

Dependencies
This project requires the following Python libraries. You can install them using pip:
pip install PyQt5
pip install pyserial
pip install docxtpl
pip install docx2pdf
pip install pandas
pip install pytz
Note: docx2pdf relies on the comtypes package for Windows. If you encounter issues on a different OS, you may need to install the appropriate library for document conversion.
