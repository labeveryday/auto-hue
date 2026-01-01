# auto-hue

Script is used to control my Phillips Hue lights settings for my YouTube videos.

Documentation on lights coming soon!

## Stream Deck: run `rotate_scenes.py`

1. In Stream Deck, add a button action: **System → Open**.
2. For the “App / File”, select:
   - **Recommended (no window):** `streamdeck_rotate_scenes.app`
   - **Fallback (opens Terminal):** `streamdeck_rotate_scenes.command`
3. Press the button to rotate scenes.

Notes:
- `rotate_scenes.py` now stores `scene_index.txt` next to the script, so it works even when Stream Deck runs it from a different working directory.
- The wrapper uses your repo venv Python at `venv/bin/python`. If you move the repo, update the path inside `streamdeck_rotate_scenes.command`.
- The `.app` is compiled from `streamdeck_rotate_scenes.applescript` and writes output to `streamdeck_rotate_scenes.log`.

## Secrets / local-only files (safe for GitHub)

- Copy `env.example` to `.env` (or `.envfile`) and set your `BRIDGE_IP` + `GROUP_NAME`.
- `.gitignore` is set up to keep `.env`/`.envfile`, `blog_post.md`, `scene_index.txt`, logs, and `venv/` out of the repo.
