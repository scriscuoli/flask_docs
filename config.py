import configparser
import os

class Config:
    def __init__(self, config_path="config.ini"):
        self.parser = configparser.ConfigParser()

        if not self.parser.read(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        # Flask settings
        self.SECRET_KEY = self.parser.get("flask", "secret_key")
        self.DEBUG = self.parser.getboolean("flask", "debug")

        # Storage settings — resolve to absolute path
        raw_pdfs_folder = self.parser.get("storage", "pdfs_folder")
        self.PDFS_FOLDER = os.path.abspath(raw_pdfs_folder)
        raw_thumbnails_folder = self.parser.get("storage", "thumbnails_folder")
        self.THUMBNAILS_FOLDER = os.path.abspath(raw_thumbnails_folder)

        max_mb = self.parser.getint("storage", "max_content_length_mb")
        self.MAX_CONTENT_LENGTH_MB = max_mb 

        # Ensure the folder exists
        os.makedirs(self.PDFS_FOLDER, exist_ok=True)
        os.makedirs(self.THUMBNAILS_FOLDER, exist_ok=True)