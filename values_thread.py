import csv
import re

class ValuesExtractor:
    @staticmethod
    def extract_data_from_csv(filename):
        extracted_data = ""
        # boot_data = ""
        capturing = False
        # append_data = False

        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                timestamp, data = row
                data = data.strip()  # Remove leading and trailing spaces
                # if 'BootNotification' in data:
                #     append_data = True

                # if append_data:
                #     boot_data += data

                # if 'imsi' in data:
                #     append_data = False

                if '"connectorId":	1,'in data:
                    capturing = True

                if capturing:
                    extracted_data += data + " "
                    if '"unit": "Celsius"' in data:
                        capturing = False

        extracted_data = ' '.join(extracted_data.split())
        return extracted_data

    @staticmethod
    def extract_values_from_data(extracted_data):
        current_import_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Current\.Import", "location": "Outlet", "unit": "A" \}'
        voltage_outlet_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Voltage", "location": "Outlet", "unit": "V" \}'
        # charge_point_model_pattern = r'"chargePointModel":\s*"([^"]+)"'
        # charge_point_serial_number_pattern = r'"chargePointSerialNumber":\s*"([^"]+)"'
        # firmware_version_pattern = r'"firmwareVersion":\s*"([^"]+)"'

        current_import_matches = re.findall(current_import_pattern, extracted_data)
        voltage_outlet_matches = re.findall(voltage_outlet_pattern, extracted_data)
        # charge_point_model_match = re.findall(charge_point_model_pattern, extracted_data)
        # charge_point_serial_number_match = re.findall(charge_point_serial_number_pattern, extracted_data)
        # firmware_version_match = re.findall(firmware_version_pattern, extracted_data)

        return current_import_matches, voltage_outlet_matches
    # , charge_point_model_match, charge_point_serial_number_match, firmware_version_match




# import csv
# import re

# def extract_data_from_csv(filename):
#     extracted_data = ""
#     boot_data = ""
#     capturing = False
#     append_data = False

#     with open(filename, mode='r', encoding='utf-8') as file:
#         reader = csv.reader(file)

#         for row in reader:
#             if not row:
#                 continue

#             timestamp, data = row
#             data = data.strip()  # Remove leading and trailing spaces
#             if 'BootNotification' in data:
#                 append_data = True

#             if append_data:
#                 boot_data += data

#             if 'imsi' in data:
#                 append_data = False

#             if "OCPP Tx messages" in data:
#                 capturing = True

#             if capturing:
#                 extracted_data += data + " "
#                 if '"unit": "Celsius"' in data:
#                     capturing = False

#     # Remove any trailing spaces from the final result
#     extracted_data = ' '.join(extracted_data.split())
#     return extracted_data and boot_data

# # Usage
# filename = "data.csv"  # Replace with your actual CSV file name
# result = extract_data_from_csv(filename)

# def extract_values_from_data(result):
#     # Define regex patterns for the segments and numerical values
#     current_import_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Current\.Import", "location": "Outlet", "unit": "A" \}'
#     voltage_outlet_pattern = r'\{ "value": "([^"]+)", "context": "Sample\.Periodic", "format": "Raw", "measurand": "Voltage", "location": "Outlet", "unit": "V" \}'
#     charge_point_model_pattern = r'"chargePointModel":\s*"([^"]+)"'
#     charge_point_serial_number_pattern = r'"chargePointSerialNumber":\s*"([^"]+)"'
#     firmware_version_pattern = r'"firmwareVersion":\s*"([^"]+)"'

#     # Find all matches for each pattern
#     current_import_matches = re.findall(current_import_pattern, extracted_data)
#     voltage_outlet_matches = re.findall(voltage_outlet_pattern, extracted_data)
#     charge_point_model_match = re.findall(charge_point_model_pattern, extracted_data)
#     charge_point_serial_number_match = re.findall(charge_point_serial_number_pattern, extracted_data)
#     firmware_version_match = re.findall(firmware_version_pattern, extracted_data)

#     # charge_point_model = charge_point_model_match.group(1) if charge_point_model_match else None
#     # charge_point_serial_number = charge_point_serial_number_match.group(1) if charge_point_serial_number_match else None
#     # firmware_version = firmware_version_match.group(1) if firmware_version_match else None

#     return current_import_matches, voltage_outlet_matches, charge_point_model_match, charge_point_serial_number_match, firmware_version_match

# # Sample extracted_data string
# extracted_data = result

# # Extract values
# current_import_values, voltage_outlet_values , charge_point_model_match, charge_point_serial_number_match, firmware_version_match = extract_values_from_data(result)

# # Output the results
# print("Current Import Values:", current_import_values)
# print("Voltage Outlet Values:", voltage_outlet_values)
# print("model:", charge_point_model_match)
# print("s no:", charge_point_serial_number_match)
# print("firmware:", firmware_version_match)