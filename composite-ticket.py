from PIL import Image

def generate_ticket(template_path, barcode_path, output_path):
    # 1. Open the background ticket template and the user's PIDBarcode
    ticket = Image.open(template_path).convert("RGBA")
    barcode = Image.open(barcode_path).convert("RGBA")

    # 2. Set target dimensions scaled for your 6912x3456 template white box
    box_width = 850
    box_height = 1500
    
    # Resize the barcode cleanly
    barcode_resized = barcode.resize((box_width, box_height), Image.Resampling.LANCZOS)

    # Rotate the barcode 90 degrees so it fits sideways in the frame
    # (Use expand=True to ensure the dimensions swap cleanly without clipping)
    barcode_rotated = barcode_resized.rotate(90, expand=True)

    # 3. Precise top-left (X, Y) pixel coordinates for the white stub box on your canvas
    x_offset = 400
    y_offset = 1000

    # 4. Paste the rotated barcode onto the ticket template
    ticket.paste(barcode_rotated, (x_offset, y_offset), barcode_rotated)

    # 5. Save the final high-resolution composite ticket
    ticket.save(output_path, "PNG")
    print(f"Successfully generated ticket: {output_path}")

if __name__ == "__main__":
    generate_ticket("ticket_template.png", "pid_barcode.png", "final_ticket.png")
