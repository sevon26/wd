from flask import Flask, render_template
import lxml.etree

ebay_root = lxml.etree.parse('db/ebay.xml')
yahoo_root = lxml.etree.parse('db/yahoo.xml')
gone321_root = lxml.etree.parse('db/321gone.xml')
ubid_root = lxml.etree.parse('db/ubid.xml')

app = Flask(__name__)

@app.route('/')
def home():
    r = find_all_auc_list()
    return render_template('index.html', auctions = r)

def find_aution_by_id(id):
    listing = ebay_root.xpath('/root/listing[./auction_info/id_num="'+id+'"]')
    if listing == []:
        listing = yahoo_root.xpath('/root/listing[./auction_info/id_num="'+id+'"]')
        if listing == []:
            listing = gone321_root.xpath('/root/listing[./auction_info/id_num="'+id+'"]')
            if listing ==[]:
                listing = ubid_root.xpath('/root/listing[./auction_info/id_num="'+id+'"]')
                return listing[0], 'ubid'
            return listing[0], 'gone321'
        return listing[0], 'yahoo'
    return listing[0], 'ebay'

@app.route('/auctionid/<auctionid>')
def about(auctionid):
    listing, db = find_aution_by_id(auctionid)
    if db == 'yahoo':
        img = 'https://www.gannett-cdn.com/-mm-/81667c78b3b803e2519a868b5a3309b72c3c6ead/c=0-0-4088-2310/local/-/media/2018/01/18/USATODAY/USATODAY/636518958643769410-EPA-FILE-USA-ECONOMY-EBAY-81477693.JPG?width=3200&height=1680&fit=crop'
    elif db == 'ebay':
        img = 'https://static.newmobilelife.com/wp-content/uploads/2016/09/yahoo-500m-account-hacked_00.jpg'
    elif db == 'gone321':
        img = 'https://trademarks.justia.com/media/og_image.php?serial=75710703'
    else:
        img = 'http://photos.prnewswire.com/prn/20120730/CG47323LOGO'

    return render_template('about.html', listing=listing, img=img)

def find_all_auc_list():
    L = []
    for listing in ebay_root.findall('listing'):
        L.append({
            'auction_info': listing.find('auction_info'),
            'memory': listing.find('item_info').find('memory'),
            'cpu': listing.find('item_info').find('cpu'),
            'hard_drive': listing.find('item_info').find('hard_drive'),
            'brand': listing.find('item_info').find('brand')
        })
    for listing in yahoo_root.findall('listing'):
        L.append({
            'auction_info': listing.find('auction_info'),
            'memory': listing.find('item_info').find('memory'),
            'cpu': listing.find('item_info').find('cpu'),
            'hard_drive': listing.find('item_info').find('hard_drive'),
            'brand': listing.find('item_info').find('brand')
        })
    for listing in gone321_root.findall('listing'):
        L.append({
            'auction_info': listing.find('auction_info'),
            'memory': listing.find('item_info').find('memory'),
            'cpu': listing.find('item_info').find('cpu'),
            'hard_drive': listing.find('item_info').find('hard_drive'),
            'brand': listing.find('item_info').find('brand')
        })
    for listing in ubid_root.findall('listing'):
        L.append({
            'auction_info': listing.find('auction_info'),
            'memory': listing.find('item_info').find('memory'),
            'cpu': listing.find('item_info').find('cpu'),
            'hard_drive': listing.find('item_info').find('hard_drive'),
            'brand': listing.find('item_info').find('brand')
        })
    return L

