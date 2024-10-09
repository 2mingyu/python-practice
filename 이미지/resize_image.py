from PIL import Image

# 원본 이미지 파일 경로
input_image_path = 'input_image.png'

# 변환된 이미지 저장 경로 및 크기
output_sizes = [
    (512, 512, 'output_image_512.png'),
    (192, 192, 'output_image_192.png'),
    (64, 64, 'output_image_64.png')
]

# 이미지 열기
img = Image.open(input_image_path)

# 각 크기로 이미지 변환 및 저장
for size in output_sizes:
    resized_img = img.resize((size[0], size[1]), Image.Resampling.LANCZOS)  # ANTIALIAS 대신 LANCZOS 사용
    resized_img.save(size[2])
    print(f"Image saved: {size[2]} with size {size[0]}x{size[1]}")
