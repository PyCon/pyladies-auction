Auction Item Management
--
Everything is managed via shared google documents. Each year gets it's own primary spreadsheet with a connected form. All items, wether for the auction or the raffle, are entered into the system via the google form. The main collection form includes sensitive information about the donors. We copy the non-sensitive information to other pages to have a printed overview at the auction, and for using google document Avery importing (described below.)

Typically we create a google folder for the auction every year, share the entire folder between the PSF accounting Team, PyCon management, and the Auction heads. All the documents and materials for the year are stored there. This includes custom PyLadies Geek logo artwork, receipts, slide show images, and donated gift certificates which may need to be printed.

# Google Drive Setup

* Create google drive folder "PyCon 20XX PyLadies Auction" 
* Share folder with PSF accountant, PyCon Head, and Auction Heads.
* Create "PyCon PyLadies 20XX Auction Items" blank spreadsheet (in the folder.)
* Create Form for spreadsheet for item intake (form described below.) Rename the form sheet **Auction Item Intake**
* Add the following sheets to the spreadsheet (described below):
    * **Descriptions** - items to be auctioned
    * **Raffle** - items in the raffle (incomplete)
    * **Winners** - import from Accountants export csv file post auction
    * **bidder tax info** - accounting breakdown
    * **donor tax info** - accounting breakdown
    * **cards** - information for writing thank-you's
    * **labels** - winner addresses for import to address label Avery template
* Create bit.ly shortened URL to the form for e-mailing and displaying. (bit.ly/pyauction, but repurposed to new year.)
* Install [Avery Label Merge Google Doc Add-On](https://chrome.google.com/webstore/detail/label-merge/nbejkhimfhdocbdciflmaofhglomdjij?hl=en-US)
* Create sub-folder for "artwork"
* Create sub-folder for "slideshow" (pictures from past auctions, and PyLadies meetups, etc.) Expand from past years.
* Create sub-folder for gift "certificates" (we always get them.)

# Auction Item Intake (sheet)

All items are entered in via the google form. Often more than one item will be included in the form. This could be "Tote bag x2" or the like. It may be the auction heads which enter the data for the donors. The main form page can have additional columns added to it for marking if the item will be for the raffle or the auction, and if the item is in hand. I usually pick a column and use the background cell color to denote if we have received the item, and have a selection column for deciding if the item will be for the auction, raffle, both, or as a PyLadies lunch giveaway.

As items come in we continually refactor what items will be in the auction and what will be in the raffle. Any items with a value of $250 or more are automatically in the auction, and can not be raffled.

Two additional sheets "**descriptions**" and "**raffle**" are created. The descriptions sheet contains all the items to be auctioned, while the raffle is for the raffle.

# Descriptions (auction items sheet)
This sheet is the main auction inventory. The first column is the item number. This is the **unique ID** which is shared between the auctioneers, the checkout, and all the accounting. It does not matter what else is there, this number if KEY. 

This sheet will be printed out for the auction checkout and the auctioneers. We use this to track what items we have left to be auctioned and have a good overview of what the auction is going to be  like. We want 25-35 items in the main auction. 30 is the best for a manageable auction. 

This sheet is also used at input into the Avery merge google doc add-on to convert the fields into business cards which can be printed out and displayed with the items.

When an item is won, the winning bid is written on the back of the card, and given to the runner who takes the item over to checkout to be paid for. The **#** on the card is what is entered into the accounting system and tied back to the spreadsheet. For accounting we need to report the difference between the winning bid and the reported value on the **bidder tax info** sheet. We use the value represented hear as the auction item intake may not have the value properly broken out (2 totes for $120, where 1 is in the auction and one in the raffle, so the winning bidder is against the )

The descriptions sheet has 6 columns:
 * **#** -increasing number (using a formula to make life easier) This is the auction item number and is
 * **Item Name** - Short(ish) item name that fits on a business card.
 * **donor**
 * **value** - used for picking an initial bid, but **NOT** included on the card.
 * **donor info** - The donor tagline, or other pertinent info
 * **description** - The description of the item in as much detail as we can fit. Often different (i.e. longer) than provided by the donor.

 # Raffle (sheet)
This is identical to the **Descriptions** sheet except it does **not** have the first **#** ID column, nor the **value** field. 

The avery merge plugin is used to print out the information on business cards for displaying with the raffle items.

This is printed for the MC to refer to during the auction [Introduction](introduction.md).

# Winners (sheet)

This sheet is not created until after the auction. The PSF accountants will export a CSV file or similar which includes the **#** item number, winning bid, and bidder information, including their address. This is imported to this sheet to be used to create the remaining sheets. The exact columns depends on the system used.

# bidder tax info (sheet)

This sheet is.... complicated. A person may have won multiple bids. We need, for each person, the total value of each item reported by the donors, the total of their bids, and the total difference. For sanity we also keep the individual breakout as well. This will also include their address information. This information is given back to the accountants for IRS reporting, and other black magic they do to keep this all legal.

# donor tax info (sheet)

**NO LONGER NEEDED** 

The PSF accountants currently just use the **Auction Item Intake** form directly for this.

This page has similar information to the donor tax info, but for the donor entities which may be people, or may be corporations. Only items worth $250? or more need to be reported? (don't take that as fact. Talk to an actual accountant!) This requires the donation value and normalized value, both for individual items and total items donated by the person. 

# cards (sheet)

The PyLadies (usually just Lynn Root) writes than you cards to all the winners. To facilitate this we generate a sheet with the columns:

* **#** - item number
* **description** - the name/description of the item won
* **name** - name of the person who won the item

This form is sorted by the bidder name, because a person may have won more than one item. This is printed out and handed off to the PyLadies to write the thank you cards and seal the envelopes. The first item **#** for a card is written on the back of the card discreetly. 

# labels (sheet)

This is a copy of the **winners** sheet, which we can edit to make sure all the addresses properly fit on the labels, and contain the properly formatted information. We use the Avery merge add-on to generate a google doc to print out the address labels. We use the **cards** sheet printout and the discreetly written item **#** on the envelope to match up the address to the envelope. Then we ship the cards. 

# Google Form

Create a blank spreadsheet and a google form connected to the spreadsheet on a new page. Form should be created as follows:


### **PyCon PyLadies 2019 Auction Items**

This form is used for tracking our auction items. Please fill out the information below so that the PyLadies Auction and PSF can track your donation and follow up with you after the auction. 

**What did you donate?**
*(required) short answer text*

**Describe the item in more detail.**
*(required) long answer text*

**What is the estimated value of your donation?**
*(required) short answer text*

**How is the donated item getting to us?**
*(required) short answer text)*

Has it been shipped? Emailed? Or will be it hand delivered?

**Who is the official donor / sponsor that we should give kudos too?**
*short answer text*

**What is the tagline of the donor/sponsor, if they have one?**
*long answer text*

When we say that something is donated by, we might use this to further describe the company or person making the donation. Limited to 140 characters. 

**Contact name**
*(required) short answer text*

This is the person who will be directly coordinating the delivery / handoff of the donation. In some cases, this may be the same as the donor.

**Contact email**
*(required) short answer text*

**Contact Phone**
*short answer text*

NOT Required. Only used in case of emergency, on short notice.

**Mailing address for tax purposes**
*(required) long answer text*

(Hold down shift & return for multiple lines). If this is different from the contact person, please include a name as well.

# E-mail response for donors

*Most of the e-mails with sponsors and donors are about particulars concerning the item they want to donate. It is best to personalize these. However the most common issue is where to ship donations. This is an example form e-mail that I use for donors which I then personalize for the specific needs of the person I am in contact with.*

Items can be shipped to the conference between April 1st and May 2nd, information below. We will also happily accept hand delivered items in the Staff Room 11, between 10am Wednesday May 1st and 10am Saturday May 4th. 


If you have a picture of the item we will include that on the auction page with accreditation.


We request that you fill out the donation form with details of each donation. If you are donating many items, or are unsure, we can enter in the information for you. We need to report donations to the IRS and this helps us with that requirement: https://bit.ly/pyauction


If you have any questions or concerns we are here to help!
Advance shipping between April 1 - April 26


    c/o *HOLDINGCO*
    PyCon Annual Conference
    Show Management - PyLadies Auction
    *HOLDINGCO*
    *ADDRESS1*
    *CITY*, *STATE* *ZIP*
    USA


Shipping to the convention center after April 26 - Before May 2


    GES
    PyCon Annual Conference
    Show Management - PyLadies Auction
    *CONVENTION CENTER*
    *ADDRESS1*
    *CITY*, *STATE* *ZIP*
    USA


