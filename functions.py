import re
def extract_all_areas(text):
    # Sabhi (Block + Number) patterns निकालेगा, जैसे A1802, B602, D1102, B803
    matches = re.findall(r'([A-D])[- ]?(\d{3,4})', text, re.IGNORECASE)
    return [m[0].upper() + m[1] for m in matches] if matches else []
