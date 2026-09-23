#!/usr/bin/env python3
"""GitHub licence + maintenance audit for Proofline Studio OS research.
Writes research/github-audit.csv (one API call per repo)."""
import json, time, csv, urllib.request, urllib.error, os

REPOS = [
    "nexu-io/open-design", "anthropics/skills", "shadcn-ui/ui", "radix-ui/primitives",
    "mui/base-ui", "tailwindlabs/tailwindcss", "tailwindlabs/headlessui", "withastro/astro",
    "vercel/next.js", "vitejs/vite", "motiondivision/motion", "greensock/GSAP",
    "mrdoob/three.js", "pmndrs/react-three-fiber", "airbnb/lottie-web", "rive-app/rive-react",
    "lucide-icons/lucide", "phosphor-icons/react", "adobe/react-spectrum", "magicuidesign/magicui",
    "formbricks/formbricks", "resend/resend-node", "plausible/analytics", "umami-software/umami",
    "PostHog/posthog", "matomo-org/matomo", "calcom/cal.com", "Thinkmill/keystatic",
    "payloadcms/payload", "decaporg/decap-cms", "dequelabs/axe-core", "pa11y/pa11y",
    "GoogleChrome/lighthouse", "microsoft/playwright", "amzn/style-dictionary",
    "uswds/uswds", "alphagov/govuk-frontend", "carbon-design-system/carbon",
]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "github-audit.csv")
fields = ["repo", "full_name", "license_spdx", "license_name", "stars", "forks",
          "open_issues", "pushed_at", "created_at", "archived", "is_fork",
          "default_branch", "homepage", "topics", "description"]

rows = []
for r in REPOS:
    url = f"https://api.github.com/repos/{r}"
    req = urllib.request.Request(url, headers={"User-Agent": "proofline-research", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.load(resp)
        lic = d.get("license") or {}
        rows.append({
            "repo": r, "full_name": d.get("full_name"), "license_spdx": lic.get("spdx_id", "NONE"),
            "license_name": lic.get("name", "NONE"), "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"), "open_issues": d.get("open_issues_count"),
            "pushed_at": (d.get("pushed_at") or "")[:10], "created_at": (d.get("created_at") or "")[:10],
            "archived": d.get("archived"), "is_fork": d.get("fork"),
            "default_branch": d.get("default_branch"), "homepage": d.get("homepage") or "",
            "topics": " ".join(d.get("topics") or []),
            "description": (d.get("description") or "").replace("\n", " "),
        })
        print(f"OK   {r:42s} {lic.get('spdx_id','NONE'):14s} pushed {str(d.get('pushed_at'))[:10]} stars {d.get('stargazers_count')}")
    except Exception as e:
        rows.append({"repo": r, "full_name": "ERROR", "license_spdx": str(e)[:60],
                     "license_name": "", "stars": "", "forks": "", "open_issues": "",
                     "pushed_at": "", "created_at": "", "archived": "", "is_fork": "",
                     "default_branch": "", "homepage": "", "topics": "", "description": ""})
        print(f"FAIL {r}: {e}")
    time.sleep(0.3)

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)
print("\nwrote", OUT, len(rows), "rows")
