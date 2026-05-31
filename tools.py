from pathlib import Path
import pymupdf
import sys


def old_pdf_to_images(inPdfFile:str, outDir:str):
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

def pdf_to_images(inPdfFile:str, outDir:str):
    doc = pymupdf.open(inPdfFile)
    ipath = Path(inPdfFile)
    opath = Path(outDir)
    stem = ipath.stem
    rtn = []
    i = 0
    for page in doc:
        image_list = page.get_images(full=True)
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            i = i + 1
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]  # Raw bytes
            image_ext = base_image["ext"]
            nfn = str(stem) + f"_{i+1}.{image_ext}"
            ofn = opath / nfn
            rtn.append({"page":i+1, "file":f"{ofn}"})
            with open(ofn, "wb") as f:
                f.write(image_bytes)

    return rtn

def pdf_image_pull(inPdfFile:str, outDir:str):
    doc = pymupdf.open(inPdfFile)
    ipath = Path(inPdfFile)
    opath = Path(outDir)
    stem = ipath.stem
    rtn = []
    for i, page in enumerate(doc):
        
        ocr_res  = page.get_pixmap(matrix=pymupdf.Matrix(300/72, 300/72))
        ocr_fn = str(stem) + f"_{i+1}-ocr.png"
        ocr_path = opath / ocr_fn
        ocr_bytes = ocr_res.tobytes("png")
        with open(ocr_path, "wb") as tf:
                tf.write(ocr_bytes)

        thumb_res = page.get_pixmap(matrix=pymupdf.Matrix(0.5, 0.5))
        thumb_fn = str(stem) + f"_{i+1}-thumb.png"
        thumb_path = opath / thumb_fn
        thumb_bytes = thumb_res.tobytes("png")   # in-memory, no disk write
        with open(thumb_path, "wb") as tf:
                tf.write(thumb_bytes)
        rtn.append({"page":i+1, "thumb":f"{thumb_fn}", "ocr":f"{ocr_fn}"})
        



images = pdf_image_pull(sys.argv[1], sys.argv[2])
"both..."
print(images)