from PIL import Image, ImageDraw, ImageOps

def make_rounded_corners(input_image_path, output_image_path, radius):
    # 이미지 열기
    img = Image.open(input_image_path).convert("RGBA")

    # 이미지 크기 가져오기
    width, height = img.size

    # 둥근 마스크 생성
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), (width, height)], radius=radius, fill=255)

    # 둥근 마스크를 적용하여 이미지의 모서리를 둥글게 만듦
    rounded_img = ImageOps.fit(img, (width, height))
    rounded_img.putalpha(mask)

    # 결과 이미지를 저장
    rounded_img.save(output_image_path, format="PNG")
    print(f"Image saved with rounded corners: {output_image_path}")

# 사용 예시
input_image_path = 'input_image.png'
output_image_path = 'output_image_rounded.png'
corner_radius = 50  # 원하는 둥근 모서리 반경 설정

make_rounded_corners(input_image_path, output_image_path, corner_radius)
