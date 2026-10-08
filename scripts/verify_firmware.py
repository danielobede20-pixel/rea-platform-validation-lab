import json
from pathlib import Path

def load(path):
    obj=json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(obj,dict):raise ValueError("not JSON object")
    return obj

scan=load("firmware-inspect.json")
extract=load("firmware-extract.json")
checks={
    "scan_evidence":bool(scan.get("evidence_id")),
    "scan_operation":scan.get("operation")=="inspect_firmware_regions",
    "gzip_signature_observed":"gzip" in json.dumps(scan).lower(),
    "extract_evidence":bool(extract.get("evidence_id")),
    "extract_operation":extract.get("operation")=="extract_firmware",
}
res={"status":"PASS" if all(checks.values()) else "FAIL","checks":checks,
     "scope":"only synthetic gzip firmware-like blob; not real firmware validation"}
print(json.dumps(res))
if not all(checks.values()):raise SystemExit(1)
