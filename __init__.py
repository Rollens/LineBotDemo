import vision_demo as vd
import demo as gpt

if __name__ == '__main__':
    print('Google cloud vision start.')
    t = vd.detect_text('pdf.jpeg')
    print('ChatGPT start.')
    sol = gpt.getAIsay(t)
    print(sol)