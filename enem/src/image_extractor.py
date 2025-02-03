import fitz
from typing import Union
import os
dimlimit = 0
abssize = 0
relsize = 0

"""
(c) 2024 Pedro L. Dias
https://github.com/diaslui/

-----------------------------------------------------------------------

Parts of this code were forked from PyMuPDF project:
https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/examples/extract-images/extract-from-pages.py
under GNU GPL V3 license.

"""

def recoverpix(doc, item):
    xref = item[0]  # xref of PDF image
    smask = item[1]  # xref of its /SMask

    # special case: /SMask or /Mask exists
    if smask > 0:
        pix0 = fitz.Pixmap(doc.extract_image(xref)["image"])
        if pix0.alpha:  # catch irregular situation
            pix0 = fitz.Pixmap(pix0, 0)  # remove alpha channel
        mask = fitz.Pixmap(doc.extract_image(smask)["image"])

        try:
            pix = fitz.Pixmap(pix0, mask)
        except:  # fallback to original base image in case of problems
            pix = fitz.Pixmap(doc.extract_image(xref)["image"])

        if pix0.n > 3:
            ext = "pam"
        else:
            ext = "png"

        return {  # create dictionary expected by caller
            "ext": ext,
            "colorspace": pix.colorspace.n,
            "image": pix.tobytes(ext),
        }

    # special case: /ColorSpace definition exists
    # to be sure, we convert these cases to RGB PNG images
    if "/ColorSpace" in doc.xref_object(xref, compressed=True):
        pix = fitz.Pixmap(doc, xref)
        pix = fitz.Pixmap(fitz.csRGB, pix)
        return {  # create dictionary expected by caller
            "ext": "png",
            "colorspace": 3,
            "image": pix.tobytes("png"),
        }
    return doc.extract_image(xref)

def resolve_image(image_output_path, page, doc, img) -> Union[dict, None]:
    """
    This function is responsible for extracting image data and saving it.

    :param image_output_path: str path to save the image
    :param page: page object
    :param doc: document object
    :param img: dict image data
    :return: dict | None
    """
    xref = img[0]
    try:
        page.get_image_rects(xref)
    except Exception as e:
        return None

    width = img[2]
    height = img[3]
    if min(width, height) <= dimlimit:
        return None
    
    image = recoverpix(doc, img)
    n = image["colorspace"]
    imgdata = image["image"]

    if len(imgdata) <= abssize:
        return None
    if len(imgdata) / (width * height * n) <= relsize:
        return None
    if image["ext"] == "jb2":
        return None

    imgfile = os.path.join(image_output_path, "img%05i.%s" % (xref, image["ext"]))
    fout = open(imgfile, "wb")
    fout.write(imgdata)
    fout.close()

    return {
        "xref": xref,
        "width": width,
        "height": height,
        "imagePath": os.path.abspath(imgfile)
    }