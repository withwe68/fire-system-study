import os
import fitz

BASE_DIR = r"D:\Github\fire-system-study"
IMG_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

PDF_GUIDE_1 = os.path.join(BASE_DIR, "1._2024년_화재안전기술기준_해설서_제1권.pdf")
PDF_GUIDE_APP_A = os.path.join(BASE_DIR, "3._2024년_화재안전기술기준_해설서_부록_A.pdf")

# 인쇄 쪽수와 100% 일치하는 정밀 좌표 세팅
TARGETS = [
    {
        # 부록 A 55쪽: 상단의 압력스위치 Range/Diff 구조 사진 (하단 텍스트 제외)
        "filename": "day04_switch.png",
        "pdf": PDF_GUIDE_APP_A,
        "page": 55,
        "crop": (0.05, 0.08, 0.95, 0.45)
    },
    {
        # 제1권 46쪽: 하단의 고압유지방식 세팅 그래프
        "filename": "day04_graph.png",
        "pdf": PDF_GUIDE_1,
        "page": 46,
        "crop": (0.05, 0.50, 0.95, 0.95)
    },
    {
        # 제1권 40쪽: 상단의 압력챔버 계통도 및 외형 구조 사진
        "filename": "day04_chamber.png",
        "pdf": PDF_GUIDE_1,
        "page": 40,
        "crop": (0.05, 0.08, 0.95, 0.65)
    }
]

for item in TARGETS:
    if os.path.exists(item["pdf"]):
        doc = fitz.open(item["pdf"])
        page = doc[item["page"] - 1]
        
        w, h = page.rect.width, page.rect.height
        c = item["crop"]
        clip_rect = fitz.Rect(w * c[0], h * c[1], w * c[2], h * c[3])
        
        # 2배 확대 고화질 렌더링
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=clip_rect)
        out_path = os.path.join(IMG_DIR, item["filename"])
        pix.save(out_path)
        print(f"🎯 [정상 크롭 완료] {item['filename']} (페이지: {item['page']})")
        doc.close()
    else:
        print(f"❌ [파일 없음] {item['pdf']}")
