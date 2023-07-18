import logging
import traceback
import datetime


def setup_logger(log_file):
    with open(log_file, "a") as file:
        file.write(f"New Run: {datetime.datetime.now()} ----------------------------------------------------------------------------------------------------" + "\n"+"\n")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Use mode='w' to overwrite the file each time
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

if __name__ == "__main__":
    log_file_path = "logs.log"
    logger = setup_logger(log_file_path)
    logger.info("Script started.")

    try:
        # Your main script logic goes here

        # Your main script logic goes here
        data = [1, 2, 3, 4, 5]
        processed_data = [x / 0 for x in data]

        # Save the processed data to a file
        with open("output.txt", "w") as file:
            for item in processed_data:
                file.write(str(item) + "\n")

    except Exception as e:
        logger.error(f"Script encountered an error: {e}")
        logger.error(traceback.format_exc())

    else:
        logger.info("Script finished successfully.")

    # Remove the file handler to avoid duplicated logs
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)