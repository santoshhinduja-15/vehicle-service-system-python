from pathlib import Path


class FileHandler:

    @staticmethod
    def create_file_if_not_exists(file_path):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        Path(file_path).touch(exist_ok=True)

    @staticmethod
    def read_all_lines(file_path):
        FileHandler.create_file_if_not_exists(file_path)

        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]

    @staticmethod
    def append_line(file_path, data):
        FileHandler.create_file_if_not_exists(file_path)

        with open(file_path, "a") as file:
            file.write(data + "\n")

    @staticmethod
    def write_all_lines(file_path, lines):
        FileHandler.create_file_if_not_exists(file_path)

        with open(file_path, "w") as file:
            for line in lines:
                file.write(line + "\n")