from pathlib import Path
import pymupdf
import sys


def pdf_to_images(inPdfFile:str, outDir:str):
    doc = pymupdf.open(inPdfFile)
    ipath = Path(inPdfFile)
    opath = Path(outDir)
    stem = ipath.stem
    rtn = []
    for i,page in enumerate(doc):
        pix = page.get_pixmap()
        nfn = str(stem) + f"_{i+1}.png"
        ofn = opath / nfn
        print(f"Saving to {ofn}")
        rtn.append({"page":i+1, "file":f"{ofn}"})
        pix.save(ofn)
    return rtn


images = pdf_to_images(sys.argv[1], sys.argv[2])
print(images)