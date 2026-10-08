import json
import os
from pathlib import Path

def load(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data,dict):raise RuntimeError("Expected JSON dict")
    return data

doctor=load(os.environ["REA_DOCTOR_REPORT"])
result=load(os.environ["REA_NATIVE_REPORT"])
checks={
    "ghidra_readiness": doctor.get("healthy") is True,
    "native_evidence_present": bool(result.get("evidence_id")),
    "native_operation": "native" in str(result.get("operation","")).lower() or result.get("provider") not in (None, ""),
    "fixture_identified": ("sample.elf" in json.dumps(result).lower()),
}
summary={"status":"PASS" if all(checks.values()) else "FAIL", "checks":checks,
         "provider":str(result.get("provider"))[:130], "operation":result.get("operation"),
         "scope":"synthetic x86-64 ELF fixture; does not prove other formats"}
Path("lab-result.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary))
if not all(checks.values()):raise SystemExit(1)
