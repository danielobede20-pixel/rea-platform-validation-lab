import gzip
from pathlib import Path
payload=b"SYNTHETIC-HERMES-REVERSE-LAB\n"+"BASIC-PAYLOAD-ONLY\n".encode()*256
prefix=b"LAB-FIRMWARE-HEADER".ljust(512,b"\0")
Path("firmware-sample.bin").write_bytes(prefix+gzip.compress(payload,mtime=0))
print("synthetic_firmware_bytes",Path("firmware-sample.bin").stat().st_size)
