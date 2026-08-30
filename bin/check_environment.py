#!/usr/bin/env python3
"""Check runtime, dependencies for duizuo-reading-companion."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

def main() -> int:
    parser = argparse.ArgumentParser(description="duizuo environment check")
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--check-updates", action="store_true", help="also run 24h throttled update checker (non-blocking)")
    args = parser.parse_args()
    checks: list[dict[str, Any]] = []
    errors: list[str] = []

    def record(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "ok": ok, "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}")

    record("python", sys.version_info >= (3, 10), f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    skill_md = args.skill_root / "SKILL.md"
    record("skill-md", skill_md.is_file(), str(skill_md))
    for ref in ["references/storage.md", "references/archiving.md", "references/content-types.md", "references/spoiler-and-evidence.md"]:
        p = args.skill_root / ref
        record(ref, p.is_file(), "exists" if p.is_file() else "missing")

    update_info = None
    if args.check_updates:
        try:
            import subprocess as _sp
            import sys as _sys_check
            checker = args.skill_root / "bin" / "check_updates.py"
            if checker.exists():
                proc = _sp.run([_sys_check.executable, str(checker), "--json"], capture_output=True, text=True, timeout=12)
                if proc.returncode == 0 and proc.stdout.strip():
                    import json as _json
                    update_info = _json.loads(proc.stdout.strip())
                    if isinstance(update_info, dict) and update_info.get("update_available"):
                        record("update-available", True, f"{update_info.get('repo')} {update_info.get('remote_sha')} newer than {update_info.get('local_sha')} — run gh skill update duizuo-reading-companion")
                    else:
                        record("update-available", True, f"up to date {update_info.get('local_sha') if isinstance(update_info, dict) else 'ok'}")
        except Exception as _e:
            record("update-available", True, f"update check skipped: {_e}")

    report = {"ok": not errors, "checks": checks, "errors": errors}
    if update_info is not None:
        report["update"] = update_info
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for item in checks:
            print(f"{'PASS' if item['ok'] else 'FAIL'} {item['name']}: {item['detail']}")
        print("Environment check passed" if not errors else "Environment check failed")
    return 0 if not errors else 2

if __name__ == "__main__":
    raise SystemExit(main())
