from PIL import Image, ImageDraw, ImageFont
import os

# Function to create a single invoice as PNG
def create_invoice_png(file_name, invoice_details):
    # Image dimensions
    img_width, img_height = 800, 1000
    bg_color = "white"
    text_color = "black"

    # Create a blank white image
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load a font
    font_title = ImageFont.truetype("arial.ttf", 24)  # Adjust font size as needed
    font_body = ImageFont.truetype("arial.ttf", 16)

    # Header
    draw.text((50, 50), "INVOICE", fill=text_color, font=font_title)

    # Invoice details
    draw.text((50, 100), f"Invoice Number: {invoice_details['invoice_number']}", fill=text_color, font=font_body)
    draw.text((50, 130), f"Date: {invoice_details['date']}", fill=text_color, font=font_body)
    draw.text((50, 160), f"Customer Name: {invoice_details['customer_name']}", fill=text_color, font=font_body)
    draw.text((50, 190), f"Billing Address: {invoice_details['billing_address']}", fill=text_color, font=font_body)

    # Item Details
    y_position = 230
    draw.text((50, y_position), "Item Details:", fill=text_color, font=font_body)
    y_position += 30
    for item in invoice_details['items']:
        item_text = f"{item['name']} - Quantity: {item['quantity']} - Unit Price: ${item['unit_price']} - Total: ${item['total']}"
        draw.text((70, y_position), item_text, fill=text_color, font=font_body)
        y_position += 30

    # Subtotal, Tax, and Total
    draw.text((50, y_position + 20), f"Subtotal: ${invoice_details['subtotal']}", fill=text_color, font=font_body)
    draw.text((50, y_position + 50), f"Tax ({invoice_details['tax_percent']}%): ${invoice_details['tax']}", fill=text_color, font=font_body)
    draw.text((50, y_position + 80), f"Total Amount Due: ${invoice_details['total_amount_due']}", fill=text_color, font=font_body)

    # Payment Due Date
    draw.text((50, y_position + 130), f"Payment Due Date: {invoice_details['due_date']}", fill=text_color, font=font_body)

    # Save the image
    img.save(file_name)
    print(f"Invoice saved as {file_name}")

# Function to generate multiple mock invoices as PNG
def generate_mock_invoices_png(output_dir, num_invoices):
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, num_invoices + 1):
        invoice_details = {
            "invoice_number": f"INV-{1000 + i}",
            "date": f"01/{20 + i}/2025",
            "customer_name": f"Customer {i}",
            "billing_address": f"{i*10} Example Street, City {i}, State {i}, 12345",
            "items": [
                {"name": "Product A", "quantity": i, "unit_price": 10.00 + i, "total": (10.00 + i) * i},
                {"name": "Product B", "quantity": i + 1, "unit_price": 15.00 + i, "total": (15.00 + i) * (i + 1)},
            ],
            "subtotal": round((10.00 + i) * i + (15.00 + i) * (i + 1), 2),
            "tax_percent": 10,
            "tax": round(((10.00 + i) * i + (15.00 + i) * (i + 1)) * 0.1, 2),
            "total_amount_due": round(((10.00 + i) * i + (15.00 + i) * (i + 1)) * 1.1, 2),
            "due_date": f"02/{5 + i}/2025",
        }

        file_name = os.path.join(output_dir, f"Invoice_{i}.png")
        create_invoice_png(file_name, invoice_details)

    print(f"{num_invoices} mock invoices generated in '{output_dir}'.")

# Generate 5 mock invoices as PNG
output_directory = "mock_invoices_png"
generate_mock_invoices_png(output_directory, 5)
