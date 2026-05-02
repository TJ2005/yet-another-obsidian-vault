from pypdf import PdfReader
from pypdf.generic import IndirectObject
from pathlib import Path

pdf = Path(r"D:\tijo\Tijo's notebook\Private\Staging Chamber\Rema\K005_Malware_Analysis_Report_REMA_Exp8.pdf")
if not pdf.exists():
    print(f"File not found: {pdf}")
    exit(1)

r = PdfReader(str(pdf))
print(f"PAGES: {len(r.pages)}")

def count_images(page):
    res = page.get("/Resources")
    if not res: return 0
    xobj = res.get("/XObject")
    if not xobj: return 0
    if isinstance(xobj, IndirectObject): 
        xobj = xobj.get_object()
    c = 0
    for _, obj in xobj.items():
        if isinstance(obj, IndirectObject): 
            obj = obj.get_object()
        if obj.get("/Subtype") == "/Image": 
            c += 1
    return c

for i, p in enumerate(r.pages, 1):
    try:
        x_count = count_images(p)
        p_images_count = len(list(p.images))
        print(f"{i} xobj_images {x_count} page.images {p_images_count}")
    except Exception as e:
        print(f"{i} err {type(e).__name__}: {e}")
