# real-life-python
This repository contains scripts for making your everyday life easier - 
especially if you're up to some tedious manual work.

No breakthroughs here - anyone writing code for living can write these in 10 minutes. The goal here is to 
perhaps inspire those who don't even know the manual work can be avoided.

## photos/copy_photos.py
### Real life scenario

- Suppose you have two versions of photos - high quality and low quality, each in its folder,
and the filenames are the same in both.
- Suppose you created a subset of the high quality photos in a third folder, e.g. for an album.
- You found out the album would be too large.
- Now want to create the same subset of the low quality photos.

### Solution
The script selects files from a folder (source) that have the same names as files in another folder 
(subset definition), and stores them in a third folder (output).

### How to run
1. In the script, specify the directory storing all photos as `source` 
   and the directory containing the selection as `subset_def`
1. Run the script
1. The files selected from `source` will appear in `output` directory

## photos/fix_timezone_metadata.py
### Real life scenario

- You have nicely sorted photos on your disk
- You upload them to a Google Photos album
- The order of the photos is screwed up.

Now, there might be a lot of reasons for that, but it's quite likely that the timezones
aren't set for some of the photos, or are set differently, e.g. if taken by a different camera.

### What happens in Google Photos
- You can only sort by date, not by name.
- If the timezone for a photo isn't present in the metadata, it's set by Photos on upload based on your
browser (I guess) - for me it was GMT+02:00.
- However, if some of the photos contain a timezone, it's left as it is. For me, this was
GMT+00:00 for some of the photos.

### Solution
The script changes the timezone of photos that have the attribute in metadata to the timezone
of your choice. This should be the timezone Google Photos sets for the photos with no timezone.
It's not possible to add the attribute if it doesn't exist in the metadata - but  Google Photos
will take care of that.

### How to run
1. Create a folder containing all photos you want in the album
1. Specify that folder as `in_directory` in the script and run
1. Upload the photos from `out_directory` to Google Photos and see if the order is right

### Side note
Stack Overflow & friends isn't of much help here - at least not when I encountered the problem.
There is [this github issue](https://gist.github.com/lummie/732b8cb0b478966b91a7f9244c7aeac7),
and [this exiftool thread](https://exiftool.org/forum/index.php?topic=9956.0) pratically 
saying what the GitHub issue suggests won't work - but as of October 2021, what this script 
does seem to work.

This repository contains scripts for making your everyday life easier - especially if you're up to some tedious manual work.