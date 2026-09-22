# YouTube to MP3 Converter

This program reads YouTube links from a text file and converts each video into an MP3 audio file.

Only download videos that you own or have permission to download.

## What you need

You need:

1. A Windows computer
2. An internet connection
3. Python
4. FFmpeg
5. The `youtube_to_mp3.py` file
6. A text file containing the YouTube links

Do not worry if you have never programmed before. Follow each step below in order.

## Step 1: Create a folder

1. Go to your Desktop.
2. Right-click an empty area.
3. Select **New**, then **Folder**.
4. Name the folder:

   ```text
   YouTube Converter
   ```

5. Put `youtube_to_mp3.py` inside this folder.

## Step 2: Install Python

1. Visit:

   https://www.python.org/downloads/

2. Click the yellow **Download Python** button.
3. Open the downloaded installer.
4. Before clicking Install, tick the box that says:

   ```text
   Add Python to PATH
   ```

5. Click **Install Now**.
6. Wait for the installation to finish.

## Step 3: Install FFmpeg

Open the **Start menu** and type:

```text
Terminal
```

Open **Terminal** or **Windows PowerShell**.

Copy and paste this command into the window:

```powershell
winget install --id Gyan.FFmpeg -e
```

Press **Enter**.

If Windows asks whether you agree to any terms, type `Y` and press **Enter**.

Wait for the installation to finish. Close and reopen Terminal afterward.

## Step 4: Install the YouTube downloader

Open Terminal again.

Copy and paste this command:

```powershell
python -m pip install --upgrade yt-dlp
```

Press **Enter** and wait for it to finish.

## Step 5: Create the list of videos

Open **Notepad**.

Put one YouTube link on each line:

```text
https://www.youtube.com/watch?v=EXAMPLE_ONE
https://www.youtube.com/watch?v=EXAMPLE_TWO
https://youtu.be/EXAMPLE_THREE
```

The examples above are placeholders. Replace them with the real links you want to use.

In Notepad:

1. Click **File**.
2. Click **Save As**.
3. Open the `YouTube Converter` folder you created.
4. Enter this filename:

   ```text
   videos.txt
   ```

5. Click **Save**.

Your folder should now contain:

```text
YouTube Converter
├── youtube_to_mp3.py
└── videos.txt
```

## Step 6: Open Terminal in the folder

Open the `YouTube Converter` folder.

Right-click an empty area inside the folder and select:

```text
Open in Terminal
```

If that option does not appear:

1. Click the folder’s address bar.
2. Type `powershell`.
3. Press **Enter**.

A Terminal window should open in the correct folder.

## Step 7: Start the converter

Enter this command:

```powershell
python youtube_to_mp3.py videos.txt
```

Press **Enter**.

The program will process every link in `videos.txt`.

When it finishes, a new folder named `downloads` will appear:

```text
YouTube Converter
├── downloads
│   ├── First video.mp3
│   └── Second video.mp3
├── youtube_to_mp3.py
└── videos.txt
```

Your MP3 files will be inside the `downloads` folder.

## Choosing the sound quality

The normal quality is 192 kbps.

For the highest available MP3 setting, use:

```powershell
python youtube_to_mp3.py videos.txt --quality 320
```

Available settings are:

```text
128
192
256
320
```

Higher settings produce larger files. They cannot improve audio that was already lower quality.

## Choosing a different output folder

To save the files in a folder named `My Music`, use:

```powershell
python youtube_to_mp3.py videos.txt --output-dir "My Music"
```

You can combine this with a quality setting:

```powershell
python youtube_to_mp3.py videos.txt --output-dir "My Music" --quality 320
```

## Using the converter again

You do not need to reinstall anything.

1. Open `videos.txt`.
2. Remove the old links.
3. Add the new links.
4. Save and close the file.
5. Open Terminal in the `YouTube Converter` folder.
6. Run:

   ```powershell
   python youtube_to_mp3.py videos.txt
   ```

## If something goes wrong

### “Python was not found”

Python is either not installed or was not added to `PATH`.

Install Python again and make sure you tick:

```text
Add Python to PATH
```

### “No module named yt_dlp”

Run:

```powershell
python -m pip install --upgrade yt-dlp
```

Then try the converter again.

### “FFmpeg is not installed”

Run:

```powershell
winget install --id Gyan.FFmpeg -e
```

Close Terminal, reopen it, and try again.

### “Input file not found”

Make sure:

- The file is named exactly `videos.txt`.
- It is in the same folder as `youtube_to_mp3.py`.
- Windows has not secretly named it `videos.txt.txt`.

To check the real filename:

1. Open the folder.
2. Click **View**.
3. Select **Show**.
4. Turn on **File name extensions**.

### A video will not download

Possible reasons include:

- The link is incorrect.
- The video is private.
- The video requires an account or age verification.
- The video is unavailable in your country.
- Your internet connection was interrupted.
- YouTube changed something.

First, update the downloader:

```powershell
python -m pip install --upgrade yt-dlp
```

Then try again.

## Important reminder

Only download and convert media that you own, that is in the public domain, or that you have permission to download. You are responsible for following copyright law and the website’s terms.