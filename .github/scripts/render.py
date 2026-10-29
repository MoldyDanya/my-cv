# Usage: render.py <in.md> <out.html> — renders markdown via GitHub API (same look as on github.com)
import json, os, sys, urllib.request

md = open(sys.argv[1], encoding="utf-8").read()
headers = {"Accept": "application/vnd.github+json", "Content-Type": "application/json"}
if os.environ.get("GH_TOKEN"):
    headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
req = urllib.request.Request("https://api.github.com/markdown",
    data=json.dumps({"text": md, "mode": "gfm"}).encode(), headers=headers)
body = urllib.request.urlopen(req).read().decode("utf-8")
html = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css">
<style>@page {{ margin: 15mm; }} .markdown-body {{ max-width: 900px; margin: 0 auto; font-size: 13px; }} .markdown-body img[align=right] {{ border-radius: 50%; margin-left: 20px; }}</style>
</head><body class="markdown-body">{body}</body></html>"""
open(sys.argv[2], "w", encoding="utf-8").write(html)
