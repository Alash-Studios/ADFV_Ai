import webbrowser
from tkinter import *
import time

# Initialize root window
root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.config(bg="black")
root.title('ADFV.Ai')

# Style options
entry_bg_color = "dimgray"
entry_fg_color = "white"
button_bg_color = "hot pink"
button_fg_color = "white"
result_text_color = "black"

# Main display for responses
display_frame = Frame(root, bg="black")
display_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

TextField2 = Text(display_frame, height=20, width=60, bg=entry_bg_color, fg=entry_fg_color, wrap=WORD)
TextField2.pack(fill=BOTH, expand=True)
TextField2.tag_config("right", justify="right")

# Bottom frame for user input and send button
bottom_frame = Frame(root, bg="black")
bottom_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

TextField = Text(bottom_frame, height=2, width=100, bg=entry_bg_color, fg=entry_fg_color)
TextField.pack(side=LEFT, expand=True, fill=X, padx=(0, 10))


# Conversation flow logic
def inserted_text():
    user_input = TextField.get("1.0", END).strip().lower().title()
    TextField2.insert(END, f'\n{user_input}\n', "right")
    TextField.delete("1.0", END)

    if "hello" in user_input:
        TextField2.insert(END, "Hello, User\n")

    elif "tell me about digital marketing" in user_input:
        TextField2.insert(END, "Digital marketing uses technology to create product awareness.\n  \n")

    elif "what loyalty programs work best for retail stores" in user_input:
        TextField2.insert(END, "Tiered rewards systems and points-based programs encourage repeat visits by offering increasing benefits.\n + \n")

    elif "how can a retail store effectively use social media" in user_input:
        TextField2.insert(END, "Engaging with customers through polls, showcasing new arrivals, and running targeted ads can boost online visibility.\n \n")

    elif "what are key elements of a successful e-commerce website" in user_input:
        TextField2.insert(END, "User-friendly navigation, high-quality product images, customer reviews, and secure payment options are essential.\n \n")

    elif "how can email marketing benefit an e-commerce business" in user_input:
        TextField2.insert(END, "Email marketing can personalize offers, remind customers of abandoned carts, and promote new products to drive sales.\n \n")

    elif "what tactics can hotels use to enhance guest experiences" in user_input:
        TextField2.insert(END, "Personalizing services, offering local experiences, and implementing feedback systems can significantly improve guest satisfaction.\n \n")

    elif "how can a hotel leverage online reviews for marketing" in user_input:
        TextField2.insert(END, "Responding to reviews and showcasing positive feedback on social media can enhance the hotel's reputation.\n \n")

    elif "what are effective ways for gyms to attract new members" in user_input:
        TextField2.insert(END, "Offering free trials, referral bonuses, and hosting community events can draw in potential members.\n \n")

    elif "how can fitness influencers aid in marketing" in user_input:
        TextField2.insert(END, "Collaborating with influencers for brand visibility and endorsements can help reach a larger, targeted audience.\n \n")

    elif "what marketing strategies work for a new restaurant" in user_input:
        TextField2.insert(END, "Hosting soft openings, utilizing food blogs for reviews, and creating visually appealing social media content can help.\n \n")

    elif "how can restaurants encourage repeat customers" in user_input:
        TextField2.insert(END, "Implementing loyalty programs and sending personalized offers can motivate repeat visits.\n \n")

    elif "what is the importance of product demos in tech marketing" in user_input:
        TextField2.insert(END, "Product demos allow potential customers to see the product in action, which can significantly boost conversion rates.\n \n")

    elif "how can tech companies build a strong online community" in user_input:
        TextField2.insert(END, "Engaging through forums, social media groups, and hosting webinars can create a loyal customer base.\n \n")

    elif "what marketing methods are effective for online education" in user_input:
        TextField2.insert(END, "Content marketing, SEO strategies, and offering free introductory courses can attract students.\n \n")

    elif "how can educational institutions engage prospective students" in user_input:
        TextField2.insert(END, "Utilizing virtual tours, student testimonials, and interactive content can capture interest.\n \n")

    elif "how can real estate agents effectively use social media" in user_input:
        TextField2.insert(END, "Sharing listings, client success stories, and local market insights can enhance engagement and visibility.\n \n")

    elif "what are some strategies for staging a home for sale" in user_input:
        TextField2.insert(END, "Depersonalizing spaces, using neutral colors, and enhancing curb appeal can attract more buyers.\n \n")

    elif "how can non-profits effectively raise funds online" in user_input:
        TextField2.insert(END, "Utilizing crowdfunding platforms, engaging storytelling, and social media campaigns can enhance fundraising efforts.\n \n")

    elif "what role do partnerships play in non-profit marketing" in user_input:
        TextField2.insert(END, "Collaborating with businesses can increase visibility and provide resources for outreach.\n \n")

    elif "how can fashion brands build a loyal customer base" in user_input:
        TextField2.insert(END, "Offering exclusive memberships, personalized shopping experiences, and unique loyalty rewards can foster loyalty.\n \n")

    elif "what are effective ways to market sustainable fashion" in user_input:
        TextField2.insert(END, "Highlighting ethical practices, utilizing influencer collaborations, and educating consumers on sustainability can be impactful.\n \n")

    elif "how can travel agencies use social media to promote destinations" in user_input:
        TextField2.insert(END, "Sharing stunning visuals, travel tips, and engaging stories can inspire potential travelers.\n \n")

    elif "what are effective marketing strategies for travel deals" in user_input:
        TextField2.insert(END, "Time-sensitive promotions, email newsletters, and partnership offers can drive urgency and bookings.\n \n")

    elif "how can car dealerships attract more customers" in user_input:
        TextField2.insert(END, "Hosting community events, offering test drive incentives, and utilizing targeted online ads can increase foot traffic.\n \n")

    elif "what role does online reputation play for dealerships" in user_input:
        TextField2.insert(END, "Positive online reviews can enhance credibility and attract potential buyers. \n \n")

    elif "how can home improvement businesses generate leads" in user_input:
        TextField2.insert(END, "Offering free consultations, showcasing past projects, and utilizing local SEO can effectively attract clients.\n \n")

    elif "what is the importance of customer testimonials in this industry" in user_input:
        TextField2.insert(END, "Testimonials build trust and can significantly influence potential customers’ decisions. \n \n")

    elif "how can film festivals effectively promote their events" in user_input:
        TextField2.insert(END, "Utilizing social media campaigns, engaging local influencers, and offering early bird tickets can increase attendance. \n \n")

    elif "what marketing strategies work best for concert promotions" in user_input:
        TextField2.insert(END, "Engaging with fans on social media, offering exclusive content, and partnering with local businesses can drive ticket sales. \n \n")

    elif "what are effective ways to market fitness products" in user_input:
        TextField2.insert(END, "Utilizing social media influencers, offering free trials, and providing engaging content can boost sales. \n \n")

    elif "how can brands create engaging content around fitness" in user_input:
        TextField2.insert(END, "Sharing workout tutorials, success stories, and fitness challenges can build community engagement. \n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")

    elif "" in user_input:
        TextField2.insert(END, "\n \n")



    elif user_input in ["quit", "shutdown", "close"]:
        TextField2.insert(END, f"{user_input.capitalize()}ing...\n")
        time.sleep(1)
        root.destroy()
    else:
        TextField2.insert(END, "I'm sorry, I don't have information on that topic. But Let me open a browser on that.\n")
        webbrowser.open(user_input)



# Send button
send_button = Button(bottom_frame, text="Send", command=inserted_text, bg=button_bg_color, fg=button_fg_color)
send_button.pack(side=RIGHT)

root.mainloop()
