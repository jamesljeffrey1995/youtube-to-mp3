# YouTube to MP3 Converter for macOS

This program reads YouTube links from a text file and converts each video into an MP3 audio file.

Only download media that you own or have permission to download.

## What you need

You need:

1. A Mac
2. An internet connection
3. The `youtube_to_mp3.py` file
4. A text file containing the YouTube links

The instructions below install the other required software.

## Step 1: Create a folder

1. Open **Finder**.
2. Open your **Desktop**.
3. Click **File**, then **New Folder**.
4. Name the folder:

   ```text
   YouTube Converter
   ```

5. Put `youtube_to_mp3.py` inside this folder.

## Step 2: Install Homebrew

Homebrew is a tool that installs the software needed by the converter.

1. Visit:

   https://brew.sh

2. Copy the installation command shown under **Install Homebrew**.
3. Open **Terminal**:
   - Press `Command + Space`.
   - Type `Terminal`.
   - Press **Return**.
4. Paste the Homebrew installation command into Terminal.
5. Press **Return**.
6. Enter your Mac password if requested.

Your password will not appear on the screen while you type. This is normal. Type it carefully and press **Return**.

The installer may display additional commands under **Next steps**. If it does, copy and run those commands before continuing. This is important because Homebrew might not work otherwise.

## Step 3: Install Python and FFmpeg

Keep Terminal open.

Enter this command:

```bash
brew install python ffmpeg
```

Press **Return** and wait for the installation to finish.

You can check that both programs were installed by running:

```bash
python3 --version
ffmpeg -version
```

Both commands should display version information.

## Step 4: Open the converter folder in Terminal

Type the following into Terminal, including the space after `cd`:

```bash
cd 
```

Do not press Return yet.

Drag the `YouTube Converter` folder from your Desktop into the Terminal window. Terminal will add the folder’s location automatically.

Now press **Return**.

## Step 5: Create a private Python environment

Run:

```bash
python3 -m venv .venv
```

This creates a private Python environment inside the converter folder. It keeps the converter’s software separate from the rest of your Mac.

Activate it by running:

```bash
source .venv/bin/activate
```

You may now see `(.venv)` at the beginning of the Terminal line. That means it is active.

## Step 6: Install the YouTube downloader

Run:

```bash
python -m pip install --upgrade pip yt-dlp
```

Wait for the installation to finish.

## Step 7: Create the list of videos

Open **TextEdit**.

Before entering any links:

1. Click **Format** at the top of the screen.
2. Select **Make Plain Text**.
3. If it says **Make Rich Text** instead, the document is already plain text.

Put one YouTube link on each line:

```text
https://www.youtube.com/watch?v=EXAMPLE_ONE
https://www.youtube.com/watch?v=EXAMPLE_TWO
https://youtu.be/EXAMPLE_THREE
```

Replace these examples with the real links you want to use.

To save the file:

1. Click **File**, then **Save**.
2. Enter this filename:

   ```text
   videos.txt
   ```

3. Save it inside the `YouTube Converter` folder.
4. If TextEdit asks whether to add another file extension, keep the name as `videos.txt`.

Your folder should now contain:

```text
YouTube Converter
├── .venv
├── youtube_to_mp3.py
└── videos.txt
```

The `.venv` folder may be hidden in Finder. That is normal.

## Step 8: Start the converter

Make sure Terminal is still open in the `YouTube Converter` folder and that `(.venv)` appears at the beginning of the line.

Run:

```bash
python youtube_to_mp3.py videos.txt
```

The program will process every link in `videos.txt`.

When it finishes, a folder named `downloads` will appear:

```text
YouTube Converter
├── downloads
│   ├── First video.mp3
│   └── Second video.mp3
├── .venv
├── youtube_to_mp3.py
└── videos.txt
```

Your MP3 files will be inside `downloads`.

## Using the converter again

You do not need to reinstall anything.

1. Open `videos.txt`.
2. Remove the old links.
3. Add the new links.
4. Save and close the file.
5. Open Terminal.
6. Type `cd` followed by a space.
7. Drag the `YouTube Converter` folder into Terminal.
8. Press **Return**.
9. Activate the private Python environment:

   ```bash
   source .venv/bin/activate
   ```

10. Run the converter:

    ```bash
    python youtube_to_mp3.py videos.txt
    ```

## Choosing the sound quality

The default setting is 192 kbps.

For the highest available MP3 setting, run:

```bash
python youtube_to_mp3.py videos.txt --quality 320
```

The available settings are:

```text
128
192
256
320
```

A higher setting produces larger files. It cannot improve audio that was already lower quality.

## Choosing a different output folder

To save the files in a folder named `My Music`, run:

```bash
python youtube_to_mp3.py videos.txt --output-dir "My Music"
```

To use that folder and select 320 kbps:

```bash
python youtube_to_mp3.py videos.txt --output-dir "My Music" --quality 320
```

## Stopping the converter

To stop the program while it is running, press:

```text
Control + C
```

Partially downloaded files may remain in the `downloads` folder.

## Fixing common problems

### “command not found: brew”

Homebrew was not added to your Terminal correctly.

Run the commands shown under **Next steps** at the end of the Homebrew installation. You can also find installation help at:

https://docs.brew.sh/Installation

Close and reopen Terminal afterward.

### “command not found: python”

Use `python3` instead:

```bash
python3 youtube_to_mp3.py videos.txt
```

If the private environment is active, `python` should normally work.

### “No module named yt_dlp”

Open Terminal in the converter folder and run:

```bash
source .venv/bin/activate
python -m pip install --upgrade yt-dlp
```

Then try again.

### “FFmpeg is not installed”

Run:

```bash
brew install ffmpeg
```

When it finishes, try the converter again.

### “Input file not found”

Make sure:

- The file is named exactly `videos.txt`.
- It is inside the same folder as `youtube_to_mp3.py`.
- The Terminal window is open in that folder.

You can display the files in the current folder by running:

```bash
ls
```

You should see both:

```text
youtube_to_mp3.py
videos.txt
```

### The file is named `videos.txt.rtf`

TextEdit saved the file as a rich-text document.

1. Open the file in TextEdit.
2. Click **Format**.
3. Select **Make Plain Text**.
4. Save it again as `videos.txt`.

### A video will not download

Possible reasons include:

- The link is incorrect.
- The video is private.
- The video requires an account or age verification.
- The video is unavailable in your country.
- Your internet connection was interrupted.
- YouTube changed something.

Update the downloader:

```bash
source .venv/bin/activate
python -m pip install --upgrade yt-dlp
```

Then try again.

### macOS will not let the script run

Do not double-click `youtube_to_mp3.py`. Run it from Terminal using:

```bash
python youtube_to_mp3.py videos.txt
```

## Important reminder

Only download and convert media that you own, that is in the public domain, or that you have permission to download. You are responsible for following copyright law and the website’s terms.
