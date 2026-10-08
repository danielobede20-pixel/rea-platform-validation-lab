import json
from pathlib import Path

def read(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data,dict):raise RuntimeError("invalid evidence")
    return data

package=read("android.json")
classes=read("classes.json")
checks={
    "package_evidence":bool(package.get("evidence_id")),
    "class_search_evidence":bool(classes.get("evidence_id")),
    "apk_name_in_evidence":"sample.apk" in json.dumps(package).lower(),
    "leadscore_class_found":"LeadScore" in json.dumps(classes),
}
result={"status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"scope":"synthetic APK only; no arbitrary app guarantee"}
print(json.dumps(result))
if not all(checks.values()):raise SystemExit(1)
