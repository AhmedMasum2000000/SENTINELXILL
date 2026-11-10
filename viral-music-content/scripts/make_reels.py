"""Auto-generate ready-to-post 9:16 reels from the track using the ideas sheet.

Give it the track (the .mp4 visualizer or an mp3/wav) and the time of the drop. For each chosen
idea it renders a 1080x1920 clip. The clip has a tropical gradient background, or your cover art
if you pass one, an audio-reactive waveform, the idea's on-screen hook text, and an out-now CTA.

Templates
  coldopen   starts on the drop (idea #1 style). Default 10s.
  countdown  3-2-1 synced into the drop (idea #9 style). Default 10s.
  lyricpulse big hook text with a mirrored spectrum (ideas #41/#42 style). Default 12s.

Usage
  python3 scripts/make_reels.py --audio "Down In Bossa.mp4" --drop 32.5 [--cover cover.jpg]
                                [--ideas 1,2,9,41,58] [--priority 1] [--out exports]
Then: DRY_RUN=1 ./scripts/postiz_schedule.sh exports/

Find the drop time by scrubbing the track; this script can't detect it reliably.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
W, H, FPS = 1080, 1920, 30
CTA = "DOWN IN BOSSA  •  OUT NOW"
ARTIST = "ASH ARMY x ACND"
PALETTES = [  # tropical sunset / Rio night / Afro gold / ocean
    ("0xff5f6d", "0xffc371", "0x2b1055"),
    ("0x0f2027", "0x2c5364", "0xf7971e"),
    ("0x3a1c71", "0xd76d77", "0xffaf7b"),
    ("0x00c9ff", "0x92fe9d", "0x1a2a6c"),
]


def load_ideas():
    ws = load_workbook(ROOT / "Down_In_Bossa_100_Viral_Ideas.xlsx")["100 Ideas"]
    rows = list(ws.iter_rows(min_row=2, values_only=True))
    return {r[0]: {"cat": r[1], "title": r[2], "text": r[6], "priority": r[10]} for r in rows}


def template_for(idea_no, cat):
    if idea_no == 9 or "countdown" in str(cat).lower():
        return "countdown"
    if cat in ("Visualizer", "Genre Flip", "Producer BTS"):
        return "lyricpulse"
    return "coldopen"


def wrap(text, width=18):
    words, lines, cur = str(text).upper().split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    lines.append(cur)
    return "\n".join(lines)


def render(audio, start, dur, idea_no, idea, tpl, cover, out_dir, tmp):
    c1, c2, c3 = PALETTES[idea_no % len(PALETTES)]
    hook = idea["text"] if idea["text"] and "none" not in str(idea["text"]).lower() else idea["title"]
    hook_file = Path(tmp) / f"hook{idea_no}.txt"
    hook_file.write_text(wrap(hook))
    cta_file = Path(tmp) / "cta.txt"
    cta_file.write_text(CTA)
    art_file = Path(tmp) / "artist.txt"
    art_file.write_text(ARTIST)

    if cover:
        bg_in = ["-loop", "1", "-framerate", str(FPS), "-i", str(cover)]
        bg = (f"[1:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"zoompan=z='min(1.0+0.0008*on,1.25)':d=1:s={W}x{H}:fps={FPS},"
              f"eq=brightness=-0.12,vignette=PI/4[bg]")
    else:
        bg_in = ["-f", "lavfi", "-i",
                 f"gradients=s={W}x{H}:r={FPS}:c0={c1}:c1={c2}:c2={c3}:n=3:speed=0.015:type=radial"]
        bg = "[1:v]vignette=PI/4[bg]"

    # Audio-reactive mirrored waveform band in the lower-middle of the frame
    viz = (f"[0:a]asplit=2[a1][a2];[a1]showwaves=s={W}x420:mode=cline:rate={FPS}:colors=white@0.9:scale=sqrt,"
           f"format=rgba,colorchannelmixer=aa=0.85[wav]")
    if tpl == "lyricpulse":
        viz = (f"[0:a]asplit=2[a1][a2];[a1]showcqt=s={W}x210:r={FPS}:sono_h=0:bar_g=2:axis=0:"
               f"cscheme=1|1|1|1|1|1,format=rgba,colorkey=black:0.1:0.1,"
               f"split[f1][f2];[f2]vflip[f2v];[f1][f2v]vstack[wav]")

    font = f"fontfile={FONT}"
    # Hook text sits in the upper-middle safe zone; kicks in on frame 1.
    hook_y = "h*0.22"
    txt = (f"drawtext={font}:textfile={hook_file}:fontsize=88:fontcolor=white:line_spacing=14:"
           f"borderw=6:bordercolor=black@0.55:x=(w-text_w)/2:y={hook_y}")
    if tpl == "lyricpulse":  # pulse the text size with time to feel on-beat (~120 BPM)
        txt = txt.replace("fontsize=88", "fontsize='88+10*abs(sin(t*PI*2))'")
    if tpl == "countdown":
        cd = []
        for i, n in enumerate(["3", "2", "1"]):
            cd.append(f"drawtext={font}:text='{n}':fontsize=520:fontcolor=white:borderw=10:"
                      f"bordercolor=black@0.5:x=(w-text_w)/2:y=(h-text_h)/2-120:enable='between(t,{i},{i + 1})'")
        txt = ",".join(cd) + "," + txt.replace(f"y={hook_y}", f"y={hook_y}:enable='gte(t,3)'")
    lower = (f"drawtext={font}:textfile={art_file}:fontsize=40:fontcolor=white@0.85:x=(w-text_w)/2:y=h*0.80,"
             f"drawtext={font}:textfile={cta_file}:fontsize=54:fontcolor=white:box=1:boxcolor=black@0.45:"
             f"boxborderw=24:x=(w-text_w)/2:y=h*0.84")
    # Flash frame on the first frame of a coldopen = pattern interrupt
    flash = ",fade=in:st=0:d=0.25:color=white" if tpl == "coldopen" else ""

    fc = (f"{bg};{viz};[bg][wav]overlay=0:H*0.52[v1];[v1]{txt},{lower}{flash},"
          f"fade=out:st={dur - 0.4}:d=0.4[v];[a2]afade=t=out:st={dur - 0.6}:d=0.6,loudnorm=I=-14:TP=-1[a]")
    out = Path(out_dir) / f"{idea_no:03d}_{tpl}.mp4"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(start), "-t", str(dur),
           "-i", str(audio), *bg_in, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
           "-t", str(dur), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True, help="track file (.mp4/.mp3/.wav)")
    ap.add_argument("--drop", type=float, required=True, help="seconds where the drop hits")
    ap.add_argument("--cover", help="optional cover art image for the background")
    ap.add_argument("--ideas", help="comma list of idea numbers (default: by --priority)")
    ap.add_argument("--priority", type=int, default=1)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--out", default=str(ROOT / "exports"))
    a = ap.parse_args()

    ideas = load_ideas()
    if a.ideas:
        chosen = [int(x) for x in a.ideas.split(",")]
    else:
        chosen = [n for n, i in ideas.items() if i["priority"] == a.priority][: a.limit]
    Path(a.out).mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        for n in chosen:
            tpl = template_for(n, ideas[n]["cat"])
            dur = {"coldopen": 10, "countdown": 10, "lyricpulse": 12}[tpl]
            start = max(0.0, a.drop - 3) if tpl == "countdown" else (a.drop if tpl == "coldopen" else max(0.0, a.drop - 4))
            out = render(a.audio, start, dur, n, ideas[n], tpl, a.cover, a.out, tmp)
            print(f"#{n:<3} {tpl:<10} -> {out}")


if __name__ == "__main__":
    main()
