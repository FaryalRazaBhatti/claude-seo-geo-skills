#!/usr/bin/env python3
"""Copy the shared files into every skill so each one works on its own,
then zip each skill (and the full set) into dist/.

Run from the repo root:  python3 scripts/build.py
Use --check to fail if any skill's copies are out of date.
"""
import shutil, sys, zipfile, filecmp
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
VOICE_SKILLS = {"content-planner", "content-writer", "content-refresh", "seo-geo-system"}

def wanted(skill):
    files = {
        SHARED / "google-guidance.md": skill / "references" / "google-guidance.md",
        SHARED / "site-profile.md": skill / "templates" / "site-profile.md",
    }
    if skill.name in VOICE_SKILLS:
        files[SHARED / "voice.md"] = skill / "templates" / "voice.md"
    return files

def main():
    check = "--check" in sys.argv
    stale = []
    skills = sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists())
    for skill in skills:
        for src, dst in wanted(skill).items():
            if check:
                if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
                    stale.append(str(dst.relative_to(ROOT)))
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
    if check:
        if stale:
            print("Out of date:\n  " + "\n  ".join(stale))
            sys.exit(1)
        print("All skills are in sync with shared/.")
        return
    DIST.mkdir(exist_ok=True)
    for skill in skills:
        with zipfile.ZipFile(DIST / f"{skill.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(SKILLS))
    with zipfile.ZipFile(DIST / "all-skills.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for skill in skills:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(SKILLS))
    print(f"Built {len(skills)} skills into dist/")

if __name__ == "__main__":
    main()
