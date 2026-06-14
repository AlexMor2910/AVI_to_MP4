# AVI to MP4 Converter

This Python script converts all `.avi` video files in a selected folder into `.mp4` files using `ffmpeg`.

## Purpose

The script searches for `.avi` files inside a folder and converts each one to `.mp4` format. It skips files that have already been converted.

## Requirements

- Python 3
- FFmpeg installed and available from the command line

To check if FFmpeg is installed, run:

```bash
ffmpeg -version
```

## How It Works

1. Looks for all `.avi` files in the folder.
2. For each `.avi` file, creates an `.mp4` output filename.
3. Skips the file if the `.mp4` version already exists.
4. Converts the file using FFmpeg.
5. Prints whether the conversion succeeded or failed.

## FFmpeg Settings

The script uses the following settings:

- Video codec: `libx264`
- Pixel format: `yuv420p`
- Video profile: `baseline`
- H.264 level: `3.0`
- Audio codec: `aac`
- Audio bitrate: `128k`
- Fast start enabled for better playback compatibility

The settings can be changed depending on the system specifications.

## Usage

Save the script as:

```text
convert_avi_to_mp4.py
```

Then run it from the terminal:

```bash
python convert_avi_to_mp4.py
```

The converted `.mp4` files will appear in the same folder as the original `.avi` files.
