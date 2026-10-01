from pyscript import document

def create_order(event):
    item = document.querySelector("#item_select").value
    qty_input = document.querySelector("#item_qty").value

    if qty_input == "":
        document.querySelector("#receipt-result").innerText = "Please enter a valid quantity."
        return

    quantity = int(qty_input)

    if item == "Americano":
        price = 99
    elif item == "Spanish Latte":
        price = 129
    elif item == "Cold Brew Malt":
        price = 189
    elif item == "Affogato":
        price = 159
    elif item == "Caramel Macchiato":
        price = 129
    else:
        price = 0

    total = price * quantity

    result_text = f"Order Summary:\nItem: {item}\nQuantity: {quantity}\nUnit Price: ₱{price}\nTotal Amount: ₱{total}"

    document.querySelector("#receipt-result").innerText = result_text