"""Build the 100 viral video ideas spreadsheet for the "Down In Bossa" (Ash Army & ACND) campaign.

Usage:  python3 scripts/build_ideas_sheet.py
Output: viral-music-content/Down_In_Bossa_100_Viral_Ideas.xlsx
"""
import json
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
TRACK = "Ash Army & ACND - Down In Bossa"

# (category, title, hook in first 1.5s, edit recipe, length, on-screen text, platforms, virality lever, difficulty 1-3, priority 1-3)
IDEAS = [
    # ---------- A. HOOK & DROP EDITS ----------
    ("Hook & Drop", "Cold-open on the drop", "Frame 1 = loudest bar of the drop, full screen motion", "Start mid-drop, cut to black for 2 beats, rewind effect to the build, drop again at 0:09", "9-12s", "wait for it… again", "TT/IG/YT", "Replay loop (ends where it starts)", 1, 1),
    ("Hook & Drop", "Fake-out silence", "Music cuts to silence, caption 'my speakers died'", "1s silence then hard drop with zoom punch + flash frame", "8s", "my speakers died… then this", "TT/IG", "Pattern interrupt", 1, 1),
    ("Hook & Drop", "Beat-synced 40 cuts", "Hyper-fast cut on every kick from 1st frame", "40+ clips (crowd, beach, city) cut to each kick; ramp speed on percussion fills", "12-15s", "none – pure rhythm", "TT/IG/YT", "Rewatch to catch frames", 2, 1),
    ("Hook & Drop", "Volume warning", "Bold red 'TURN IT UP' card shaking to bassline", "Card shakes on kick, wipes to DJ hands on the drop", "7s", "🔊 TURN IT UP", "TT/IG", "Sound-on conversion", 1, 2),
    ("Hook & Drop", "Bass-face reaction loop", "Close-up face reacting to drop, freeze frame", "Freeze on face → zoom → unfreeze on drop; loop seamlessly", "6-8s", "the face you make at 0:04", "TT/IG", "Relatable + loop", 1, 1),
    ("Hook & Drop", "Shazam moment", "Phone screen showing Shazam spinning", "Screen record Shazam → result 'Down In Bossa' → cut to dance floor", "10s", "everyone asked what this was", "TT/IG", "Answers the #1 comment ('song?')", 1, 1),
    ("Hook & Drop", "Earbuds in, world changes", "Person puts AirPods in, B&W street", "Color + slow-mo bursts in on drop; people around start moving to beat", "10-14s", "POV: you press play", "TT/IG/YT", "Transformation", 2, 1),
    ("Hook & Drop", "Speedometer of energy", "On-screen meter at 0 rising with build", "Animated meter maxes out on drop, screen shake, explosion transition", "10s", "energy level:", "TT/IG", "Visual tension", 2, 3),
    ("Hook & Drop", "Countdown to drop", "Big 3…2…1 synced to snare roll", "Each number on a different location; '0' = drop + crowd", "8s", "3…2…1", "TT/IG/YT", "Anticipation", 1, 2),
    ("Hook & Drop", "Wrong song → right song", "Plays a boring elevator tune", "Record scratch, 'nah' text, slam into Down In Bossa drop", "9s", "my dad's playlist vs mine", "TT/IG", "Contrast humor", 1, 1),

    # ---------- B. TREND / PARTICIPATION ----------
    ("Trend Starter", "#DownInBossa 4-count dance", "Dancer does 4-move hook facing camera", "Simple 4-count move on the vocal hook, tutorial slow version at end", "15s", "learn it in 10 sec 👇", "TT/IG/YT", "Replicable = UGC flood", 2, 1),
    ("Trend Starter", "Hip-sway transition trend", "Outfit/scene change on the 'Bossa' vocal", "Hand covers lens → new location/outfit every vocal hit", "10-15s", "3 cities, 1 song", "TT/IG", "Easy for fans to copy", 1, 1),
    ("Trend Starter", "Glow-up on the drop", "Before shot (sleepy, home)", "Hard cut to glow-up on drop; template-ready", "8s", "before / after the drop", "TT/IG", "CapCut template potential", 1, 1),
    ("Trend Starter", "Duet/Stitch bait", "Split screen with empty right side", "Left: DJ playing; right: 'your turn' placeholder", "12s", "duet this with your best move", "TT", "Built-in Duet loop", 1, 2),
    ("Trend Starter", "Couples sync challenge", "Two people back to back", "Turn on drop, mirror moves, misfire blooper at end", "15s", "tag your dance partner", "TT/IG", "Tagging drives shares", 2, 2),
    ("Trend Starter", "Pet vibe check", "Dog/cat 'nodding' to beat (speed-matched)", "Speed-ramp pet movements to BPM", "8s", "even he gets it", "TT/IG/YT", "Pet content reach", 1, 2),
    ("Trend Starter", "Car-window vibe", "Hand out of car window at sunset", "Golden hour drive, windows down, drop on tunnel exit", "10s", "summer never left", "TT/IG", "Aesthetic + saveable", 1, 1),
    ("Trend Starter", "Office escape", "Laptop typing, boring lights", "Drop hits → office becomes beach club (green screen)", "10s", "5pm friday", "TT/IG", "Relatable timing (post Fridays)", 2, 2),
    ("Trend Starter", "Grandma approves", "Grandparent hears track first time", "Genuine reaction, starts dancing", "15-20s", "grandma's new favorite song", "TT/IG/YT", "Wholesome = shares", 1, 1),
    ("Trend Starter", "CapCut template drop", "Template preview with 5 photo slots", "Publish official CapCut template synced to drop; post example", "10s", "use this template 👆", "TT", "Template = mass reuse of sound", 2, 1),

    # ---------- C. GENRE FLIP / MASHUP ----------
    ("Genre Flip", "Bossa nova guitar → Afro House", "Acoustic nylon guitar playing the melody", "Live guitarist plays motif; cut to club version on drop", "15s", "bossa nova in 1965 vs 2026", "TT/IG/YT", "Proven format (SOAD x Bossa = 5.4M)", 2, 1),
    ("Genre Flip", "Rio 1960s film look", "Grainy 8mm Copacabana footage", "Vintage film filter → snap to modern club 4K on drop", "12s", "Ipanema called. it wants its groove back", "TT/IG/YT", "Nostalgia contrast", 2, 1),
    ("Genre Flip", "Piano cover → original", "Hands on piano playing hook", "Pianist plays slow; producer joins with drums; full drop", "15-20s", "I made it bossa first", "TT/IG/YT", "Musician audience shares", 2, 2),
    ("Genre Flip", "Sax player in the crowd", "Saxophonist on a balcony over a club", "Sax plays topline over drop, crowd turns", "15s", "he wasn't booked 😂", "TT/IG", "Live surprise", 3, 2),
    ("Genre Flip", "Afro house in 5 genres", "Same hook as bossa/lofi/techno/afro/orchestra", "5 x 3s segments, ends on original", "15s", "which one hits?", "TT/IG/YT", "Comment debate", 2, 1),
    ("Genre Flip", "Percussionist breakdown", "Live congas/shakers only", "Layer each percussion element on screen one by one", "15s", "every sound in this track", "TT/IG/YT", "Educational + satisfying", 2, 2),
    ("Genre Flip", "Samba school meets club", "Bateria drummers marching", "Cut drum hits in sync with track percussion", "12s", "Brazil x Africa x Club", "TT/IG/YT", "Cultural pride shares", 3, 3),
    ("Genre Flip", "Kitchen instruments remix", "Pans and glasses as percussion", "Recreate groove with kitchen items, fade to track", "15s", "made the beat with my kitchen", "TT/IG/YT", "Creativity / 'how'", 2, 2),
    ("Genre Flip", "Acapella only", "Isolated vocal on black", "Vocal + lyric text; beat slams in at 0:06", "10s", "now add the drums…", "TT/IG", "Stripped-back reveal", 1, 2),
    ("Genre Flip", "Old vinyl crate find", "Hands flipping old bossa records", "Drop needle on vinyl → it's Down In Bossa", "10s", "found this in my dad's crate", "TT/IG", "Story twist", 1, 2),

    # ---------- D. CROWD / DJ PERFORMANCE ----------
    ("Crowd & DJ", "Crowd drop POV from booth", "Behind DJ, hand raised before drop", "Wide crowd shot, phone flashes, confetti on drop", "8-12s", "the moment I dropped it", "TT/IG/YT", "Top afro house format (1.8M)", 1, 1),
    ("Crowd & DJ", "Sunset terrace set", "Rooftop DJ at golden hour", "Slow push-in, lens flare, drop = drone pull-out", "15s", "sunset + this track", "TT/IG/YT", "Aspirational / saves", 2, 1),
    ("Crowd & DJ", "Crowd sings the hook", "Mic pointed at crowd", "Crowd shouts vocal hook, DJ cuts music, crowd carries it", "10s", "they knew every word", "TT/IG", "Social proof", 2, 1),
    ("Crowd & DJ", "Mixer close-up macro", "Macro of fader & knobs", "EQ sweep filter build, bass knob up on drop", "8s", "watch the bass knob", "TT/IG/YT", "Satisfying gear porn", 1, 2),
    ("Crowd & DJ", "First play reaction", "DJ: 'never played this before'", "Live reaction of crowd hearing it for first time", "15s", "first time ever played", "TT/IG", "Exclusivity", 1, 1),
    ("Crowd & DJ", "Beach party drone", "Top-down drone over beach crowd", "Drone spiral synced to build, drop = descent", "12s", "where we're going this weekend", "TT/IG/YT", "Visual wow", 3, 2),
    ("Crowd & DJ", "B2B Ash Army x ACND", "Two DJs fist bump", "Split edit both artists mixing, mirror transition", "15s", "when two worlds collide", "TT/IG/YT", "Collab story", 2, 2),
    ("Crowd & DJ", "Phone light ocean", "Dark venue, phones light up", "Light-sweep transition on vocal, drop = strobes", "10s", "goosebumps", "TT/IG", "Emotional peak", 1, 2),
    ("Crowd & DJ", "Security guard dancing", "Stone-face guard starts grooving", "Zoom in, slow-mo, freeze-frame meme text", "8s", "even security broke", "TT/IG/YT", "Humor + shareable", 1, 1),
    ("Crowd & DJ", "Crowd 360 spin", "360 camera in middle of crowd", "Reframed spin synced to tempo", "10s", "middle of the floor", "TT/IG", "Immersive", 2, 3),

    # ---------- E. VISUALIZER / MOTION GRAPHICS ----------
    ("Visualizer", "Vertical audio-reactive loop", "Pulsing sun/palm logo on the kick", "After Effects audio-to-keyframes, seamless 8-bar loop", "15s", "Down In Bossa – out now", "TT/IG/YT", "Loop rewatch", 2, 1),
    ("Visualizer", "Kinetic lyric typography", "Huge word 'BOSSA' slams on beat", "Words animate per syllable, color pops on drop", "12s", "lyrics", "TT/IG/YT", "Sound-off viewers", 2, 1),
    ("Visualizer", "Waveform you can see", "Track waveform scrolling like a road", "Camera 'drives' along waveform; drop = jump", "10s", "the drop looks like this", "TT/IG/YT", "Novel visual", 3, 2),
    ("Visualizer", "Album art comes alive", "Cover art static", "Parallax/3D depth + moving elements (Runway/AI animate)", "8s", "cover art, but alive", "TT/IG", "Brand recall", 2, 1),
    ("Visualizer", "Spectrum on real world", "Equalizer bars rising from city skyline", "Tracked EQ bars on buildings, lights flicker to beat", "10s", "the city hears it", "TT/IG/YT", "VFX wow", 3, 2),
    ("Visualizer", "Paint drop", "Paint on speaker cone", "Macro slow-mo paint bouncing on bass (practical)", "8s", "bass you can see", "TT/IG/YT", "Satisfying ASMR-visual", 2, 1),
    ("Visualizer", "Water bowl bass test", "Bowl of water on subwoofer", "Cymatics patterns synced to drop", "8s", "cymatics of Down In Bossa", "TT/IG/YT", "Science curiosity", 1, 1),
    ("Visualizer", "Retro VHS tropical", "VHS tracking glitch palm trees", "VHS overlays, glitch on snares, clean on drop", "10s", "found tape: Rio '89", "TT/IG", "Aesthetic", 1, 2),
    ("Visualizer", "3D tropical club render", "Camera flies through a 3D jungle club", "Blender/Unreal fly-through synced to arrangement", "15s", "enter the bossa jungle", "TT/IG/YT", "High production standout", 3, 3),
    ("Visualizer", "Spotify canvas → reel", "Phone showing Spotify canvas", "Zoom into phone, canvas becomes full screen world", "8s", "streaming now", "IG/TT", "Drives to streaming", 1, 1),

    # ---------- F. STORY / POV / TEXT MEMES ----------
    ("POV & Memes", "POV: last night of holiday", "Sunset balcony, sad face", "Text story → track drops → slow-mo friends", "12s", "POV: last night in Tulum", "TT/IG", "Emotional relatability", 1, 1),
    ("POV & Memes", "Things that hit different", "List text over beach clips", "4-item list, item 4 = 'this drop at 2am'", "10s", "things that hit different:", "TT/IG", "List format retention", 1, 1),
    ("POV & Memes", "Me explaining afro house", "Person with whiteboard", "Explains seriously then gives up and dances on drop", "12s", "me explaining afro house to my mum", "TT/IG", "Humor", 1, 2),
    ("POV & Memes", "Main character walk", "Slow-mo walk through market", "Speed ramps on percussion hits", "10s", "main character energy", "TT/IG", "Self-insert", 1, 2),
    ("POV & Memes", "Group chat screenshot", "Fake chat 'send me that song'", "Chat scrolls, link sent, cut to party", "10s", "the group chat at 1am", "TT/IG", "Relatable + link drop", 1, 2),
    ("POV & Memes", "Pre-game vs party", "Split: getting ready / dance floor", "Left/right sync, merge on drop", "12s", "the playlist doing the heavy lifting", "TT/IG", "Weekend timing", 1, 2),
    ("POV & Memes", "Airport to beach", "Boarding pass close-up", "Travel match-cuts every bar, drop = jump in sea", "15s", "this song = my passport", "TT/IG/YT", "Travel aspiration", 2, 1),
    ("POV & Memes", "Rate this drop 1-10", "Big number '?/10'", "Play drop, number spins, lands on 11", "8s", "rate it in comments", "TT/IG/YT", "Comment bait", 1, 1),
    ("POV & Memes", "Gym PR song", "Lifter struggling", "Drop hits, lifts PR, slow-mo celebration", "10s", "the song that gets the PR", "TT/IG/YT", "Gym niche crossover", 1, 2),
    ("POV & Memes", "Barber shop vibe", "Barber with clippers", "Clipper buzz synced to hi-hats, fresh cut reveal on drop", "12s", "fresh cut + fresh track", "TT/IG", "Niche crossover", 2, 2),

    # ---------- G. PRODUCER / BTS ----------
    ("Producer BTS", "From 1 sound to full track", "Single shaker loop", "Layer stems one by one on DAW screen", "15-20s", "how Down In Bossa was built", "TT/IG/YT", "Producer audience", 1, 1),
    ("Producer BTS", "The rejected version", "'version 1 was trash'", "Play bad v1, cringe, cut to final drop", "12s", "v1 vs final", "TT/IG/YT", "Before/after", 1, 1),
    ("Producer BTS", "Sample hunt", "Digging bossa samples on laptop", "Show finding the original vibe → chop → result", "15s", "the sample that started it", "TT/IG/YT", "Origin story", 2, 2),
    ("Producer BTS", "Studio session with ACND", "Two producers vibing in studio", "Handheld fly-on-wall, captions of real chat", "15s", "the night we made it", "TT/IG/YT", "Authentic access", 1, 2),
    ("Producer BTS", "Kick drum anatomy", "Waveform of kick zoomed", "Explain 3 layers in 10 sec, then play groove", "15s", "why this kick hits", "TT/YT", "Educational saves", 1, 3),
    ("Producer BTS", "Bedroom to club", "Bedroom monitor playing track", "Same moment cut to club PA, crowd", "10s", "my bedroom → the club", "TT/IG/YT", "Journey", 1, 1),
    ("Producer BTS", "Ableton timeline speedrun", "Full project zoomed out", "Playhead races through arrangement in 10s", "10s", "4 months in 10 seconds", "TT/YT", "Effort reveal", 1, 2),
    ("Producer BTS", "Free sample pack bait", "'want the shaker loop?'", "Show loop, CTA comment 'BOSSA' to get it", "10s", "comment BOSSA for the loop", "TT/IG", "Comment keyword automation", 1, 1),
    ("Producer BTS", "Release day panic", "Phone notifications going off", "Countdown, upload, first stream", "12s", "release day reality", "TT/IG", "Human moment", 1, 3),
    ("Producer BTS", "Label signing reaction", "Opening the email", "Real reaction → play track", "12s", "the email that changed everything", "TT/IG/YT", "Story arc", 1, 3),

    # ---------- H. TRAVEL / LIFESTYLE ----------
    ("Lifestyle", "Ibiza boat day", "Boat bow cutting water", "Wake + champagne + jump synced", "12s", "boat day soundtrack", "TT/IG/YT", "Aspirational saves", 2, 2),
    ("Lifestyle", "Mykonos white streets", "Walk through white alleys", "Match-cut doors to beat", "10s", "mykonos at 7pm", "TT/IG", "Destination tags", 2, 2),
    ("Lifestyle", "Cape Town afro roots", "Table Mountain timelapse", "Township dancers + city, respectful cultural edit", "15s", "where afro house lives", "TT/IG/YT", "Cultural authenticity", 3, 2),
    ("Lifestyle", "Rio Copacabana tribute", "Copacabana wave pavement pattern", "Pattern morphs into waveform; drop = beach", "12s", "a tribute to Rio", "TT/IG/YT", "Ties to track concept", 3, 1),
    ("Lifestyle", "Rooftop pool party", "Underwater shot of jump", "Split above/below water on drop", "8s", "summer 26", "TT/IG", "Visual hook", 2, 2),
    ("Lifestyle", "Coffee morning slow groove", "Espresso pour slow-mo", "Calm intro → drop as cafe crowd moves", "10s", "morning playlist upgrade", "TT/IG", "Daytime niche", 1, 3),
    ("Lifestyle", "Fashion lookbook", "Model walking to camera", "Outfit change every 2 beats", "12s", "fit check: bossa edition", "TT/IG", "Fashion crossover", 2, 2),
    ("Lifestyle", "Night drive city lights", "Neon reflections on windshield", "Hyperlapse, light streaks on hi-hats", "10s", "late night drive", "TT/IG/YT", "Mood/saves", 1, 2),
    ("Lifestyle", "Sunrise after-party", "Sun rising over sea", "Crowd silhouettes, slow fade to logo", "15s", "6am, still here", "TT/IG/YT", "Emotional ending", 1, 2),
    ("Lifestyle", "Desert festival", "Dust + sunset DJ booth", "Drone + slow-mo dancers in dust", "15s", "the desert remembers", "TT/IG/YT", "Burner aesthetic", 3, 3),

    # ---------- I. FAN / UGC / INTERACTION ----------
    ("Fan & UGC", "Fan video compilation", "Best fan clip first", "Stitch 8 fan videos using the sound, credit each", "15s", "you guys did THIS", "TT/IG/YT", "Rewards UGC = more UGC", 1, 1),
    ("Fan & UGC", "Reply to comment video", "Pinned comment bubble on screen", "Answer 'song name?' with the drop", "8s", "replying to @…", "TT/IG", "Algorithm favors replies", 1, 1),
    ("Fan & UGC", "Guess the sample", "Mystery sound clip", "Play 2s of original, reveal in next video", "8s", "guess where this came from", "TT/IG", "Series cliffhanger", 1, 2),
    ("Fan & UGC", "Pick the next drop", "Two drop versions A/B", "Poll in caption, vote in comments", "12s", "A or B?", "TT/IG/YT", "Comment engagement", 1, 2),
    ("Fan & UGC", "Fan dance contest", "Prize reveal on screen", "Contest rules, best entry wins guestlist", "12s", "win guestlist 🎟️", "TT/IG", "Incentivized UGC", 1, 1),
    ("Fan & UGC", "Live stream clip", "Funniest live moment", "Cut live chat reaction + drop", "10s", "chat went crazy", "TT/IG/YT", "Repurpose", 1, 3),
    ("Fan & UGC", "Street reaction test", "Headphones on strangers", "3 reactions, best one last", "15-20s", "playing it to strangers", "TT/IG/YT", "Street-interview format", 2, 1),
    ("Fan & UGC", "Dancer collab", "Known dancer intro", "Pro choreo on hook, tag dancer", "15s", "@dancer x Down In Bossa", "TT/IG", "Borrowed audience", 2, 1),
    ("Fan & UGC", "Micro-influencer seeding pack", "Same template across 20 creators", "Brief creators with 3 hooks + template", "8-15s", "(creator-specific)", "TT/IG", "Seeding volume", 2, 1),
    ("Fan & UGC", "Map of plays", "World map lighting up", "Animate cities where track played/streamed", "10s", "Down In Bossa around the world", "TT/IG/YT", "Global proof", 2, 3),

    # ---------- J. SERIES / FRANCHISE FORMATS ----------
    ("Series", "Day 1 of playing it until it trends", "'Day 1' big text", "Daily post, new location each day", "8-12s", "day X until it trends", "TT/IG", "Series follow-hook", 1, 1),
    ("Series", "Drop in random places", "Unusual location (library/market)", "Speaker reveal, reactions", "12s", "dropping it in a…", "TT/IG/YT", "Repeatable format", 2, 1),
    ("Series", "Bossa vs Afro: who wins", "VS card", "Weekly genre battle, audience decides", "15s", "round 1", "TT/IG/YT", "Recurring debate", 2, 2),
    ("Series", "1 track, 10 edits", "Number counter '1/10'", "Same footage, 10 editing styles across 10 posts", "8s each", "edit style #3", "TT/IG", "Editor audience", 1, 2),
    ("Series", "Tour diary vertical", "City name stamp", "Each tour stop, 10s recap with drop", "10s", "stop #4: Lisbon", "TT/IG/YT", "Tour hype", 2, 2),
    ("Series", "Behind the label", "Label HQ entrance", "Mini-doc episodes on the team", "15-30s", "ep. 1", "IG/YT", "Brand depth", 2, 3),
    ("Series", "Song of the week loop", "Calendar flip", "Weekly feature, stays on brand", "8s", "song of the week", "TT/IG", "Consistency", 1, 3),
    ("Series", "Before it blew up", "Old footage of early show", "Then vs now crowd sizes", "12s", "before it blew up", "TT/IG/YT", "Underdog narrative", 1, 2),
    ("Series", "AI music video reel", "Surreal AI-generated Rio scenes", "AI video (Veo/Kling) frames cut to beat", "10-15s", "an AI dreamed this song", "TT/IG/YT", "Novelty", 2, 2),
    ("Series", "Full-length YouTube Shorts → long", "Short ends on cliffhanger", "Link to full visualizer / extended edit", "15s", "full version on my channel", "YT", "Funnels to long-form & streams", 1, 1),
]

assert len(IDEAS) == 100, len(IDEAS)

HEAD = ["#", "Category", "Idea", "Hook (first 1.5s)", "Edit recipe", "Length", "On-screen text",
        "Platforms", "Virality lever", "Difficulty (1 easy-3 hard)", "Priority (1 high)", "Status", "Editor", "Post URL", "Views 48h"]

PLAYBOOK = [
    ("Hook", "Win the first 1.5s: start on movement or the drop. Never open on a static logo or slow fade."),
    ("Length", "7-15s for reach and rewatches. The top Afro House clips scraped were 8-18s. Use 20-30s only for story or tutorial formats."),
    ("Audio", "Upload the track as ORIGINAL AUDIO from the artist account so every reuse links back. Start the clip on the hook, not the intro."),
    ("Loop", "Make the last frame match the first so the clip replays seamlessly. Rewatches count as watch time."),
    ("Text", "Put large text in the upper-middle of the frame, inside the safe zone (avoid the bottom 20% and right 15%). Most viewers start on mute."),
    ("Ratio", "60% the track in different contexts, 30% trending sounds and formats, 10% experiments."),
    ("Engagement", "Reply to comments within the first 30-60 minutes. Shares and saves outweigh likes."),
    ("Volume", "Post 1-3 times a day across TT/IG/YT Shorts at staggered times. Kill a format after 5 flops. Remake winners in 3 new variations."),
    ("Funnel", "Every caption needs a CTA: 'full track in bio' or 'comment BOSSA'. Use a smart link for streams."),
    ("Gap found", "Searching TikTok for 'Down In Bossa' (2026-11-10) returned only bossa-nova covers, not the track. Nobody has claimed the sound yet."),
    ("Proof", "'System Of A Down x Bossa Nova' mashup: 5.4M views, 108K saves. Genre-flip formats (category C) are the strongest bet."),
    ("Specs", "1080x1920, 30/60fps, H.264, loudness around -14 LUFS, burned-in captions. Export a 9:16 master plus a 4:5 version for the IG feed."),
]


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "100 Ideas"
    ws.append(HEAD)
    for i, row in enumerate(IDEAS, 1):
        ws.append([i, *row, "To do", "", "", ""])
    hdr_fill = PatternFill("solid", fgColor="1F2937")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = hdr_fill
        c.alignment = Alignment(wrap_text=True, vertical="center")
    widths = [5, 14, 30, 34, 50, 9, 30, 11, 30, 11, 9, 11, 12, 22, 10]
    for col, w in zip("ABCDEFGHIJKLMNO", widths):
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        pr = row[10]
        pr.fill = PatternFill("solid", fgColor={1: "BBF7D0", 2: "FEF08A", 3: "E5E7EB"}[pr.value])
    dv = DataValidation(type="list", formula1='"To do,Editing,Review,Scheduled,Posted,Winner,Flop"')
    ws.add_data_validation(dv)
    dv.add(f"L2:L{len(IDEAS) + 1}")
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = ws.dimensions

    pb = wb.create_sheet("Virality Playbook")
    pb.append(["Rule", "Detail"])
    for r in PLAYBOOK:
        pb.append(r)
    pb.column_dimensions["A"].width = 14
    pb.column_dimensions["B"].width = 110
    for c in pb[1]:
        c.font = Font(bold=True)

    research = json.loads((ROOT / "research_tiktok_2026-11-10.json").read_text())
    rs = wb.create_sheet("Scraped Research")
    cols = ["query", "author", "views", "likes", "shares", "saves", "comments", "duration_s", "desc", "url"]
    rs.append(cols)
    for r in research:
        rs.append([r.get(k) for k in cols])
    for c in rs[1]:
        c.font = Font(bold=True)
    rs.column_dimensions["I"].width = 70
    rs.column_dimensions["J"].width = 45

    out = ROOT / "Down_In_Bossa_100_Viral_Ideas.xlsx"
    wb.save(out)
    print(f"Wrote {out} ({len(IDEAS)} ideas, {len(research)} research rows) for {TRACK}")


if __name__ == "__main__":
    main()
