from pyscript import document

def generate_sku(event):
    category = document.querySelector("#category").value
    prod_name = document.querySelector("#prod_name").value
    stock_qty = document.querySelector("#stock_qty").value

    if prod_name == "" or stock_qty == "":
        document.querySelector("#sku-result").innerText = "Please fill in all fields."
        return

    name_code = prod_name[:3].upper()

    sku_code = category + "-" + name_code + "-" + str(stock_qty)

    document.querySelector("#sku-result").innerText = "Generated SKU: " + sku_code