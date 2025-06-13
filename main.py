from tkinter import *
from tkinter import messagebox
from functools import partial
import pickle

okno = Tk()
okno.geometry('800x700')
okno.resizable(False, False)
okno.title('Louis Vuitton')

okno.option_add("*tearOff", False)

main_menu = Menu(okno)
file_menu = Menu()
settings_menu = Menu()

settings_menu.add_command(label="UK")
settings_menu.add_command(label="USA")
settings_menu.add_command(label="Russia")
settings_menu.add_command(label="Italy")
settings_menu.add_command(label="Azerbaijan")
settings_menu.add_command(label="Dubai")

file_menu.add_cascade(label="country", menu=settings_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)

okno.config(menu=main_menu)

cart = []

shoes = {
    'Sneakerina' : 5430,
    'Pool Pillow' : 2000,
    'Pool Comfort' : 1700,
    'Trainer Sneaker' : 3100,
    'Lvisola' : 1500,
    'Bomdia' : 2000,
    'Silhouette' : 1000,
    'Sneaker' : 2500,
    'Mule' : 6800,
    'Shake' : 5430,
     'Sandal' : 7000,
    'Berlin' : 2000,
    'Lanad' : 1700,
    'Wedge Sandal' : 3100,
    'Flat Heilus' : 1500,
    'Swing' : 2000,
    'Allure' : 2500,
    'Sling Back' : 6800,

}

bags = {
    'High Rise PM': 2000,
    'Never Full MM': 1500,
    'Diane': 1200,
    'No way Vibe': 1800,
    'Low Key Cookie': 800,
    'All in BB': 2200,
    'Slouchy MM': 1600,
    'The Drop GM': 1900,
    'Mini Bumbag': 700,
    'Bobo Trunk': 2500,
    'Steamer 30': 2300,
    'Trunkie': 2100,
    'Keepit': 1000,
    'CarryAll PM': 1400,
    'Looping': 1700,
    'Anytime MM': 1600,
    'Carmel': 1800,
    'Bella': 1600,
}




def add_to_cart(item):
    cart.append(item)
    print(f'Added to Cart: {cart}')

def add_bag_to_cart(bag_name):
    add_to_cart(bag_name)

def add_shoe_to_cart(shoe_name):
    add_to_cart(shoe_name)

def save_cart():
    with open('purchased_items.pkl', 'wb') as file:
        pickle.dump(cart, file)
    print("Cart saved successfully!")

def load_cart():
    try:
        with open('purchased_items.pkl', 'rb') as file:
            saved_cart = pickle.load(file)
            print("Purchased Items:")
            for item in saved_cart:
                price = bags.get(item, shoes.get(item))
                print(f"{item} - ${price}")
    except FileNotFoundError:
        print("No previous purchases found.")

new_frame = Frame(okno)

def view_shoes():
    global new_frame
    global second_frame
    second_frame.destroy()
    global shoes_visible

    new_frame = Frame(okno)
    new_frame.pack(fill=BOTH, expand=1)

    new_canvas = Canvas(new_frame)
    new_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    new_scrollbar = Scrollbar(new_frame, orient=VERTICAL, command=new_canvas.yview)
    new_scrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.configure(yscrollcommand=new_scrollbar.set) #связывание

    def new_config_this(event):
        new_canvas.configure(scrollregion=new_canvas.bbox('all'))

    new_canvas.bind('<Configure>', new_config_this)

    new_scroll_frame = Frame(new_canvas)
    new_canvas.create_window((0, 0), window=new_scroll_frame, anchor='nw')

    column = 3

    for new_index, shoe in enumerate(shoes):
        new_row = new_index // column
        new_column = new_index % column

        shoe_frame = Frame(new_scroll_frame, relief='solid', borderwidth=3)
        shoe_frame.grid(row=new_row,
                        column=new_column,
                        ipadx=50,
                        ipady=7,
                        padx=10, pady=10)

        new_label = Label(shoe_frame, text=shoe, font=('Times New Roman', 16))
        new_label.pack(pady=10)

        if shoe == 'Sneakerina':
           new_image = PhotoImage(file='sneakerina.png.png')
           new_image_label = Label(shoe_frame, image=new_image)
           new_image_label.image = new_image
           new_image_label.pack()

        if shoe == 'Pool Pillow':
           new_image_2 = PhotoImage(file='poolPillow.png.png')
           new_image_label = Label(shoe_frame, image=new_image_2)
           new_image_label.image = new_image_2
           new_image_label.pack()

        if shoe == 'Pool Comfort':
           new_image_3 = PhotoImage(file='poolComfort.png.png')
           new_image_label = Label(shoe_frame, image=new_image_3)
           new_image_label.image = new_image_3
           new_image_label.pack()

        if shoe == 'Trainer Sneaker':
           image_4 = PhotoImage(file='trainerSneaker.png.png')
           image_label = Label(shoe_frame, image=image_4)
           image_label.image = image_4
           image_label.pack()

        if shoe == 'Lvisola':
           image_5 = PhotoImage(file='lvisola.png.png')
           image_label = Label(shoe_frame, image=image_5)
           image_label.image = image_5
           image_label.pack()

        if shoe == 'Bomdia':
           image_6 = PhotoImage(file='bomdia.png.png')
           image_label = Label(shoe_frame, image=image_6)
           image_label.image = image_6
           image_label.pack()

        if shoe == 'Silhouette':
           image_7 = PhotoImage(file='silhouette.png.png')
           image_label = Label(shoe_frame, image=image_7)
           image_label.image = image_7
           image_label.pack()

        if shoe == 'Sneaker':
           image_8 = PhotoImage(file='Sneaker.png.png')
           image_label = Label(shoe_frame, image=image_8)
           image_label.image = image_8
           image_label.pack()

        if shoe == 'Mule':
           image_9 = PhotoImage(file='mule.png.png')
           image_label = Label(shoe_frame, image=image_9)
           image_label.image = image_9
           image_label.pack()

        if shoe == 'Shake':
           new_image_10 = PhotoImage(file='shake.png.png')
           new_image_label = Label(shoe_frame, image=new_image_10)
           new_image_label.image = new_image_10
           new_image_label.pack()

        if shoe == 'Sandal':
           new_image_11 = PhotoImage(file='sandal.png.png')
           new_image_label = Label(shoe_frame, image=new_image_11)
           new_image_label.image = new_image_11
           new_image_label.pack()

        if shoe == 'Berlin':
           new_image_12 = PhotoImage(file='berlin.png.png')
           new_image_label = Label(shoe_frame, image=new_image_12)
           new_image_label.image = new_image_12
           new_image_label.pack()

        if shoe == 'Lanad':
           new_image_13 = PhotoImage(file='lanad.png.png')
           image_label = Label(shoe_frame, image=new_image_13)
           image_label.image = new_image_13
           image_label.pack()

        if shoe == 'Wedge Sandal':
           new_image_14 = PhotoImage(file='wedgeSandal.png.png')
           image_label = Label(shoe_frame, image=new_image_14)
           image_label.image = new_image_14
           image_label.pack()

        if shoe == 'Flat Heilus':
           new_image_15 = PhotoImage(file='flatHeilus.png.png')
           image_label = Label(shoe_frame, image=new_image_15)
           image_label.image = new_image_15
           image_label.pack()

        if shoe == 'Swing':
           new_image_16 = PhotoImage(file='swing.png.png')
           image_label = Label(shoe_frame, image=new_image_16)
           image_label.image = new_image_16
           image_label.pack()

        if shoe == 'Allure':
           new_image_17 = PhotoImage(file='allure.png.png')
           image_label = Label(shoe_frame, image=new_image_17)
           image_label.image = new_image_17
           image_label.pack()

        if shoe == 'Sling Back':
           new_image_18 = PhotoImage(file='slingback.png.png')
           image_label = Label(shoe_frame, image=new_image_18)
           image_label.image = new_image_18
           image_label.pack()

        new_button = Button(shoe_frame,
                        text="Place in Cart",
                        command=partial(add_to_cart, shoe))
        new_button.pack(pady=10)


def open_cart():
    def remove_item(item_name, frame_widget):
        if item_name in cart:
            cart.remove(item_name)
            frame_widget.destroy()
            update_total()

    def update_total():
        total = 0
        for item in cart:
            total += bags.get(item, shoes.get(item))
        total_label.config(text=f"Total: ${total}")

    def confirm_purchase():
        if not cart:
            messagebox.showinfo("Info", "Cart is Empty !")
            return

        def process_payment():
            card_type = card_var.get()
            card_digits = card_entry.get()

            if card_type == "":
                messagebox.showerror("Error",
                                     "Please choose a card type.")
            elif len(card_digits) != 4 or not card_digits.isdigit():
                messagebox.showerror("Error",
                                     "Enter the last 4 "
                                     "digits of your card.")
            else:
                messagebox.showinfo("Success",
                                    f"Paid with {card_type}. "
                                    f"Thanks for buying!")

                save_cart()
                cart.clear()
                payment_window.destroy()
                cart_window.destroy()

        payment_window = Toplevel(cart_window)
        payment_window.title("Payment")
        payment_window.geometry("300x250")
        payment_window.resizable(False,False)

        Label(payment_window, text="Choose Card Type:",
              font=('Times New Roman', 12)).pack(pady=5)

        card_var = StringVar()
        visa_radio = Radiobutton(payment_window, text="Visa",
                                 variable=card_var, value="Visa")
        master_radio = Radiobutton(payment_window, text="MasterCard",
                                   variable=card_var, value="MasterCard")
        visa_radio.pack()
        master_radio.pack()

        Label(payment_window, text="Enter Last 4 Digits of Card:",
              font=('Times New Roman', 12)).pack(pady=5)
        card_entry = Entry(payment_window)
        card_entry.pack(pady=5)

        pay_button = Button(payment_window, text="Pay Now",
                            command=process_payment, bg='white',
                            fg='black')
        pay_button.pack(pady=10)

    cart_window = Toplevel(okno)
    cart_window.title("Added to Cart")
    cart_window.geometry('400x500')

    if not cart:
        label_empty = Label(cart_window,
                            text="Cart is empty!",
                            font=('Times New Roman', 16)
                            )
        label_empty.pack(pady=20)
    else:
        label_on_top = Label(cart_window,
                             text="Your Items:",
                             font=('Times New Roman', 16)
                             )
        label_on_top.pack(pady=10)


        for item in cart:
            frame = Frame(cart_window)
            frame.pack(pady=5, fill=X, padx=10)
            price = bags.get(item, shoes.get(item))
            label = Label(frame,
                            text=f"{item} - ${price}",
                            font=('Times New Roman', 16))
            label.pack(side=LEFT)

            remove_button = Button(frame,
                                text="Remove",
                                command=partial(remove_item, item, frame))

            remove_button.pack(side=RIGHT)


        total_label = Label(cart_window, font=('Times New Roman', 14, 'bold'))
        total_label.pack(pady=20)
        update_total()

        buy_button = Button(cart_window,
                         text="Buy",
                         command=confirm_purchase,
                         font=('Times New Roman', 14),
                         bg='white',
                         fg='black')
        buy_button.pack(pady=10)

second_frame = Frame(okno)

def view_bags():
    global second_frame

    def config_this(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    new_frame.destroy()
    second_frame = Frame(okno)
    second_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(second_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(second_frame, orient=VERTICAL,
                          command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', config_this)

    scroll_frame = Frame(canvas)
    canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

    columns = 3

    for index, bag in enumerate(bags):
            for_row = index // columns
            for_column = index % columns

            frame = Frame(scroll_frame, relief='solid', borderwidth=3)
            frame.grid(row=for_row, column=for_column,
                   ipadx=50, ipady=7,
                   padx=10, pady=10)

            label = Label(frame, text=bag, font=('Times New Roman', 16))
            label.pack(pady=10)


            if bag == 'Low Key Cookie':
               image = PhotoImage(file='cooka.png')
               image_label = Label(frame, image=image)
               image_label.image = image
               image_label.pack()

            if bag == 'High Rise PM':
               image_2 = PhotoImage(file='highrise.png')
               image_label = Label(frame, image=image_2)
               image_label.image = image_2
               image_label.pack()

            if bag == 'Never Full MM':
               image_3 = PhotoImage(file='neverfull.png')
               image_label = Label(frame, image=image_3)
               image_label.image = image_3
               image_label.pack()

            if bag == 'Diane':
               image_4 = PhotoImage(file='diane.png')
               image_label = Label(frame, image=image_4)
               image_label.image = image_4
               image_label.pack()

            if bag == 'All in BB':
               image_5 = PhotoImage(file='allinbb.png')
               image_label = Label(frame, image=image_5)
               image_label.image = image_5
               image_label.pack()

            if bag == 'No way Vibe':
               image_6 = PhotoImage(file='nowayvibe.png')
               image_label = Label(frame, image=image_6)
               image_label.image = image_6
               image_label.pack()

            if bag == 'Slouchy MM':
               image_7 = PhotoImage(file='slouchyMM.png')
               image_label = Label(frame, image=image_7)
               image_label.image = image_7
               image_label.pack()

            if bag == 'The Drop GM':
               image_8 = PhotoImage(file='thedropgm.png')
               image_label = Label(frame, image=image_8)
               image_label.image = image_8
               image_label.pack()

            if bag == 'Mini Bumbag':
               image_9 = PhotoImage(file='miniBumBag.png')
               image_label = Label(frame, image=image_9)
               image_label.image = image_9
               image_label.pack()

            if bag == 'Bobo Trunk':
               image_10 = PhotoImage(file='boboTrunk.png')
               image_label = Label(frame, image=image_10)
               image_label.image = image_10
               image_label.pack()

            if bag == 'Steamer 30':
               image_11 = PhotoImage(file='steamer30.png')
               image_label = Label(frame, image=image_11)
               image_label.image = image_11
               image_label.pack()

            if bag == 'Trunkie':
               image_12 = PhotoImage(file='trunkie.png')
               image_label = Label(frame, image=image_12)
               image_label.image = image_12
               image_label.pack()

            if bag == 'Keepit':
               image_13 = PhotoImage(file='keepIt.png')
               image_label = Label(frame, image=image_13)
               image_label.image = image_13
               image_label.pack()

            if bag == 'CarryAll PM':
               image_14 = PhotoImage(file='carryAll.png')
               image_label = Label(frame, image=image_14)
               image_label.image = image_14
               image_label.pack()

            if bag == 'Looping':
               image_15 = PhotoImage(file='Looping.png')
               image_label = Label(frame, image=image_15)
               image_label.image = image_15
               image_label.pack()

            if bag == 'Anytime MM':
               image_16 = PhotoImage(file='AnytimeMM.png')
               image_label = Label(frame, image=image_16)
               image_label.image = image_16
               image_label.pack()

            if bag == 'Carmel':
               image_17 = PhotoImage(file='Carmel.png')
               image_label = Label(frame, image=image_17)
               image_label.image = image_17
               image_label.pack()

            if bag == 'Bella':
               image_18 = PhotoImage(file='Bella.png')
               image_label = Label(frame, image=image_18)
               image_label.image = image_18
               image_label.pack()

            button=Button(frame,
                          text="Place in Cart",
                          command=partial(add_to_cart, bag))
            button.pack(pady=10)


def change_my_button():

    if change_button['text'] == "View Shoes":

        change_button.config(text="View Bags")
        change_button.pack(side=LEFT, padx=20)
        view_shoes()
    else:

        view_bags()
        change_button.config(text="View Shoes")
        change_button.pack(side=LEFT, padx=20)


view_bags()

bottom_frame = Frame(okno)
bottom_frame.pack(side=BOTTOM, pady=10)

change_button = Button(bottom_frame, text="View Shoes", command=change_my_button)
change_button.pack(side=LEFT, padx=20)

open_cart_button = Button(
    bottom_frame,
    text="View my Cart",
    command=open_cart,
    bg='white',
    fg='black',
    font=('Times New Roman', 14)
)
open_cart_button.pack(side=LEFT, padx=20)

load_cart()


okno.mainloop()



