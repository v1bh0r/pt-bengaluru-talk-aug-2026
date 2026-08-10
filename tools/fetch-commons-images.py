#!/usr/bin/env python3
"""Final asset build: fetch the curated Commons set, compress, base64-encode,
emit data URIs + an attribution table for the credits slide."""
import base64, json, os, subprocess, urllib.parse, urllib.request

UA = "TalkDeck/1.0 (vibhor.mahajan@gmail.com)"
API = "https://commons.wikimedia.org/w/api.php"
WORK = "/private/tmp/claude-504/-Users-personal-Documents-pt-bengaluru-platform-engineering-talk/c8ce218a-5a92-4810-9b21-651f6d8f1774/scratchpad/final"
os.makedirs(WORK, exist_ok=True)

MANIFEST = [
    ("oxcart",      "File:A bullock cart in India (c. 1900).jpg"),
    ("appian",      "File:ViaAppiaAntica1900.JPG"),
    ("coach",       "File:McLaughlin stagecoach, circa 1880s - DPLA - 294b58f952c4bb69ac1c19a050817dfb.jpg"),
    ("benz",        "File:1885Benz.jpg"),
    ("bertha",      "File:Berthabenzportrait.jpg"),
    ("earlycar",    "File:Charles Rolls driving a Peugeot 1896.jpg"),
    ("assembly",    "File:Assembly line Ford T, 1923.jpg"),
    ("congestion",  'File:Traffic passing "Magic Circle" at Wilshire and Western, Los Angeles, 1922 (AAA-EN-135-2).jpg'),
    ("policeman",   "File:Oxford Street (22327733075).jpg"),
    ("autobahn",    "File:Autobahn-RAB4-03-Rudolf-Knobloch-1935.jpg"),
    ("istate",      "File:Southern Freeway construction at Balboa Park, 1964.jpg"),
    ("interchange", "File:Highway 401 between 403 and 410.jpg"),
    ("waymo",       "File:Waymo self-driving car. (52194843144).jpg"),
]

def strip_html(s):
    import re
    return re.sub(r"<[^>]+>", "", s or "").strip()

def info(title):
    p = {"action": "query", "titles": title, "prop": "imageinfo",
         "iiprop": "url|extmetadata|size", "iiurlwidth": "1600", "format": "json"}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(p), headers={"User-Agent": UA})
    d = json.load(urllib.request.urlopen(req, timeout=40))
    for k, v in d.get("query", {}).get("pages", {}).items():
        if k == "-1" or "imageinfo" not in v:
            return None
        ii = v["imageinfo"][0]; em = ii.get("extmetadata", {})
        return {"url": (ii.get("thumburl") or ii["url"]).split("?")[0],
                "license": strip_html(em.get("LicenseShortName", {}).get("value", "?")),
                "artist": strip_html(em.get("Artist", {}).get("value", ""))[:70],
                "page": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))}
    return None

assets, credits, total = {}, [], 0
for slug, title in MANIFEST:
    m = info(title)
    if not m:
        print(f"{slug:12} MISSING"); continue
    src = f"{WORK}/{slug}.src"
    req = urllib.request.Request(m["url"], headers={"User-Agent": UA})
    open(src, "wb").write(urllib.request.urlopen(req, timeout=90).read())
    jpg = f"{WORK}/{slug}.jpg"
    subprocess.run(["magick", src, "-resize", "1280x", "-quality", "78", "-strip",
                    "-interlace", "Plane", jpg], check=True, capture_output=True)
    b64 = base64.b64encode(open(jpg, "rb").read()).decode()
    assets[slug] = "data:image/jpeg;base64," + b64
    total += len(b64)
    credits.append({"slug": slug, "title": title[5:], "license": m["license"],
                    "artist": m["artist"], "page": m["page"]})
    print(f"{slug:12} OK  {len(b64)//1024:5} KB b64   {m['license'][:16]:18} {m['artist'][:34]}")

json.dump(assets, open("/private/tmp/claude-504/-Users-personal-Documents-pt-bengaluru-platform-engineering-talk/c8ce218a-5a92-4810-9b21-651f6d8f1774/scratchpad/assets.json", "w"))
json.dump(credits, open("/private/tmp/claude-504/-Users-personal-Documents-pt-bengaluru-platform-engineering-talk/c8ce218a-5a92-4810-9b21-651f6d8f1774/scratchpad/credits.json", "w"), indent=2)
print(f"\nTOTAL base64: {total/1024/1024:.2f} MB across {len(assets)} images")
