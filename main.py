from pyscript import document

def generate(event):

    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    quantity = document.querySelector("#quantity").value

    category = category[:3].upper()
    product = product[:3].upper()

    sku = category + product + quantity

    document.querySelector("#result").innerText = "SKU: " + sku