from datetime import date, datetime
from docxtpl import DocxTemplate
from docx2pdf import convert
import pandas as pd
import re
import pythoncom
from PyQt5.QtCore import QThread, pyqtSignal
import pytz
import csv


class GenerateThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, template_path, data_csv_path, output_docx_path, output_pdf_path, input_file, output_file,import_context, timestamp_column_index=0):
        super().__init__()

        self.template_path = template_path
        self.data_csv_path = data_csv_path
        self.output_docx_path = output_docx_path
        self.output_pdf_path = output_pdf_path
        self.input_file = input_file
        self.output_file = output_file
        self.timestamp_column_index = timestamp_column_index

        self.import_context = import_context

    def run(self):
        pythoncom.CoInitialize()
        try:
            self.convert_timestamps_to_ist(self.input_file, self.output_file, self.timestamp_column_index)
            self.generate_document(self.import_context, self.template_path, self.data_csv_path, self.output_docx_path, self.output_pdf_path)
            self.result_signal.emit("Process complete!")
        finally:
            pythoncom.CoUninitialize()

    def convert_timestamps_to_ist(self, input_file, output_file, timestamp_column_index=0):
        utc_timezone = pytz.utc
        ist_timezone = pytz.timezone('Asia/Kolkata')

        with open(input_file, "r") as csvfile, open(output_file, "w", newline="") as output_csvfile:
            csv_reader = csv.reader(csvfile)
            csv_writer = csv.writer(output_csvfile)

            header = next(csv_reader)
            csv_writer.writerow(header)

            for row in csv_reader:
                timestamp_str = row[timestamp_column_index]

                try:
                    utc_datetime = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print(f"Error parsing timestamp: {timestamp_str}")
                    continue

                ist_datetime = utc_datetime.replace(tzinfo=utc_timezone).astimezone(ist_timezone)
                row[timestamp_column_index] = ist_datetime.strftime("%Y-%m-%d %I:%M %p")
                csv_writer.writerow(row)

        print(f"Timestamp conversion complete! Check '{output_file}' for results.")

    def generate_document(self, import_context, template_path, data_csv_path, output_docx_path, output_pdf_path):
        local_context = {}
        doc = DocxTemplate(template_path)

        column_header = 'Data'
        keywords = ['chargePointSerialNumber', 'chargePointModel', 'firmwareVersion']

        df = pd.read_csv(data_csv_path)

        for keyword in keywords:
            matching_rows = df[column_header].str.contains(keyword, case=False)
            if matching_rows.any():
                value = df.loc[matching_rows, column_header].str.extract(f'"{keyword}":\s*"(.*?)"', flags=re.IGNORECASE)
                local_context[keyword] = value.iloc[0, 0]

        local_context["c_date"] = str(date.today())
        local_context = {**local_context, **import_context}
       
        doc.render(local_context)
        doc.save(output_docx_path)

        output_pdf_path = (f"{local_context['chargePointModel']}#{local_context['chargePointSerialNumber']}.pdf")

        convert(output_docx_path, output_pdf_path)
        print("Document successfully generated.")
