from flask import Flask, render_template, request, redirect, url_for

from comic_book_generation import create_storyline
from io import BytesIO
import base64
app = Flask(__name__)


def pil_to_base64(img):
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    base64_img = base64.b64encode(img_io.getvalue()).decode('utf8')
    return f"data:image/png;base64,{base64_img}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        style = request.form['style']
        # return render_template('index.html', panels='strip.png')
        story = create_storyline(user_prompt, style)
        output_path = "static/strip.png"  # Save inside static directory
        story.save(output_path)
        return render_template('index.html', panels='strip.png')
    return render_template('index.html', panels=None)


def generate_image(prompt, style):
    # Placeholder for image generation logic
    # You can integrate an image generation API or model here
    return 'path_to_generated_image.jpg'

if __name__ == '__main__':
    app.run(debug=True)
