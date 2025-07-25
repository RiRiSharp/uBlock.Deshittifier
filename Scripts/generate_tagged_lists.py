import sys
from pathlib import Path

from Scripts import metadata_filler, file_io, constants


def output_with_metadata(metadata: str, file_as_str: str, output_path: Path):
    combined_content = metadata + '\n' + file_as_str
    file_io.write_file_text_to_path(output_path, combined_content)

    print(f"Successfully prepended metadata and outputted to '{output_path}'.", file=sys.stdout)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Parameter missing. Usage: python prepend_template.py <list_directory> <template_directory> <output_directory>",
            file=sys.stderr)
        sys.exit(1)

    list_directory = sys.argv[1]

    template_directory = sys.argv[2]
    site_list_template_path = Path(f"{template_directory}/{constants.SITE_LIST}")
    ultra_list_template_path = Path(f"{template_directory}/{constants.ULTRA_LIST}")

    output_directory = sys.argv[3]

    metadata_template = file_io.read_file_as_text(site_list_template_path)
    all_files_in_folder = file_io.all_file_paths_in_directory(list_directory)
    ultra_list_lines = ""
    for file in all_files_in_folder:
        ultra_list_lines += '\n'
        file_lines = file_io.read_file_as_text(file)
        ultra_list_lines += file_lines + '\n'

        metadata = metadata_filler.fill_metadata_template(metadata_template, target_path=file)
        output_file_path = Path(f"{output_directory}/{file.name}")
        output_with_metadata(metadata, file_lines, output_file_path)

    metadata_template = file_io.read_file_as_text(ultra_list_template_path)
    metadata = metadata_filler.fill_metadata_template(metadata_template)
    output_file_path = Path(f"{output_directory}/ultralist.txt")
    output_with_metadata(metadata, ultra_list_lines, output_file_path)
