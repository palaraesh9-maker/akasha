from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import swisseph as swe
import shutil
import os

app = FastAPI(title="ആകാശദീപ്തം സമഗ്ര പ്ലാറ്റ്‌ഫോം", version="4.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ഫ്രണ്ട്എൻഡ് HTML കോഡ്
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ml">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ആകാശദീപ്തം - സമ്പൂർണ്ണ ജാതക & ലക്ഷണ വിശകലന പ്ലാറ്റ്‌ഫോം</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 15px; }
        .container { max-width: 650px; margin: 0 auto; background: rgba(30, 41, 59, 0.95); padding: 20px; border-radius: 16px; border: 1px solid rgba(56, 189, 248, 0.3); box-shadow: 0 20px 40px rgba(0,0,0,0.7); }
        h1 { text-align: center; color: #38bdf8; font-size: 22px; }
        p.subtitle { text-align: center; color: #94a3b8; font-size: 12px; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 6px; color: #cbd5e1; font-size: 13px; font-weight: 600; }
        input, select, textarea { width: 100%; padding: 10px; box-sizing: border-box; background: #1e293b; border: 1px solid #475569; color: #fff; border-radius: 8px; font-size: 14px; }
        .date-row { display: flex; gap: 8px; }
        .date-row select, .date-row input { flex: 1; }
        .time-row { display: flex; gap: 8px; align-items: center; }
        .submit-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #7c3aed, #0284c7); color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 15px; }
        #result-section { display: none; margin-top: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
        .card h3 { color: #c084fc; margin-top: 0; font-size: 15px; border-bottom: 1px solid #334155; padding-bottom: 6px; }
        .card p, .card li { font-size: 13px; color: #e2e8f0; line-height: 1.5; }
    </style>
</head>
<body>
<div class="container">
    <h1>ആകാശദീപ്തം</h1>
    <p class="subtitle">പ്രപഞ്ചത്തിന്റെ വെളിച്ചം - ജ്യോതിഷ & ലക്ഷണം</p>
    
    <div id="form-section">
        <div class="form-group">
            <label>മുഴുവൻ പേര്:</label>
            <input type="text" id="name" placeholder="പേര് നൽകുക">
        </div>
        <div class="form-group">
            <label>ജനനത്തീയതി (ദിവസം / മാസം / വർഷം):</label>
            <div class="date-row">
                <select id="day"><option value="" disabled selected>ദിവസം</option><script>for(let i=1; i<=31; i++) document.write(`<option value="${i}">${i}</option>`);</script></select>
                <select id="month"><option value="" disabled selected>മാസം</option><script>const m=["ജനുവരി","ഫെബ്രുവരി","മാർച്ച്","ഏപ്രിൽ","മെയ്","ജൂൺ","ജൂലൈ","ഓഗസ്റ്റ്","സെപ്റ്റംബർ","ഒക്ടോബർ","നവംബർ","ഡിസംബർ"];for(let i=0;i<12;i++)document.write(`<option value="${i+1}">${m[i]}</option>`);</script></select>
                <input type="number" id="year" placeholder="വർഷം">
            </div>
        </div>
        <div class="form-group">
            <label>ജനന സമയം (മണിക്കൂർ, മിനിറ്റ് & AM/PM):</label>
            <div class="time-row">
                <input type="number" id="hour" placeholder="മണിക്കൂർ (1-12)" min="1" max="12">
                <input type="number" id="minute" placeholder="മിനിറ്റ് (0-59)" min="0" max="59">
                <select id="ampm"><option value="AM">AM</option><option value="PM" selected>PM</option></select>
            </div>
        </div>
        <div class="form-group">
            <label>ജനന സ്ഥലം:</label>
            <input type="text" id="place_name" value="Pathanamthitta" placeholder="സ്ഥലം">
        </div>
        <div class="form-group">
            <label>ലിംഗം:</label>
            <select id="gender"><option value="Male">പുരുഷൻ</option><option value="Female">സ്ത്രീ</option></select>
        </div>
        <div class="form-group">
            <label>കൈരേഖയോ മുഖമോ സ്കാൻ ചെയ്യാനുള്ള ചിത്രം (ഓപ്ഷണൽ):</label>
            <input type="file" id="scan_image" accept="image/*">
        </div>
        <button class="submit-btn" onclick="calculateHoroscope()">വിശകലനം ആരംഭിക്കുക</button>
    </div>

    <div id="result-section">
        <h2 style="color: #38bdf8; font-size: 18px; text-align: center;">റിപ്പോർട്ട്</h2>
        <div class="card">
            <h3>അടിസ്ഥാന വിവരങ്ങൾ</h3>
            <ul>
                <li>പേര്: <strong id="res_name" style="color:#38bdf8;"></strong></li>
                <li>നക്ഷത്രം: <strong id="res_nakshatra"></strong></li>
                <li>ലഗ്നം: <strong id="res_lagna"></strong></li>
                <li>ചിത്ര വിശകലനം: <strong id="res_img" style="color:#4ade80;"></strong></li>
            </ul>
        </div>
    </div>
</div>

<script>
async function calculateHoroscope() {
    const name = document.getElementById('name').value;
    const year = document.getElementById('year').value;
    const month = document.getElementById('month').value;
    const day = document.getElementById('day').value;
    if(!name || !year || !month || !day) { alert('എല്ലാ വിവരങ്ങളും പൂരിപ്പിക്കുക!'); return; }

    let hour = parseInt(document.getElementById('hour').value || 12);
    const minute = parseInt(document.getElementById('minute').value || 0);
    if(document.getElementById('ampm').value === "PM" && hour < 12) hour += 12;

    const formData = new FormData();
    formData.append("name", name);
    formData.append("gender", document.getElementById('gender').value);
    formData.append("year", parseInt(year));
    formData.append("month", parseInt(month));
    formData.append("day", parseInt(day));
    formData.append("hour", hour);
    formData.append("minute", minute);
    formData.append("lat", 9.2648);
    formData.append("lon", 76.7870);
    formData.append("focus", "പൊതുഫലം");
    
    const img = document.getElementById('scan_image').files[0];
    if(img) formData.append("scan_image", img);

    try {
        const response = await fetch('/calculate', { method: 'POST', body: formData });
        const result = await response.json();
        if(result.status === "success") {
            document.getElementById('res_name').innerText = result.name;
            document.getElementById('res_nakshatra').innerText = result.nakshatra;
            document.getElementById('res_lagna').innerText = result.lagna;
            document.getElementById('res_img').innerText = result.image_analysis;
            document.getElementById('form-section').style.display = 'none';
            document.getElementById('result-section').style.display = 'block';
        } else {
            alert('ഗണനകളിൽ പിശക് സംഭവിച്ചു.');
        }
    } catch(e) {
        alert('സർവറുമായി ബന്ധപ്പെടാൻ കഴിഞ്ഞില്ല!');
        console.error(e);
    }
}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    return HTML_CONTENT

@app.post("/calculate")
async def calculate_horoscope(
    name: str = Form(...),
    gender: str = Form(...),
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    minute: int = Form(...),
    lat: float = Form(...),
    lon: float = Form(...),
    focus: str = Form("പൊതുഫലം"),
    scan_image: UploadFile = File(None)
):
    try:
        hour_decimal = hour + (minute / 60.0) - 5.5
        jd = swe.julday(year, month, day, hour_decimal)
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        
        moon_pos, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
        nak_list = ["അശ്വതി", "ഭരണി", "കാർത്തിക", "രോഹിണി", "മകയിരം", "തിരുവാതിര", "പുണർതം", "പൂയം", "ആയില്യം", "മകം", "പൂരം", "ഉത്രം", "അത്തം", "ചിത്തിര", "ചോതി", "വിശാഖം", "അനിഴം", "തൃക്കേട്ട", "മൂലം", "പൂരാടം", "ഉത്രാടം", "തിരുവോണം", "അവിട്ടം", "ചതയം", "പൂരുരുട്ടാതി", "ഉത്രട്ടാതി", "രേവതി"]
        nak_name = nak_list[int(moon_pos[0] / (360.0 / 27.0)) % 27]
        
        houses, ascmc = swe.houses(jd, lat, lon, b'P')
        ay = swe.get_ayanamsa_ut(jd)
        zodiac = ["മേടം", "ഇടവം", "മിഥുനം", "കർക്കടകം", "ചിങ്ങം", "കന്നി", "തുലാം", "വൃശ്ചികം", "ധനു", "മകരം", "കുംഭം", "മീനം"]
        lagna_name = zodiac[int(((ascmc[0] - ay) % 360) / 30.0)]

        img_status = "ചിത്രം നൽകിയിട്ടില്ല"
        if scan_image:
            file_path = os.path.join(UPLOAD_DIR, scan_image.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(scan_image.file, buffer)
            img_status = f"ലഭിച്ചു: {scan_image.filename}"

        return {
            "status": "success",
            "name": name,
            "nakshatra": nak_name,
            "lagna": lagna_name,
            "image_analysis": img_status
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
