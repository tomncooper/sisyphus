from typing import List

COMMENT_CHARS: List[str] = ['"', "'", "#"]
CLASS_CHARS: str = "class"
FUNC_CHARS: str = "def"
TODO_MARKERS: List[str] = ["TODO"]


def parse_file(file_path: str):

    with open(file_path, "r") as parse_file:

        class_stack: List[str] = []
        func_stack: List[str] = []

        raw_line: str
        for line_no, raw_line in enumerate(parse_file, start=1):
            line: str = raw_line.strip()
            if len(line) > 0:

                if line.startswith(CLASS_CHARS):
                    class_name: str = line.split(CLASS_CHARS, maxsplit=1)[
                        -1
                    ].strip().split("(")[0]
                    class_stack.append(class_name)
                    print("CLASS")
                    print(class_name)
                elif line.startswith(FUNC_CHARS):
                    # TODO: We need to identify function that are not inside a class
                    # further up the file
                    func_name: str = line.split(FUNC_CHARS, maxsplit=1)[
                        -1
                    ].strip().split("(")[0]
                    func_stack.append(func_name)
                    print("FUNC")
                    print(func_name)
                elif line[0] in COMMENT_CHARS:
                    for todo_marker in TODO_MARKERS:
                        if todo_marker in line:
                            # TODO: We need to identify multi-line comments
                            todo_msg: str = line.split(todo_marker, maxsplit=1)[
                                -1
                            ].strip(" :")
                            print(f"Line {line_no}: {todo_msg}")


if __name__ == "__main__":

    parse_file("test_source.py")
