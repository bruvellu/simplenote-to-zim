# :spiral_notepad: Simplenote to Zim

A simple script to convert your notes from [Simplenote](https://simplenote.com/) to [Zim Desktop Wiki](https://zim-wiki.org/).

## Steps

1. Export your Simplenote at `Settings` > `Tools` > `Export Notes`
2. Unzip the `notes.zip` file somewhere
3. Find the file `notes.json` inside the `source` directory
4. Run `simplenote_to_zim.py notes.json`

## Details

The script reads the Simplenote JSON file, extracts the notes’ contents and metadata, and exports them to the [Zim Wiki format](https://zim-wiki.org/manual/Help/Wiki_Syntax.html) in the same directory.
It generates a file header with a timestamp, sets the note’s title to the first line of the content, and converts existing tags to the Zim `@tag` format.
The script also sanitizes the filename according to Zim settings.
Please refer to the example output below.

Note that notes in Simplenote's trash are not converted.

## Example

```
Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.6
Creation-Date: 2023-01-19T09:11:27+01:00

====== Title of the note ======
Created Thursday 19 January 2023

@tagthis @tagthat

Contents of the note.
```
