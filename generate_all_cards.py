import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"D:\Github\fire-system-study"
IMG_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

# 폰트 경로 (맑은 고딕 기본)
font_bold = "C:/Windows/Fonts/malgunbd.ttf"
font_regular = "C:/Windows/Fonts/malgun.ttf"

def create_card(filename, title, subtitle, main_boxes, bg_color="#F1F3F5", card_color="#FFFFFF"):
    width, height = 900, 1100
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        f_title = ImageFont.truetype(font_bold, 36)
        f_sub = ImageFont.truetype(font_bold, 22)
        f_box_title = ImageFont.truetype(font_bold, 26)
        f_box_text = ImageFont.truetype(font_regular, 22)
        f_footer = ImageFont.truetype(font_regular, 18)
    except:
        f_title = f_sub = f_box_title = f_box_text = f_footer = ImageFont.load_default()
    
    card_margin = 35
    draw.rounded_rectangle([(card_margin, card_margin), (width - card_margin, height - card_margin)], radius=24, fill=card_color, outline="#CED4DA", width=2)
    draw.rounded_rectangle([(card_margin, card_margin), (width - card_margin, 145)], radius=24, fill="#003366")
    draw.rectangle([(card_margin, 120), (width - card_margin, 145)], fill="#003366")
    draw.text((65, 65), title, font=f_title, fill="#FFFFFF")
    draw.text((65, 165), subtitle, font=f_sub, fill="#495057")
    
    start_y = 215
    for box in main_boxes:
        b_title = box.get("title", "")
        b_lines = box.get("lines", [])
        box_h = 42 + len(b_lines) * 38 + 18
        box_bg = box.get("bg", "#F8F9FA")
        box_border = box.get("border", "#DEE2E6")
        draw.rounded_rectangle([(65, start_y), (width - 65, start_y + box_h)], radius=12, fill=box_bg, outline=box_border, width=2)
        draw.text((88, start_y + 14), b_title, font=f_box_title, fill=box.get("title_color", "#003366"))
        line_y = start_y + 52
        for line in b_lines:
            draw.text((88, line_y), line, font=f_box_text, fill="#212529")
            line_y += 38
        start_y += box_h + 16
        
    draw.text((65, height - 65), "소방시설관리사 2차 점검실무행정 · NFTC 기술기준", font=f_footer, fill="#868E96")
    out_path = os.path.join(IMG_DIR, filename)
    img.save(out_path, quality=95)
    print(f"✅ [PNG 생성 완료] {filename}")

# --- [Day 02 암기카드] ---
create_card(
    "card_day02_front.png", "[Day 02] 배관구경 및 방수성능 (앞면)", "Q. 핵심 수치와 암기 공식을 머릿속으로 인출해보세요.",
    [
        {"title": "Q1. 법정 방수압력 및 방수량 기준은?", "lines": ["• 노즐 선단 방수압력 범위는?", "• 분당 법정 최소 방수량은?", "• 피토게이지 방수량(Q) 계산식은?"], "title_color": "#003366"},
        {"title": "Q2. 배관 구경 및 밸브 기준은?", "lines": ["• 주배관 유속 / 수직배관 구경 / 가지배관 구경은?", "• 방수구 인입측 감압장치 설치 기준 압력은?", "• 펌프 흡입측에 버터플라이밸브 설치 금지 이유는?"], "title_color": "#003366"},
        {"title": "💡 인출 힌트 (두문자 암기 공식)", "lines": ["• 배관구경: 수오-가사-주오사", "• 감압기준: 영칠 초과 시 오·밸 감압"], "bg": "#FFF9DB", "border": "#FFE066", "title_color": "#D9480F"}
    ]
)
create_card(
    "card_day02_back.png", "[Day 02] 배관구경 및 방수성능 (뒷면)", "A. 핵심 정답 및 점검 기준 요약",
    [
        {"title": "A1. 방수성능 및 측정 기준", "lines": ["• 방수압: 0.17 MPa 이상 0.7 MPa 이하", "• 방수량: 130 L/min 이상", "• 피토게이지 공식: Q = 2.086 × d² × √P (d=13㎜, D/2 측정)"], "title_color": "#0B7285"},
        {"title": "A2. 배관 구경 및 감압 기준", "lines": ["• 수직 50㎜ 이상, 가지 40㎜ 이상, 주배관 유속 4m/s 이하", "• 노즐 선단 압력 0.7 MPa 초과 시 감압장치(오리피스·밸브) 설치", "• 흡입측 버터플라이 금지: 와류로 인한 캐비테이션 방지"], "title_color": "#0B7285"},
        {"title": "⚠️ 자체점검표(2-C-002, 2-C-003) 판정 사례", "lines": ["• 0.17 MPa 미달 시 양정 부족 불량", "• 0.7 MPa 초과 시 호스 파손 및 조작자 전도 위험 불량"], "bg": "#FFF5F5", "border": "#FFA8A8", "title_color": "#C92A2A"}
    ]
)

# --- [Day 03 암기카드] ---
create_card(
    "card_day03_front.png", "[Day 03] 수원량 산정 및 옥상수조 (앞면)", "Q. 핵심 수치와 암기 공식을 머릿속으로 인출해보세요.",
    [
        {"title": "Q1. 주된 수원량 산정 공식 및 층수별 기준은?", "lines": ["• 기본 유효수량 산정 공식은? (N 최대 기준)", "• 30~49층(준초고층) 및 50층 이상(초고층) 가산 기준은?"], "title_color": "#003366"},
        {"title": "Q2. 옥상수조 기준 및 겸용수조 유효수량은?", "lines": ["• 옥상수조 법정 확보 수량 비율은?", "• 타 설비 겸용수조의 유효수량 판정 구간은?", "• 소화배관 흡수구 상단까지만 인정하는 공학적 이유는?"], "title_color": "#003366"},
        {"title": "💡 인출 힌트 (두문자 암기 공식)", "lines": ["• 옥상수조 제외: 지·고·최·십·예·수·가", "• 수조 부대설비: 수·사·조·배·표"], "bg": "#FFF9DB", "border": "#FFE066", "title_color": "#D9480F"}
    ]
)
create_card(
    "card_day03_back.png", "[Day 03] 수원량 산정 및 옥상수조 (뒷면)", "A. 핵심 정답 및 점검 기준 요약",
    [
        {"title": "A1. 수원량 산정 기준", "lines": ["• 기본: N(최대 2개) × 2.6㎥ 이상 (20분)", "• 30~49층: N × 5.2㎥ (40분) / 50층 이상: N × 7.8㎥ (60분)"], "title_color": "#0B7285"},
        {"title": "A2. 옥상수조 및 겸용수조 판정", "lines": ["• 옥상수조: 주된 수원 유효수량의 1/3 이상 옥상 설치", "• 겸용수조: [타배관 흡수구 하단] ~ [소화배관 흡수구 상단] 사이 수량", "• 흡수구 상단 기준 이유: 수위 저하 시 와류로 인한 공기유입(에어바운딩) 방지"], "title_color": "#0B7285"},
        {"title": "⚠️ 옥상수조 제외 대상 (지고최십예수가)", "lines": ["• 지하층 / 고가수조 / 최상층 방수구 위 / 10m 이하", "• 예비펌프(내연기관·비상전원) / 수동기동 / 가압수조"], "bg": "#FFF5F5", "border": "#FFA8A8", "title_color": "#C92A2A"}
    ]
)

# --- [Day 04 암기카드] ---
create_card(
    "card_day04_front.png", "[Day 04] 압력스위치 세팅 및 충압펌프 (앞면)", "Q. 핵심 수치와 암기 공식을 머릿속으로 인출해보세요.",
    [
        {"title": "Q1. 압력스위치 Range/Diff와 세팅 공식은?", "lines": ["• Range와 Diff 눈금의 정확한 정의는?", "• 주펌프 및 충압펌프의 기동점 설정 수식은?", "• 충압펌프 정지점(Range) 설정 기준은?"], "title_color": "#003366"},
        {"title": "Q2. 실무 판정 및 충압펌프 규격은?", "lines": ["• 2006.12.30 이후 주펌프 자동정지가 금지된 이유는?", "• 충압펌프 토출량을 60 L/min 이하로 제한하는 이유는?"], "title_color": "#003366"},
        {"title": "💡 인출 힌트 (두문자 암기 공식)", "lines": ["• 펌프 압력세팅: 주기-자이, 충기-주오, 주정-수동", "• 충압펌프 규격: 육공 이하, 자이 이상"], "bg": "#FFF9DB", "border": "#FFE066", "title_color": "#D9480F"}
    ]
)
create_card(
    "card_day04_back.png", "[Day 04] 압력스위치 세팅 및 충압펌프 (뒷면)", "A. 핵심 정답 및 점검 기준 요약",
    [
        {"title": "A1. 압력스위치 세팅 공식", "lines": ["• Range = 정지점, Diff = 정지점 - 기동점 (기동점 = Range - Diff)", "• 주펌프 기동점: 자연낙차압 + 0.2 MPa (스프링클러는 +0.15 MPa)", "• 충압펌프 기동점: 주펌프 기동점 + 0.05 MPa 이상 (먼저 기동)", "• 충압펌프 정지점: 주펌프 정격토출압력 수준"], "title_color": "#0B7285"},
        {"title": "A2. 실무 판정 및 충압펌프 사양", "lines": ["• 주펌프 자동정지 금지: 기동/정지 반복 단속운전(소화실패) 방지", "• 충압 토출량 60LPM 이하: 과대 시 방수 중에도 주펌프 미기동 방지", "• 충압 토출압력: 최고위 자연낙차압 + 0.2 MPa 이상"], "title_color": "#0B7285"},
        {"title": "⚠️ 자체점검표(2-C-007) 불량 판정 사례", "lines": ["• 주펌프 기동점이 자연압보다 낮아 감압에도 기동 불능 (물기둥효과)", "• 화재 시 주펌프가 자동정지되도록 세팅된 경우"], "bg": "#FFF5F5", "border": "#FFA8A8", "title_color": "#C92A2A"}
    ]
)
