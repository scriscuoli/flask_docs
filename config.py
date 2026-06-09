import configparser
import os

class Config:
    def __init__(self, config_path=None):

        if config_path == None:
           config_path = os.path.join(os.path.dirname(__file__), "config.ini")
            
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

    def get_year_month(self,filename):
        # Remove extension and parse: MMDDYYYYhhmmss
        stem = filename.rsplit('.', 1)[0]
        mm = stem[0:2]
        yyyy = stem[4:8]
        return f"{yyyy}{os.sep}{mm}"
    
    # given MMDDYYYYhhmmss.pdf return PDFS_FOLDER/YYYY/MM/MMDDYYYYhhmmss.pdf
    # 
    def get_file_location(self,filename:str,folder_only=False):
        rtn = ""
        if filename.upper().endswith(".PDF"):
            subdir = self.get_year_month(filename)
            pdfs_subfolder = f"{self.PDFS_FOLDER}{os.sep}{subdir}"
            if folder_only:
                rtn = pdfs_subfolder
            else:
                rtn = str(os.path.join(pdfs_subfolder, filename))
        elif filename.upper().endswith(".PNG"):
            subdir = self.get_year_month(filename)
            thumbnail_subfolder = f"{self.THUMBNAILS_FOLDER}{os.sep}{subdir}"
            if folder_only:
                rtn = thumbnail_subfolder
            else:
                rtn = str(os.path.join(thumbnail_subfolder, filename))

        return rtn
    
if __name__ == "__main__":
    cfg = Config("config.ini")

    pdf_file="08012026000000.pdf"
    pdf_dir = cfg.get_file_location(pdf_file,folder_only=True)
    full_pdf = cfg.get_file_location(pdf_file)
    print(f"{pdf_file} is at {full_pdf}")
    print(f"folder is  {pdf_dir}")

    thumbnail_file = "05192026000000-01.png"
    thumbnail_dir = cfg.get_file_location(thumbnail_file,folder_only=True)
    full_thm = cfg.get_file_location(thumbnail_file)
    print(f"{thumbnail_file} is at {full_thm}")
    print(f"folder is  {thumbnail_dir}")


    
