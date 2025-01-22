from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


# Function to create a single invoice
def create_invoice(file_name, invoice_details):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "INVOICE")

    # Invoice details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Invoice Number: {invoice_details['invoice_number']}")
    c.drawString(50, height - 120, f"Date: {invoice_details['date']}")
    c.drawString(50, height - 140, f"Customer Name: {invoice_details['customer_name']}")
    c.drawString(50, height - 160, f"Billing Address: {invoice_details['billing_address']}")

    # Item Details
    c.drawString(50, height - 200, "Item Details:")
    y_position = height - 220
    for item in invoice_details['items']:
        c.drawString(60, y_position,
                     f"{item['name']} - Quantity: {item['quantity']} - Unit Price: ${item['unit_price']} - Total: ${item['total']}")
        y_position -= 20

    # Subtotal, Tax, and Total
    c.drawString(50, y_position - 20, f"Subtotal: ${invoice_details['subtotal']}")
    c.drawString(50, y_position - 40, f"Tax ({invoice_details['tax_percent']}%): ${invoice_details['tax']}")
    c.drawString(50, y_position - 60, f"Total Amount Due: ${invoice_details['total_amount_due']}")

    # Payment Due Date
    c.drawString(50, y_position - 100, f"Payment Due Date: {invoice_details['due_date']}")

    # Save the PDF
    c.save()


# Function to generate multiple mock invoices
def generate_mock_invoices(output_dir, num_invoices):
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, num_invoices + 1):
        invoice_details = {
            "invoice_number": f"INV-{1000 + i}",
            "date": f"01/{20 + i}/2025",
            "customer_name": f"Customer {i}",
            "billing_address": f"{i * 10} Example Street, City {i}, State {i}, 12345",
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

        file_name = os.path.join(output_dir, f"Invoice_{i}.pdf")
        create_invoice(file_name, invoice_details)
    print(f"{num_invoices} mock invoices generated in '{output_dir}'.")


# Generate 5 mock invoices
output_directory = "mock_invoices"
generate_mock_invoices(output_directory, 5)
