
import requests
import json
import time
import os

BASE_URL = "http://127.0.0.1:8000"
WEBHOOK_URL = f"{BASE_URL}/calls/webhook"

def run_simulation():
    print(f"🚀 Starting Field Service AI Checkout Simulation...")
    print(f"📡 Target: {WEBHOOK_URL}")

    # 1. Health Check
    try:
        resp = requests.get(f"{BASE_URL}/health")
        if resp.status_code != 200:
            print("❌ Server is not running or unhealthy.")
            return
        print("✅ Server Status: ONLINE")
    except Exception:
        print("❌ Could not connect to server. Make sure it's running: 'uvicorn app.main:app --reload'")
        return

    # 2. Define Realistic Field Service Payload
    # Scenario: Technician completing a plumbing job
    call_id = f"call_{int(time.time())}_plumbing"
    
    payload = {
        "call_id": call_id,
        "metadata": {
            "technician_id": "TECH-1042",
            "job_location": "123 Main St, Seattle, WA",
            "job_type": "maintenance"
        },
        "transcripts": [
            {
                "id": 1,
                "text": "Hey there, I see you've wrapped up at the site. Can you tally up the work for the invoice?",
                "user": "agent",
                "timestamp": 1000.0
            },
            {
                "id": 2,
                "text": "Yeah, job's done. I successfully replaced the leaking P-trap under the kitchen sink.",
                "user": "user",
                "timestamp": 1005.5
            },
            {
                "id": 3,
                "text": "Great. any parts used from the truck?",
                "user": "agent",
                "timestamp": 1010.2
            },
            {
                "id": 4,
                "text": "I had to use three copper fittings and purchase a new valve.",
                "user": "user",
                "timestamp": 1015.0
            },
            {
                "id": 5,
                "text": "Got it. Three fittings and a valve. I'll generate the invoice now.",
                "user": "agent",
                "timestamp": 1020.0
            }
        ],
        "analyzers": [
            {
                "id": "analyzer_intent_1",
                "type": "intent_recognition",
                "instruction": "Identify if the job is complete or incomplete."
            },
            {
                "id": "analyzer_checkout_1",
                "type": "checkout_completion",
                "instruction": "Extract work done and parts used from technician speech."
            }
        ]
    }

    print("\n📞 Simulating Checkout Call...")
    print("------------------------------------------------")
    for t in payload["transcripts"]:
        role = "🤖 Agent" if t["user"] == "agent" else "👨‍🔧 Tech"
        print(f"{role}: {t['text']}")
    print("------------------------------------------------")

    print("🧾 Work Narration Sent. Processing...")
    
    # 3. Send Request
    start_time = time.time()
    response = requests.post(WEBHOOK_URL, json=payload)
    duration = time.time() - start_time

    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ API Response Received in {duration:.4f}s")
        
        # 4. Print Analysis Results
        print("\n🧠 Analyzer Engine Results:")
        print(f"   📝 Summary: {data.get('summary', 'No summary generated')}")
        
        print("   🔍 Structured Extractions:")
        for res in data.get('analysis_results', []):
            print(f"     - [{res['analyzer_id']}]: {json.dumps(res['result'])}")
        
        # 5. Check Output Artifacts (Background Tasks)
        print("\n📦 Waiting for inventory update & invoice generation...")
        time.sleep(2.5) # Allow background worker to finish
        
        invoice_path = f"generated_invoices/invoice_{call_id}.pdf"
        if os.path.exists(invoice_path):
            print(f"   ✅ Invoice PDF successfully generated: {invoice_path}")
            print(f"      (Simulated upload to S3/Blob Storage would happen here)")
        else:
            print(f"   ❌ Invoice PDF missing at {invoice_path}")
            
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    run_simulation()
