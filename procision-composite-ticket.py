from PIL import Image

def generate_ticket(template_path, barcode_path, output_path):
    # 1. Open the background ticket template and the user's PIDBarcode
    ticket = Image.open(template_path).convert("RGBA")
    barcode = Image.open(barcode_path).convert("RGBA")

    # 2. Set the exact target dimensions to fit your white box frame
    # Adjust these values based on your Canva export resolution
    box_width = 160
    box_height = 280
    
    # Resize the barcode cleanly
    barcode_resized = barcode.resize((box_width, box_height), Image.Resampling.LANCZOS)

    # 3. Define the precise top-left (X, Y) pixel coordinates of the white box stub
    # Adjust these numbers to match the exact placement in your template
    x_offset = 75
    y_offset = 320

    # 4. Paste the barcode onto the ticket template
    ticket.paste(barcode_resized, (x_offset, y_offset), barcode_resized)

    # 5. Save the final high-resolution composite ticket
    ticket.save(output_path, "PNG")
    print(f"Successfully generated ticket: {output_path}")

if __name__ == "__main__":
    generate_ticket("ticket_template.png", "pid_barcode.png", "final_ticket.png")