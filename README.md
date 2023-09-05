# :spiral_notepad: Simplenote to Zim

A simple script to convert your notes from Simplenote to Zim Desktop Wiki.

## Steps

1. Export your Simplenote at `Settings` > `Tools` > `Export Notes`
2. Unzip the `notes.zip` file somewhere
3. Find the file `notes.json` inside the `source` directory
4. Run `simplenote_to_zim.py notes.json`

## Details

The script will read the JSON, parsing the notes’ contents and metadata, and will export them to the same directory in the [Zim Wiki format](https://zim-wiki.org/manual/Help/Wiki_Syntax.html).
It creates the file header with the proper timestamp.
Uses the first line of the note as the title, removing the header markup (`#`).
Converts Simplenote tags to `@tag` format and inserts them below the title separated by `/`.
And the script also sanitizes the filename following Zim settings.
Please see the example output below.

Note that notes inside Simplenote’s trash won’t be converted.

## Example

```
Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.6
Creation-Date: 2023-01-19T09:11:27+01:00

====== Title of the page ======
Created Thursday 19 January 2023

@onetag / @another 

This is the content of the note.
```
