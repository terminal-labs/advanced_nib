import os
import tempfile
import shutil

import pdfkit
from xvfbwrapper import Xvfb

from lxccloud.settings import TEMPLATE_DIR
from lxccloud.utils import file_read


def render_pdf_html():
    templatepath = os.path.join(TEMPLATE_DIR, "invoice.html")
    html = file_read(os.path.abspath(templatepath))
    html = html.decode("utf-8")
    html = html.replace("\n", "")
    html = html.replace("\t", "")
    return html


def generate_pdf(html):
    dirpath = tempfile.mkdtemp()

    with open(os.path.join(dirpath, "test.html"), "w") as f:
        f.write(html)

    vdisplay = Xvfb()
    vdisplay.start()
    pdfkit.from_file(os.path.join(dirpath, "test.html"), os.path.join(dirpath, "out.pdf"))
    vdisplay.stop()

    with open(os.path.join(dirpath, "out.pdf"), "rb") as f:
        content = f.read()

    shutil.rmtree(dirpath)
    return content
