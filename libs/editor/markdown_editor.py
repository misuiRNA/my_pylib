import os


class MarkdownEditor:

    def __init__(self, file_name, mode=None):
        self._file_name = f"{file_name}.md"
        self._file = self._open_file(self._file_name, mode)

    def write(self, text):
        self._write_line(text)

    def write_title(self, title, level: int = 1):
        ext = "#"*level
        self._write_line(f"{ext} {title}")

    def write_table_head(self, head_list):
        head_list = self._to_str_list(head_list)
        head_str = "|" + "|".join(head_list) + "|"
        line_str = "|-"*len(head_list) + "|"
        self._write_line(head_str)
        self._write_line(line_str)

    def write_table_row(self, value_list):
        value_list = self._to_str_list(value_list)
        string = "|".join(value_list)
        self._write_line(string)

    def write_parting_line(self):
        self._write_line("---")

    def write_blanks(self, num: int = 1):
        self._write_line("\n"*num)

    def output(self):
        self._file.close()
        print(f"write '{self._file_name}' done!")

    def _write_line(self, string):
        self._file.writelines([string, "\n"])

    @staticmethod
    def _open_file(file_name, mode):
        if mode:
            fo = open(file_name, mode=mode)
            return fo
        if os.path.exists(file_name):
            os.remove(file_name)
        fo = open(file_name, mode="x")
        return fo

    @staticmethod
    def _to_str_list(item_list):
        item_list = [str(item) for item in item_list]
        return item_list
