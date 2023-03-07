

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    print('Detecting...')
    texts = response.text_annotations
    for text in texts:
        print("Belowing is the texts detected by google cloud vision api")
        print('\n"{}"'.format(text.description))
        return text.description

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
if __name__ == "__main__":
    detect_text('pdf.jpeg')