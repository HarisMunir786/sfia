from flask import render_template
from application import app

bookData = [
    {
        "genre":"Fiction",
        "title":"No Mercy",
        "author": {"first":"Colin", "last":"Forbes"},
        "content":"A man is found by Chief Superintendent Buchanan sitting on the steps of Whitehall. The man has apparently lost his memory. He utters only three words: I witnessed murder."
    },
    {
        "genre":"Fiction",
        "title":"Sinister Tide",
        "author": {"first":"Colin", "last":"Forbes"},
        "content":"Can Tweed stop Dr Goslar, the inventor of the supreme weapon, before it's too late? Tweed fought the doctor ten years before, and lost. If he fails this time then it will mean death for a hundred million people or more."
    },
    {
        "genre":"Fiction",
        "title":"Stealth",
        "author": {"first":"Colin", "last":"Forbes"},
        "content":"Paula Grey has her first inkling of danger when a boat vanishes in fog off Lymington, its sole occupant drifts ashore, dead. Then a British naval commander warns Tweed that vessels are disappearing. How are these and other factors related?"
    },
    {
        "genre":"Fiction",
        "title":"The Vorpal Blade",
        "author": {"first":"Colin", "last":"Forbes"},
        "content":"The Vorpal Blade advances into gripping new territory. Tweed has reverted to his one-time role of Homicide Superintendent at the Yard. He also retains his position as Deputy Director of the SIS."
    },
    {
        "genre":"Sports",
        "title":"The Book of Basketball",
        "author": {"first":"Bill", "last":"Simmons"},
        "content":"Bill Simmons, the wildly opinionated and thoroughly entertaining basketball addict known to millions as ESPN.com’s The Sports Guy, has written the definitive book on the past, present, and future of the NBA."
    },
    {
        "genre":"Sports",
        "title":"How to be a Footballer",
        "author": {"first":"Peter", "last":"Crouch"},
        "content":"Very funny on almost every page, wonderfully self-deprecating and very sharp on the ludicrous behaviour of the modern player."
    },
    {
        "genre":"Sports",
        "title":"Unstoppable",
        "author": {"first":"Tim", "last":"Green"},
        "content":"If anyone understands the phrase “tough luck,” it's Harrison. As a foster kid in a cruel home, he knows his dream of one day playing for the NFL is a..."
    },
    {
        "genre":"Sports",
        "title":"Underdogs",
        "author": {"first":"Tony", "last":"Hannan"},
        "content":"One of the founder members in 1895 of what became the Rugby League, Batley was once a thriving centre of commerce, one of the bustling mill towns in the Heavy Woollen District of ..."
    },
    {
        "genre":"Tech",
        "title":"Mastering Flask Web Development",
        "author": {"first":"Daniel", "last":"Gasper"},
        "content":"Learn to build modern, secure, highly available web MVC applications and API's using Python`s Flask framework..."
    },
    {
        "genre":"Tech",
        "title":"The Science of Lean Software and DevOps",
        "author": {"first":"Gene", "last":"Kim"},
        "content":"Accelerate your organization to win in the marketplace.How can we apply technology to drive business value?"
    },
    {
        "genre":"Tech",
        "title":"The Phoenix Project",
        "author": {"first":"Gene", "last":"Kim"},
        "content":"The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business..."
    },
    {
        "genre":"Tech",
        "title":"The DevOps Handbook",
        "author": {"first":"John", "last":"Williams"},
        "content":"How to Create World-Class Agility, Reliability, and Security in Technology Organizations..."
    },
    {
        "genre":"Tech",
        "title":"Fluent Python",
        "author": {"first":"Luciano", "last":"Ramalho"},
        "content":"With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best."
    },
    {
        "genre":"Tech",
        "title":"Flask Web Development",
        "author": {"first":"Miguel", "last":"Grinberg"},
        "content":"Take full creative control of your web applications with Flask, the Python-based microframework."
    },
    {
        "genre":"Tech",
        "title":"Effective DevOps",
        "author": {"first":"Jennifer", "last":"Davis"},
        "content":"Learn why devops is a professional and cultural movement that calls for change from inside your organization. ..."
    },
    {
        "genre":"Tech",
        "title":"Infrastructure as Code",
        "author": {"first":"Kief", "last":"Morris"},
        "content":"Virtualization, cloud, containers, server automation, and software-defined networking are meant to simplify IT operations."
    },
    {
        "genre":"Tech",
        "title":"The Site Reliability Workbook: Practical Ways to Implement SRE",
        "author": {"first":"Betsy", "last":"Beyer"},
        "content":"The overwhelming majority of a software system’s lifespan is spent in use, not in design or implementation. ..."
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', books=bookData)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/myaccount')
def myaccount():
    return render_template('myaccount.html', title='My Account')

@app.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')
