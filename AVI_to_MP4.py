from pathlib import Path
import subprocess

INPUT_FOLDER = Path(r"C:\Users\gm347\Documents\NewerCat\Miscelánea\Escuelas\UNAM\Ingeniería Mecatrónica\Segundo Semestre\Dibujo Mecánico e Industrial\Proyecto Para Enviar\mp4")
OUTPUT_FOLDER = INPUT_FOLDER
OUTPUT_FOLDER.mkdir(exist_ok=True)


def convert_avi_to_mp4(input_file: Path, output_file: Path):
    command = [
        "ffmpeg",
        "-i", str(input_file),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-profile:v", "baseline",
        "-level", "3.0",
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        str(output_file)
    ]
    print(f"Converting: {input_file.name} -> {output_file.name}")
    result = subprocess.run(command)
    if result.returncode == 0:
        print(f"Done: {output_file}")
    else:
        print(f"Failed: {input_file}")


def main():
    avi_files = list(INPUT_FOLDER.glob("*.avi"))
    if not avi_files:
        print("No .avi files found in the folder.")
        return
    for _ in avi_files:
        output_file = OUTPUT_FOLDER / f"{_.stem}.mp4"
        if output_file.exists():
            print(f"Skipping existing file: {output_file.name}")
            continue
        convert_avi_to_mp4(_, output_file)


if __name__ == "__main__":
    main()
