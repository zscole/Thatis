
# DiagJet Backend (FastAPI)

## اجرای لوکال:
1. نصب پکیج‌ها:
   pip install -r requirements.txt

2. اجرا:
   uvicorn main:app --reload

## Endpoint:
POST /diagnose
Body: { "issue": "your description" }
