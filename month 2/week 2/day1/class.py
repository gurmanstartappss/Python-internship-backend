# no class so revision
# import csv
# import json
# import logging

# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# try:
#     logging.info("Program Started")

#     csv_file = "data.csv"
#     json_file = "output.json"

#     data = ["hi"]

#     logging.info("Opening CSV file")

#     with open(csv_file, mode="r", newline="", encoding="utf-8") as file:

#         reader = csv.DictReader(file)

#         for row in reader:
#             data.append(row)

#     logging.info("CSV file read successfully")

#     logging.info("Writing JSON file")

#     with open(json_file, mode="w", encoding="utf-8") as file:

#         json.dump(data, file, indent=4)

#     logging.info("JSON conversion completed")

# except FileNotFoundError:
#     logging.error("CSV file not found.")

# except PermissionError:
#     logging.error("Permission denied while accessing the file.")

# except json.JSONDecodeError:
#     logging.error("JSON encoding error.")

# except Exception as e:
#     logging.exception(f"Unexpected Error: {e}")

# finally:
#     logging.info("Program Finished")

import logging
import csv
import json

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format=%())