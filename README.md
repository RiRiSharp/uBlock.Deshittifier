# uBlock.Deshittifier
Contains uBlock filter lists for deshittifying your web experience by blocking lots of useless content on a given webiste.
Each folder in this repository contains a website, each file filters a certain category of annoying content on that website.
Examples:
- Block YouTube shorts
- Hide irrelevant search results on YouTube (shorts, previously watched, etc.)
- Remove the discogs audio section

# Installation
To install one (or more) of these lists, lookup the site and the category in the table below.
Copy the url.
Open the extension settings of uBlock and press the three gears (dashboard).
Navigate to filter lists and click on "Import...", listed on the bottom.
Paste the url, where each line only contains one url.

# List of uBlock lists
| Site    | Category | Url                                                                                                |
|---------|----------|----------------------------------------------------------------------------------------------------|
| YouTube | Shorts   | https://raw.githubusercontent.com/RiRiSharp/uBlock.Deshittifier/refs/heads/main/YouTube/shorts.txt |
|         | Search   | https://raw.githubusercontent.com/RiRiSharp/uBlock.Deshittifier/refs/heads/main/YouTube/search.txt |
| Discogs | Audio    | https://raw.githubusercontent.com/RiRiSharp/uBlock.Deshittifier/refs/heads/main/Discogs/audio.txt  |

# Full description
## YouTube
### Shorts
The filter list [/YouTube/shorts.txt] blocks everything related to YouTube shorts.

### Irrelevant search results
The filter list [/YouTube/search.txt] hides all search results which are designed to keep you as long as possible looking for your favorite video.
This includes sections like "People also watched", "Explore more", "Previously watched" and of course "Shorts".

## Discogs
### Audio
For all the people that prefer to listen to their music on YouTube this hides the Audio section on a given track release page.
It allows you to click on the YouTube videos faster, because no scrolling is required.

## To do
- [ ] Create a simple web interface where you can select multiple filter lists to get a new one.
- [ ] Create a build pipeline which contains all combined filter lists.