# uBlock.Deshittifier

Contains opiniated uBlock filter lists for deshittifying your web experience by blocking lots of useless content on a
given webiste.
Each file in `Lists/` blocks all the annoying content for a given website.
Examples:

- Block YouTube shorts
- Hide irrelevant search results on YouTube (shorts, previously watched, etc.)
- Hide Google popups
- Remove all Copilot propaganda from GitHub

# Installation

To install one (or more) of these lists, lookup the site and the category in the table below.
Copy the url.
Open the extension settings of uBlock and press the three gears (dashboard).
Navigate to filter lists and click on "Import...", listed on the bottom.
Paste the url, where each line only contains one url.

# Description of blocked items

- **YouTube**
-
    - All propaganda related to YouTube shorts is blocked.
-
    - The search results are decluttered by hiding all search results which are designed to keep you as long as possible
      looking for your favorite video.
      Filtered sections include sections like "People also watched", "Explore more", "Previously watched" and of
      course "Shorts".
- **GitHub**
-
    - Removes all references to Copilot. No more footers promoting Copilot, no more search suggestions with copilot.
- **Google**
-
    - Removes all the annoying popups which tell you to log in with Google. For instance, StackOverflow is suffering
      this fate.
- **Discogs**
-
    - For all the people that prefer to listen to their music on YouTube this hides the Audio section promoting Apple
      Music on a given track release page.
      It allows you to click on the YouTube videos faster, because no scrolling is required.

## To do

- [ ] Create a simple web interface where you can select multiple filter lists to get a new one.

# Links to uBlock lists

| Site       | Url                                              |
|------------|--------------------------------------------------|
| **All**    | https://deshittifier.ririsharp.nl/ultralist.txt  |
| YouTube    | https://deshittifier.ririsharp.nl/youtube.txt    |
| GitHub     | https://deshittifier.ririsharp.nl/github.txt     |
| Google     | https://deshittifier.ririsharp.nl/google.txt     |
| Discogs    | https://deshittifier.ririsharp.nl/discogs.txt    |
| StoryGraph | https://deshittifier.ririsharp.nl/storygraph.txt |