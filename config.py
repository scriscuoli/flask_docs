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
        raw_pages_folder = self.parser.get("storage", "pages_folder")
        self.PAGES_FOLDER = os.path.abspath(raw_pages_folder)

        max_mb = self.parser.getint("storage", "max_content_length_mb")
        self.MAX_CONTENT_LENGTH_MB = max_mb 

        # Ensure the folder exists
        os.makedirs(self.PDFS_FOLDER, exist_ok=True)
        os.makedirs(self.PAGES_FOLDER, exist_ok=True)

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
            pages_subfolder = f"{self.PAGES_FOLDER}{os.sep}{subdir}"
            if folder_only:
                rtn = pages_subfolder
            else:
                rtn = str(os.path.join(pages_subfolder, filename))

        return rtn
    
if __name__ == "__main__":
    cfg = Config("config.ini")

    pdf_file="08012026000000.pdf"
    pdf_dir = cfg.get_file_location(pdf_file,folder_only=True)
    full_pdf = cfg.get_file_location(pdf_file)
    print(f"{pdf_file} is at {full_pdf}")
    print(f"folder is  {pdf_dir}")

    pages_file = "05192026000000-01.png"
    pages_dir = cfg.get_file_location(pages_file,folder_only=True)
    full_thm = cfg.get_file_location(pages_file)
    print(f"{pages_file} is at {full_thm}")
    print(f"folder is  {pages_dir}")


    
