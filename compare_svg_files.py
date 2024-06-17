import difflib
import sys
import subprocess


def compare_svg_files(file1, file2, output_file):
    """_summary_
"       so sanh 2 file văn bản 
    Args:
        file1 (_type_): tên file 1 VD: a.txt
        file2 (_type_): tên file 2 VD: c:\a.txt
        output_file (_type_): tên file đầu ra. Nếu tên file đã tồn tại thì ghi đè
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as f_out:
        svg1 = f1.read()
        svg2 = f2.read()

        """ So sánh nội dung SVG  """
        diff = difflib.unified_diff(svg1.splitlines(), svg2.splitlines())

        # Ghi kết quả diff vào file
        f_out.writelines(diff)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: compare_svg_files.py <file1.svg> <file2.svg> <output.diff>')
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    subprocess.run(["ttf2svg", "..."])

    compare_svg_files(file1, file2, output_file)
